import pandas as pd
import re

file_path = '/Users/mac/antigravity-testing-kit/Feature_01_PR_Quan_Ly_Bieu_Phi/test case/II.5.1.4.  PR.04- Danh sách Code phí chưa sử dụng.xlsx'
out_path = '/Users/mac/antigravity-testing-kit/Feature_01_PR_Quan_Ly_Bieu_Phi/test case/II.5.1.4.  PR.04- Danh sách Code phí chưa sử dụng.xlsx'

df = pd.read_excel(file_path)

# 1. Update TC_ID formats
def fix_tc_id(tc_id):
    if not isinstance(tc_id, str): return tc_id
    tc_id = tc_id.replace('br01', 'BR-01')
    tc_id = tc_id.replace('br02', 'BR-02')
    tc_id = tc_id.replace('br04', 'BR-04')
    # Standardize to uppercase
    return tc_id.upper()

df['TC_ID'] = df['TC_ID'].apply(fix_tc_id)

# 2. Fix copy-paste Expected Results for Filtering and Pagination
wrong_expected_happy = "(i) Nghiệp vụ/Logic: Thông tin được xử lý thành công và lưu trữ toàn vẹn dữ liệu.\n(ii) UI: Thông báo 'Thao tác thành công'.\n(iii) Trạng thái: 'Chờ duyệt' (Maker tạo mới)."
correct_expected_search_happy = "(i) Nghiệp vụ/Logic: Lưới dữ liệu cập nhật danh sách các bản ghi thỏa mãn điều kiện.\n(ii) UI: Hiển thị đúng kết quả tìm kiếm/phân trang trên lưới.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có."

# 3. Fix placeholder text for Boundary / Negative 
wrong_expected_boundary = "(i) Nghiệp vụ/Logic: Hệ thống xử lý đúng quy định tại giá trị biên (Min/Max/Limit).\n(ii) UI: Hiển thị thông báo hoặc trạng thái tương ứng.\n(iii) Trạng thái: Lưu hoặc Chặn tùy quy định."
correct_expected_boundary = "(i) Nghiệp vụ/Logic: Hệ thống xử lý thành công các điều kiện giới hạn/ngoại lệ.\n(ii) UI: Giao diện phản hồi hợp lý (Trống lưới / Thông báo lỗi / Cho phép thao tác nếu hợp lệ).\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có."

wrong_expected_negative = "(i) Nghiệp vụ/Logic: Hệ thống thực hiện kiểm tra và chặn dữ liệu/thao tác không hợp lệ.\n(ii) UI: Hiển thị đúng thông báo lỗi (Error message) theo quy tắc của trường dữ liệu/BR.\n(iii) Trạng thái: Không thay đổi dữ liệu gốc, không tạo bản ghi nháp."
correct_expected_negative = "(i) Nghiệp vụ/Logic: Chặn thao tác do không thỏa mãn điều kiện hoặc lưới rỗng.\n(ii) UI: Cảnh báo lỗi chi tiết trên màn hình (Ví dụ: Không tìm thấy kết quả phù hợp).\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Không có."


def fix_expected(row):
    expected = str(row['Expected']).strip()
    title = str(row['Title']).lower()
    tc_type = str(row['Type']).lower()
    
    # Neu la text sai cua Happy path
    if "Maker tạo mới" in expected:
        return correct_expected_search_happy
        
    # Neu la text sai cua Boundary
    if "tùy quy định" in expected:
        # Nếu chức năng tải xuống lớn
        if "tải trang trong giới hạn" in title or "đổi trang dưới ngưỡng" in title or "giới hạn dung lượng" in title:
            return "(i) Nghiệp vụ/Logic: Hệ thống tải dữ liệu mượt mà, không gặp lỗi Timeout.\n(ii) UI: Giao diện không bị treo, hiển thị Loading spinner nếu cần.\n(iii) Trạng thái bản ghi: Không thay đổi.\n(iv) Output: Thành công."
        elif "empty" in title or "rỗng" in title:
            return "(i) Nghiệp vụ/Logic: Lưới dữ liệu và bộ lọc xử lý an toàn khi không có bản ghi.\n(ii) UI: Hiển thị trạng thái lưới trống ('Không có dữ liệu').\n(iii) Trạng thái bản ghi: Không thay đổi."
        else:
            return correct_expected_boundary

    # Neu la text sai cua Negative
    if "Không thay đổi dữ liệu gốc" in expected and "thông báo lỗi (Error message)" in expected:
        if "không hiển thị các code phí" in title or "loại trừ code phí" in title:
            return "(i) Nghiệp vụ/Logic: Bộ đếm và câu lệnh query loại trừ chính xác trạng thái Hoạt động ngoài phạm vi.\n(ii) UI: Lưới không chứa bất cứ dòng nào có trạng thái Hoạt động. Nếu không có dòng nào khác thỏa mãn, hiển thị rỗng.\n(iii) Trạng thái bản ghi: Không thay đổi."
        else:
            return correct_expected_negative
        
    return expected

df['Expected'] = df.apply(fix_expected, axis=1)

# Add Note to flag automatic correction
def update_note(note):
    note_str = str(note)
    if note_str == 'nan' or not note_str.strip():
        note_str = "Auto-fixed Expected Result (Removed copy-paste errors/placeholders)."
    else:
        if "Auto-fixed" not in note_str:
            note_str += "\nAuto-fixed Expected Result (Removed copy-paste errors/placeholders)."
    return note_str

df['Note'] = df['Note'].apply(update_note)

df.to_excel(out_path, index=False)
print("Updated Test Cases successfully in", out_path)
