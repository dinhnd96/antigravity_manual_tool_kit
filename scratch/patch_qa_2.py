import re
import os

patches = {
    '01_v2': ",\n        ('QA-TC-01', 'Validation / Boundary', 'Code quy định độ dài (Max-length) của Mã và Tên SPDV cấp 1/2/3 là bao nhiêu ký tự? Ký tự đặc biệt nào bị cấm? Message lỗi khi nhập trùng Mã SPDV là gì?', 'Test Case / Boundary', 'Cần BA cung cấp message lỗi chính xác và rule Regex cho Input.', '')",
    '02': ",\n        ('QA-TC-01', 'Validation / Value', 'Tính năng VAT: Nếu chọn VAT là Có, tỉ lệ % giới hạn Min-Max là bao nhiêu? Cho phép lẻ tới mấy chữ số thập phân? (VD: 8.5%). Error msg khi nhập sai là gì?', 'Test Case / Boundary', 'Bổ sung Data Limit cho trường VAT %.', '')",
    '05': ",\n        ('QA-TC-01', 'Validation / Logic', 'Lỗi cú pháp Formula: Nếu user nhập công thức thiếu đóng ngoặc kép, sai biến thì hệ thống Validate báo lỗi message bằng chữ gì? Mã Code HTTP trả về là 400?', 'Test Case / Error handling', 'Yêu cầu Mapping bảng Error Messages cho công thức tính phí.', '')",
}

for num, patch in patches.items():
    file = f"scratch/generate_us{num}_qa_report.py"
    if file == "scratch/generate_us01_v2_qa_report.py":
        file = "scratch/generate_us01_qa_report_v2.py" # name mapping
    if not os.path.exists(file): continue
    with open(file, 'r') as f:
        content = f.read()
    
    if patch not in content:
        content = re.sub(r'(\n\s*\]\n\s*for)', patch + r'\1', content)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Patched {file}")
