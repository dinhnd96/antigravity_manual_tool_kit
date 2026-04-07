import pandas as pd
import os

file_path = "/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/test case/SA07_Quan_Ly_Nhom_Khach_Hang_Updated.xlsx"
df = pd.read_excel(file_path, na_filter=False)

# Clean up Role 'Maker' -> 'Người dùng', 'Đăng nhập Maker' -> 'Đăng nhập tài khoản được phân quyền'
df['Precondition'] = df['Precondition'].str.replace('Đăng nhập Maker.', 'Đăng nhập tài khoản được phân quyền.')
df['Precondition'] = df['Precondition'].str.replace('Maker,', 'Tại')
df['Precondition'] = df['Precondition'].str.replace('Maker.', 'Từ màn hình hệ thống.')
df['Steps'] = df['Steps'].str.replace('Maker', 'Người dùng')

# Row by row modifications
new_rows = []

for index, row in df.iterrows():
    tcid = row['TC_ID']
    
    if tcid == 'TC_SA07_005':
        row['Title'] = "Kiểm tra báo lỗi đỏ dưới field khi để trống các trường bắt buộc"
        row['Comment'] = ""
    
    if tcid == 'TC_SA07_008':
        row['Precondition'] = "1. Đăng nhập tài khoản được phân quyền.\n2. Ở menu trang chủ."
        row['Steps'] = "1. Từ menu trái, chọn tính năng Quản lý nhóm khách hàng -> Hiển thị danh sách.\n2. Chọn nút Thêm mới.\n3. Quan sát layer popup vừa mở."
        row['Comment'] = ""
        
    if tcid == 'TC_SA07_006':
        row['Precondition'] = "1. Đăng nhập tài khoản được phân quyền.\n2. Bản ghi Nhóm KH 'NHOM_TEST' đang ở trạng thái Hoạt động VÀ đang gán vào 1 Code phí trạng thái Hoạt động."
        row['Steps'] = "1. Chọn Sửa Nhóm KH 'NHOM_TEST'. \n2. Đổi trạng thái từ Hoạt động sang Không hoạt động. \n3. Nhấn 'Xác nhận'."
        row['Comment'] = ""
        row['Title'] = "Kiểm tra không được phép sửa Trạng thái khi Nhóm KH Hoạt động đang gán với Code phí trạng thái Hoạt động"
        new_rows.append(row.copy())
        
        # Add 2 more variations
        row2 = row.copy()
        row2['TC_ID'] = 'TC_SA07_006_B'
        row2['Precondition'] = row2['Precondition'].replace('trạng thái Hoạt động.', 'trạng thái Ngừng hoạt động.')
        row2['Title'] = row2['Title'].replace('trạng thái Hoạt động', 'trạng thái Ngừng hoạt động')
        new_rows.append(row2)
        
        row3 = row.copy()
        row3['TC_ID'] = 'TC_SA07_006_C'
        row3['Precondition'] = row3['Precondition'].replace('trạng thái Hoạt động.', 'trạng thái Chờ gán.')
        row3['Title'] = row3['Title'].replace('trạng thái Hoạt động', 'trạng thái Chờ gán')
        new_rows.append(row3)
        continue

    # Clean MASS mock data
    if tcid == 'TC_SA07_007':
        row['Precondition'] = row['Precondition'].replace("'MASS'", "'NHOM_TEST'")
        row['Steps'] = row['Steps'].replace("'MASS'", "'NHOM_TEST'")
        
    if tcid == 'TC_SA07_010':
        row['Comment'] = ""
        row['Precondition'] = "1. Đăng nhập tài khoản được phân quyền.\n2. Hệ thống chưa có bản ghi Nhóm KH 'NEW_GROUP'."
        
    # Append current row
    new_rows.append(row)

    if tcid == 'TC_SA07_001':
        # Add TC_SA07_001_A (operator IN with 1 value)
        row_A = row.copy()
        row_A['TC_ID'] = 'TC_SA07_001_A'
        row_A['Title'] = "Kiểm tra nhập liệu 1 giá trị không có dấu phẩy khi chọn Operator = 'IN'"
        row_A['Type'] = "Happy"
        row_A['Priority'] = "P2"
        row_A['Steps'] = "1. Tại form Thêm mới, chọn Operator = 'IN'.\n2. Nhập 1 giá trị duy nhất (không có dấu phẩy). \n3. Nhấn Xác nhận."
        row_A['Expected'] = "(i) Nghiệp vụ/Logic: Nhận diện list có 1 phần tử.\n(ii) UI: Form lưu bình thường.\n(iii) Trạng thái/Audit: Ghi xuống CSDL.\n(iv) Output: Không."
        row_A['Trace_ID'] = "BR01-IN-SINGLE"
        row_A['Comment'] = ""
        new_rows.append(row_A)
        
        # Add TC_SA07_001_B (operator = with 1 value)
        row_B = row.copy()
        row_B['TC_ID'] = 'TC_SA07_001_B'
        row_B['Title'] = "Kiểm tra nhập liệu 1 giá trị hợp lệ khi chọn Operator = '='"
        row_B['Type'] = "Happy"
        row_B['Priority'] = "P2"
        row_B['Steps'] = "1. Tại form Thêm mới, chọn Operator = '='.\n2. Nhập 1 giá trị duy nhất. \n3. Nhấn Xác nhận."
        row_B['Expected'] = "(i) Nghiệp vụ/Logic: Xử lý theo equals.\n(ii) UI: Form lưu bình thường, không báo lỗi.\n(iii) Trạng thái/Audit: Ghi CSDL.\n(iv) Output: Không."
        row_B['Trace_ID'] = "BR01-EQUAL-SINGLE"
        row_B['Comment'] = ""
        new_rows.append(row_B)

    # After TC_SA07_013, add the reverse logic
    if tcid == 'TC_SA07_013':
        row_rev = row.copy()
        row_rev['TC_ID'] = 'TC_SA07_013_REV'
        row_rev['Title'] = "Kiểm tra cho phép sửa Trạng thái từ Không hoạt động sang Hoạt động đối với Nhóm KH hoàn toàn chưa được gán Code phí nào"
        row_rev['Precondition'] = "1. Đăng nhập tài khoản được phân quyền.\n2. Mở 1 bản ghi Nhóm KH đang ở trạng thái Không hoạt động (chưa phát sinh gán chéo)."
        row_rev['Steps'] = "1. Edit Mode -> Đổi trạng thái từ Không hoạt động lên Hoạt động.\n2. Nhấn 'Xác nhận'."
        row_rev['Expected'] = "(i) Nghiệp vụ/Logic: Rất thỏa mãn BR03 chiều ngược.\n(ii) UI: Báo cập nhật thành công, Lưới hiển thị dòng KH đổi tag trạng thái.\n(iii) Trạng thái/Audit: Ghi đè trạng thái 'Hoạt động' tại DB, lưu vết log Update Audit Maker.\n(iv) Output: Không đẩy message."
        row_rev['Trace_ID'] = "BR03-REVERSE"
        row_rev['Comment'] = ""
        new_rows.append(row_rev)

# Rebuild dataframe
df_new = pd.DataFrame(new_rows)
# Clean 'Comment' column across all
df_new['Comment'] = ""

output_file = "/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/test case/SA07_Quan_Ly_Nhom_Khach_Hang_Final.xlsx"
df_new.to_excel(output_file, index=False)
print("Success:", output_file)
