import pandas as pd

file_path = '/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/test case/Test_Cases_SA06_Danh_Muc_Dieu_Kien_Updated.xlsx'
output_path = '/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/test case/Test_Cases_SA06_Danh_Muc_Dieu_Kien_Updated_v2.xlsx'

df = pd.read_excel(file_path)

def format_expected(title, old_expected, type_case):
    title_lower = str(title).lower()
    if type_case == "Negative":
        if "trống" in title_lower or "bỏ trống" in title_lower:
            return "(i) Nghiệp vụ/Logic: Chặn người dùng, không cho phép lưu bản ghi.\n(ii) UI: Vẫn ở form hiện tại, focus và bôi đỏ ô lỗi, hiển thị text cảnh báo bắt buộc nhập.\n(iii) Trạng thái/Audit: Bản ghi không được tạo, không ghi log thao tác sửa đổi.\n(iv) Output: Không có file/message sinh ra."
        elif "trùng" in title_lower:
            return "(i) Nghiệp vụ/Logic: Hệ thống kiểm tra hàm unique trên DB và chặn không sinh bản ghi mới.\n(ii) UI: Hiển thị toast message/popup báo lỗi dữ liệu đã tồn tại.\n(iii) Trạng thái/Audit: Không tạo thay đổi bản ghi, không sinh log Audit thêm mới.\n(iv) Output: Không."
        elif "sửa trạng thái" in title_lower or "gán" in title_lower:
            return "(i) Nghiệp vụ/Logic: Từ chối hành động sửa do phát hiện ràng buộc dữ liệu đang gán.\n(ii) UI: Popup báo lỗi ràng buộc, dropdown trạng thái khôi phục lại giá trị cũ.\n(iii) Trạng thái/Audit: Trạng thái của bản ghi giữ nguyên.\n(iv) Output: Không."
        else:
            return "(i) Nghiệp vụ/Logic: Chặn lưu/xử lý với data sai.\n(ii) UI: Bắn popup lỗi hiển thị, focus field sai.\n(iii) Trạng thái/Audit: Không bị ảnh hưởng thay đổi gốc.\n(iv) Output: Không."
    elif type_case == "Happy":
        if "thêm mới" in title_lower and "điều hướng" not in title_lower and "đóng" not in title_lower:
             return "(i) Nghiệp vụ/Logic: Hệ thống xử lý lưu thành công bản ghi vào CSDL.\n(ii) UI: Toast thông báo 'Thêm mới thành công', popup tự đóng và Grid Grid reload hiện lên bản ghi vừa tạo.\n(iii) Trạng thái/Audit: Trạng thái bản ghi là 'Hoạt động', ghi log Audit vào bảng truy vết (Maker thông tin người tạo).\n(iv) Output: Không."
        elif "đóng" in title_lower or "hủy" in title_lower:
             return "(i) Nghiệp vụ/Logic: Xác nhận lệnh Hủy không lưu.\n(ii) UI: Form popup lập tức ẩn đóng lại, Grid dữ liệu hiện trường cũ không reload lại trang.\n(iii) Trạng thái/Audit: Không ghi log tạo hay update.\n(iv) Output: Không."
        elif "tìm kiếm" in title_lower:
             return "(i) Nghiệp vụ/Logic: Trả về tập dữ liệu matched theo input search.\n(ii) UI: Skeleton loading Grid, lưới hiển thị đúng các bản ghi lọc theo thông tin đưa vào.\n(iii) Trạng thái/Audit: Giữ nguyên lịch sử.\n(iv) Output: UI lưới (không xuất File)."
        elif "tải xuống" in title_lower or "export" in title_lower:
            return "(i) Nghiệp vụ/Logic: Khởi tạo và ghi Binary stream cho Data đang có ở lưới.\n(ii) UI: Biểu tượng download trigger.\n(iii) Trạng thái/Audit: Phụ thuộc rules của hệ thống sẽ ghi log (Tên user Export báo cáo).\n(iv) Output: Sinh File định dạng (.xlsx / .csv) chứa data table."
        elif "xem" in title_lower:
            return "(i) Nghiệp vụ/Logic: Trả về form object detail.\n(ii) UI: Popup Xem bật lên. Form chuyển đổi tất cả Field Input sang chế độ Read-only vô hiệu hóa sửa.\n(iii) Trạng thái/Audit: Không ảnh hưởng state gốc.\n(iv) Output: Không."
        elif "logic hiển thị" in title_lower or "định dạng" in title_lower:
             return "(i) Nghiệp vụ/Logic: Xác nhận cấu hình Dropdown tĩnh mảng Client hoặc Validation data Masked.\n(ii) UI: Dropdown option xổ đủ các items cần thiết Hoặc UI đỏ validation date.\n(iii) Trạng thái/Audit: Bổ trợ UI input.\n(iv) Output: Không."
        elif "sửa trạng thái" in title_lower:
             return "(i) Nghiệp vụ/Logic: Cho phép update cột status trực tiếp tại DB.\n(ii) UI: Báo cập nhật thành công, Lưới hiển thị tại cột Trạng thái chuyển đổi màu tag.\n(iii) Trạng thái/Audit: DB được update, Ghi lại log Audit sự kiện Update trạng thái do người dùng tạo.\n(iv) Output: Không."
        elif "luồng nghiệp vụ" in title_lower or "e2e" in title_lower:
             return "(i) Nghiệp vụ/Logic: Hành vi qua các màn hình và ràng buộc toàn vẹn thành công.\n(ii) UI: Chuyển hướng các trang, Toast thao tác qua lại ok.\n(iii) Trạng thái/Audit: Ghi log Audit đầy đủ xuyên suốt các Module, bản ghi đổi status chuẩn.\n(iv) Output: Config áp dụng hệ thống."
    
    return f"(i) Nghiệp vụ/Logic: Xử lý OK.\n(ii) UI: Giao diện reload.\n(iii) Trạng thái/Audit: Ghi \n(iv) Output: none."

for idx, row in df.iterrows():
    df.at[idx, 'Expected'] = format_expected(row['Title'], str(row['Expected']), row['Type'])

df.to_excel(output_path, index=False)
print("SUCCESS V2:", output_path)
