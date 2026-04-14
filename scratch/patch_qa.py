import re
import os
import glob

patches = {
    '14': ",\n        ('QA-TC-01', 'Validation / Boundary', 'Pagination: Lưới danh sách tối đa show bao nhiêu bản ghi mỗi trang? Dropdown SPDV có giới hạn load bao nhiêu item để tránh lag không?', 'Test Case / Boundary', 'Cần BA chốt size cụ thể để bổ sung vào Expected Result.', '')",
    '15': ",\n        ('QA-TC-01', 'Validation / Input', 'Điều kiện filter Ngày: Nếu người dùng nhập (Từ ngày > Đến ngày) thì message lỗi hiển thị chính xác string là gì? Có chặn submit không?', 'Test Case / Error Msg', 'Bổ sung mã lỗi và message text cho UI validate.', '')",
    '16': ",\n        ('QA-TC-01', 'Validation / Data trim', 'Ô tìm kiếm Mã CTƯĐ: Nếu search bằng cách paste dư khoảng trắng ở đầu/cuối, hệ thống có tự động Trim() khi truy vấn không?', 'Test Case / Data', 'Đề xuất Trim() toàn bộ khoảng trắng thừa để UX tốt hơn.', '')",
    '17': ",\n        ('QA-TC-01', 'Validation / Phone', 'Trường Số ĐT (Tra cứu CIF): Hệ thống có validate format số ĐT (ví dụ start=0, length=10-11) hay chỉ quan tâm không bỏ trống? Message lỗi khi nhập chữ cái là gì?', 'Test Case / Input Validate', 'Nêu rõ regex của phone number.', '')",
    '18': ",\n        ('QA-TC-01', 'Data Format / UI', 'Cột Số tiền phí/quy đổi VNĐ: Có áp dụng format dấu phẩy phân cách hàng nghìn (1,000,000) không? Nếu ra tiền lẻ VNĐ thì hệ thống quy tròn (Round) lên hay xuống?', 'Test Case / Display', 'Chốt quy tắc làm tròn (Round/Ceil/Floor) để so sánh expected result.', '')",
    '19': ",\n        ('QA-TC-01', 'Boundary / Date', 'Ràng buộc 1 năm cho khoảng ngày: Nếu chọn khoảng > 1 năm, validation message lỗi hiển thị chính xác từng chữ là gì? Nếu Từ ngày ở tương lai thì sao?', 'Test Case / Boundary', 'Cung cấp Error Message cụ thể để Tester viết Expected Result.', '')",
}

for num, patch in patches.items():
    file = f"scratch/generate_us{num}_qa_report.py"
    if not os.path.exists(file): continue
    with open(file, 'r') as f:
        content = f.read()
    
    # Insert patch before the closing bracket of qa_data list
    # Assuming qa_data ends with \n    ]
    if patch not in content:
        content = re.sub(r'(\n\s*\]\n\s*for)', patch + r'\1', content)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Patched {file}")
