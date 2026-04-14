import pandas as pd
import os

file_path = '/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/test case/Test_Cases_SA06_Danh_Muc_Dieu_Kien.xlsx'
output_path = '/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/test case/Test_Cases_SA06_Danh_Muc_Dieu_Kien_Updated.xlsx'

df = pd.read_excel(file_path)

row_br03 = df.iloc[1].copy()

row_1 = row_br03.copy()
row_1['Title'] = "Kiểm tra báo lỗi khi Thêm mới trùng [Tên điều kiện] đã tồn tại trên hệ thống"
row_1['Steps'] = "1. Nhập Tên điều kiện = 'Tên điều kiện mẫu'. \n2. Nhập đầy đủ các trường khác. \n3. Nhấn 'Xác nhận'."
row_1['Trace_ID'] = "BR03-UNIQUE-NAME"

row_2 = row_br03.copy()
row_2['Title'] = "Kiểm tra báo lỗi khi Thêm mới trùng cả [Tên điều kiện] và [Mã điều kiện] đã tồn tại trên hệ thống"
row_2['Steps'] = "1. Nhập Mã điều kiện = 'COND001'. \n2. Nhập Tên điều kiện = 'Tên điều kiện mẫu'. \n3. Nhập đầy đủ các trường khác. \n4. Nhấn 'Xác nhận'."
row_2['Trace_ID'] = "BR03-UNIQUE-BOTH"

df_top = df.iloc[:2].copy()
df_bottom = df.iloc[2:].copy()
df_new = pd.DataFrame([row_1, row_2])
df = pd.concat([df_top, df_new, df_bottom], ignore_index=True)

def format_expected(title, old_expected, type_case):
    title_lower = str(title).lower()
    if type_case == "Negative":
        if "trống" in title_lower or "bỏ trống" in title_lower:
            return "(1) UI: Hiển thị cảnh báo đỏ dưới field bắt buộc, thông báo 'Trường này bắt buộc nhập'.\n(2) API Action: Hệ thống chặn gửi request do validation frontend.\n(3) Database: Không lưu thay đổi vào CSDL.\n(4) Form State: Màn hình cảnh báo giữ nguyên, text đang gõ vẫn giữ lại."
        elif "trùng" in title_lower:
            return "(1) UI: Hiển thị toast message/popup báo lỗi cụ thể (dữ liệu đã tồn tại).\n(2) API Action: Gửi request lên API nhận response 400 báo lỗi trùng lặp.\n(3) Database: Yêu cầu bị rollback, không sinh bản ghi mới.\n(4) Form State: Màn hình giữ nguyên nhập liệu."
        elif "sửa trạng thái" in title_lower or "gán" in title_lower:
            return "(1) UI: Cảnh báo 'Không thể thay đổi trạng thái' do dính ràng buộc.\n(2) API Action: Tuyên truy validation ràng buộc.\n(3) Database: Trạng thái không bị ghi đè.\n(4) Form State: Trường trạng thái load lại giá trị cũ."
    elif type_case == "Happy":
        if "thêm mới" in title_lower and "điều hướng" not in title_lower and "đóng" not in title_lower:
             return "(1) UI: Hiển thị thông báo 'Thêm mới thành công'.\n(2) API Action: Code 200 OK cho lệnh tạo.\n(3) Database: Sinh dòng dữ liệu mới trong bảng.\n(4) Form State: Bảng danh sách load lại bản ghi mới thêm."
        elif "đóng" in title_lower or "hủy" in title_lower:
             return "(1) UI: Modal bị đóng, không báo lỗi.\n(2) API Action: Không phát sinh API tạo mới.\n(3) DB: Không có dữ liệu chui vào.\n(4) Form State: Trở lại màn hình danh sách."
        elif "tìm kiếm" in title_lower:
             return "(1) UI: Lưới load lại.\n(2) API Action: Trả về kết quả search params.\n(3) DB: DB filter.\n(4) Form State: Bảng update data source."
        elif "tải xuống" in title_lower or "export" in title_lower:
            return "(1) UI: Chớp download.\n(2) API: Sinh excel stream.\n(3) DB: Data read.\n(4) Form State: File về máy thành công."
        elif "xem" in title_lower:
            return "(1) UI: Popup Xem bật lên với đúng detail record click vào.\n(2) API Action: GET detail code 200.\n(3) DB: Không.\n(4) Form State: Field readonly, không button thao tác."
        elif "logic hiển thị" in title_lower:
            return "(1) UI: Ẩn/hiện field theo event.\n(2) API: local.\n(3) DB: Không.\n(4) Form State: Toggle layout."
        elif "định dạng" in title_lower and "ngày tháng" in title_lower:
             return "(1) UI: Bắt sai định dạng ngay tại frontend.\n(2) API: pass format.\n(3) DB: Lưu Date.\n(4) Form State: field nhập đúng màu bình thường."
        elif "định dạng chuẩn" in title_lower:
             return "(1) UI: Mở sổ list Dropdown 4 field.\n(2) API: local.\n(3) DB: none.\n(4) Form State: list sổ phần tử."
        elif "sửa trạng thái" in title_lower:
             return "(1) UI: Báo cập nhật thành công.\n(2) API Action: Update status code 200.\n(3) DB: Update field.\n(4) Form State: Lưới đổi label trạng thái."
        elif "luồng nghiệp vụ" in title_lower or "e2e" in title_lower:
             return "(1) UI: Thao tác thông báo liên tục.\n(2) API: Gọi api gán thành công 200.\n(3) DB: Lưu quan hệ DB.\n(4) Form State: End với lỗi ràng buộc hệ thống."
    return f"(1) UI: Hành động diễn ra ổn định.\n(2) API: Thực thi code phù hợp.\n(3) DB: Commit or Read only.\n(4) Form State: Update tương ứng. (Gốc: {old_expected})"

for idx, row in df.iterrows():
    df.at[idx, 'Expected'] = format_expected(row['Title'], row['Expected'], row['Type'])

df['TC_ID'] = [f"TC_SA06_{str(i+1).zfill(3)}" for i in range(len(df))]

df.to_excel(output_path, index=False)
print("SUCCESS:", output_path)
