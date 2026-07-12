import os
import shutil
import sqlite3
import base64
import subprocess

def check_ide_running():
    # Kiểm tra xem có tiến trình Antigravity IDE nào đang chạy không
    out = subprocess.getoutput('pgrep -f "Antigravity IDE"')
    if out.strip():
        return True
    return False

def sync():
    if check_ide_running():
        print("=" * 60)
        print("⚠️ CẢNH BÁO: Ứng dụng Antigravity IDE vẫn đang hoạt động!")
        print("Vui lòng ĐÓNG HOÀN TOÀN ứng dụng (Cmd + Q) trước khi chạy script.")
        print("=" * 60)
        return

    src_base = '/Users/mac/.gemini/antigravity'
    dst_base = '/Users/mac/.gemini/antigravity-ide'
    db_path = '/Users/mac/Library/Application Support/Antigravity IDE/User/globalStorage/state.vscdb'
    
    print("🚀 Bắt đầu đồng bộ lịch sử chat...")
    
    # 1. Đồng bộ file .pb trong conversations
    src_conv = os.path.join(src_base, 'conversations')
    dst_conv = os.path.join(dst_base, 'conversations')
    os.makedirs(dst_conv, exist_ok=True)
    for f in os.listdir(src_conv):
        if f.endswith('.pb'):
            shutil.copy2(os.path.join(src_conv, f), os.path.join(dst_conv, f))
    print("✅ Đã đồng bộ các file conversations.")
    
    # 2. Đồng bộ thư mục brain
    src_brain = os.path.join(src_base, 'brain')
    dst_brain = os.path.join(dst_base, 'brain')
    os.makedirs(dst_brain, exist_ok=True)
    for d in os.listdir(src_brain):
        src_d = os.path.join(src_brain, d)
        if os.path.isdir(src_d):
            dst_d = os.path.join(dst_brain, d)
            if os.path.exists(dst_d):
                shutil.rmtree(dst_d)
            shutil.copytree(src_d, dst_d)
    print("✅ Đã đồng bộ thư mục brain.")

    # 3. Đồng bộ annotations & implicit
    for folder in ['annotations', 'implicit']:
        src_f = os.path.join(src_base, folder)
        dst_f = os.path.join(dst_base, folder)
        if os.path.exists(src_f):
            if os.path.exists(dst_f):
                shutil.rmtree(dst_f)
            shutil.copytree(src_f, dst_f)
            print(f"✅ Đã đồng bộ thư mục {folder}.")

    # 4. Cập nhật database state.vscdb
    pb_path = os.path.join(src_base, 'agyhub_summaries_proto.pb')
    if os.path.exists(pb_path) and os.path.exists(db_path):
        # Đọc và mã hóa Base64 summaries file
        with open(pb_path, 'rb') as f:
            pb_data = f.read()
        encoded_data = base64.b64encode(pb_data).decode('utf-8')
        
        # Sao lưu db trước khi cập nhật
        backup_path = db_path + '.backup_script'
        shutil.copy2(db_path, backup_path)
        print("💾 Đã sao lưu database gốc.")
        
        # Ghi đè key trajectorySummaries trong database
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("UPDATE ItemTable SET value = ? WHERE key = 'antigravityUnifiedStateSync.trajectorySummaries'", (encoded_data,))
        conn.commit()
        conn.close()
        print("✅ Đã cập nhật danh sách cuộc hội thoại vào database IDE.")
    else:
        print("❌ Lỗi: Không tìm thấy file summaries hoặc database của IDE.")
        
    print("\n🎉 Đồng bộ hoàn tất! Bạn có thể mở lại Antigravity IDE ngay bây giờ.")

if __name__ == '__main__':
    sync()
