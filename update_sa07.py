import pandas as pd

file_path = '/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/test case/Test_Cases_SA07_Quan_Ly_Nhom_Khach_Hang.xlsx'
output_path = '/Users/mac/antigravity-testing-kit/Feature_02_SA_Tham_So_He_Thong/test case/Test_Cases_SA07_Quan_Ly_Nhom_Khach_Hang_Updated.xlsx'

df = pd.read_excel(file_path)

df = df.astype(str)
df = df.replace('nan', '')

# Update title of existing Test Case SA07-BR03-NEG-004
for i in range(len(df)):
    if "linh hoạt" in str(df.at[i, 'Title']).lower():
        df.at[i, 'Title'] = "Kiểm tra không được phép sửa Trạng thái khi Nhóm KH đang gán với Code phí trạng thái Hoạt động/Ngừng hoạt động/Chờ gán"

row_template = df.iloc[0].copy()

# Add 3 missing Test Cases
row_1 = row_template.copy()
row_1['BR_Ref'] = 'BR_01'
row_1['Title'] = "Kiểm tra danh sách 'Trạng thái' hiển thị đầy đủ 2 giá trị [Hoạt động, Không hoạt động]"
row_1['Type'] = "Happy"
row_1['Category'] = "Smoke"
row_1['Priority'] = "P2"
row_1['Precondition'] = "Truy cập màn hình Thêm mới/Sửa."
row_1['Steps'] = "1. Click Dropdown trường 'Trạng thái'."
row_1['Expected'] = "(i) Nghiệp vụ/Logic: Frontend map đúng list tĩnh.\n(ii) UI: Dropdown hiển thị chuẩn 2 lựa chọn: Hoạt động, Không hoạt động.\n(iii) Trạng thái/Audit: Không đổi bản ghi CSDL.\n(iv) Output: Không sinh message."

row_2 = row_template.copy()
row_2['BR_Ref'] = 'BR_02'
row_2['Title'] = "Kiểm tra chức năng Đóng popup Thêm mới không lưu thông tin vào DB"
row_2['Type'] = "Happy"
row_2['Category'] = "Regression"
row_2['Priority'] = "P3"
row_2['Precondition'] = "Đang điền dở dữ liệu màn hình Thêm mới."
row_2['Steps'] = "1. Nhập một số thông tin (Mã nhóm, Tên nhóm).\n2. Nhấn nút 'Đóng'."
row_2['Expected'] = "(i) Nghiệp vụ/Logic: Hủy thao tác lưu trữ.\n(ii) UI: Form popup trực tiếp đóng lại. Quay về đúng trang cấu hình danh sách.\n(iii) Trạng thái/Audit: CSDL báo không có biến động, không sinh log Audit.\n(iv) Output: Bỏ qua (không)."

row_3 = row_template.copy()
row_3['BR_Ref'] = 'BR_03'
row_3['Title'] = "Kiểm tra cho phép sửa Trạng thái đối với Nhóm KH hoàn toàn chưa được gán Code phí nào"
row_3['Type'] = "Happy"
row_3['Category'] = "Regression"
row_3['Priority'] = "P2"
row_3['Precondition'] = "Mở 1 bản ghi Nhóm KH mới (chưa phát sinh gán chéo)."
row_3['Steps'] = "1. Edit Mode -> Đổi trạng thái từ Hoạt động xuống Không hoạt động.\n2. Nhấn 'Xác nhận'."
row_3['Expected'] = "(i) Nghiệp vụ/Logic: Ràng buộc Code phí = rỗng => System bypass.\n(ii) UI: Báo cập nhật thành công, Lưới hiển thị dòng KH đổi tag trạng thái màu xám.\n(iii) Trạng thái/Audit: Ghi đè trạng thái tại DB, lưu vết log Update Audit Maker.\n(iv) Output: Không đẩy message."

df_new = pd.DataFrame([row_1, row_2, row_3])
df = pd.concat([df, df_new], ignore_index=True)

def standardize_expected(title, type_case, old_expected):
    title_lower = str(title).lower()
    if "(i) Nghiệp vụ/Logic" in str(old_expected):
        return old_expected # already processed manually above
    
    if type_case == "Negative":
        if "trống" in title_lower or "bắt buộc" in title_lower:
            return "(i) Nghiệp vụ/Logic: Hệ thống detect trường bắt buộc rỗng, chặn gọi API.\n(ii) UI: Màn hình KHÔNG TẮT, chèn text đỏ dưới ô field 'Trường này bắt buộc'.\n(iii) Trạng thái/Audit: Hủy lệnh trên DB.\n(iv) Output: Trống."
        elif "chặn" in title_lower or "không được phép" in title_lower or "hiệu lực" in title_lower:
            return "(i) Nghiệp vụ/Logic: Check Validation thấy bảng Code phí đang dính trạng thái Hoạt động/Ngừng hoạt động/Chờ gán => Trả về Error.\n(ii) UI: Show popup cảnh báo lỗi không thể đổi.\n(iii) Trạng thái/Audit: Form roll-back lại data. DB không cập nhật trạng thái.\n(iv) Output: Không."
        elif "báo lỗi" in title_lower or "định dạng" in title_lower:
            return "(i) Nghiệp vụ/Logic: Báo lỗi ký tự validate input.\n(ii) UI: Phản hồi tooltip lỗi format đỏ.\n(iii) Trạng thái/Audit: Không tiến vào tầng DB để ghi gì cả.\n(iv) Output: Bỏ qua."
    elif type_case == "Happy":
        if "điều hướng" in title_lower:
             return "(i) Nghiệp vụ/Logic: Route sang trang mới.\n(ii) UI: Bật Layer popup Thêm Mới với các controls rỗng sẵn sàng nhập.\n(iii) Trạng thái/Audit: Không.\n(iv) Output: Load view."
        elif "operator" in title_lower or "hiển thị đầy đủ" in title_lower:
             return "(i) Nghiệp vụ/Logic: Parsing List Option Data.\n(ii) UI: Nhấn dropdown nhảy ra đúng ['=', 'IN'].\n(iii) Trạng thái/Audit: Data view only.\n(iv) Output: Không xuất file."
        elif "dấu phẩy" in title_lower and "in" in title_lower:
             return "(i) Nghiệp vụ/Logic: System chẻ chuỗi comma-separated để gán qua object List Backend.\n(ii) UI: Form accept submit thành công, lưới đổ data.\n(iii) Trạng thái/Audit: Create bản ghi mới cùng mảng giá trị đó tương ứng (Log event Create).\n(iv) Output: Không sinh message Kafka."
        elif "trim" in title_lower or "khoảng trắng" in title_lower:
             return "(i) Nghiệp vụ/Logic: String Utils tự động cắt Space dư thừa lúc submit.\n(ii) UI: Không bắn lỗi. \n(iii) Trạng thái/Audit: Dữ liệu sạch đưa thẳng xuống bảng DB, insert Success log Audit.\n(iv) Output: Report rỗng."
        elif "hủy" in title_lower and "sửa trạng thái" in title_lower:
             return "(i) Nghiệp vụ/Logic: Query thấy ALL Code phí gán cùng = 'Hủy' => Cho phép Update.\n(ii) UI: Green notification updated.\n(iii) Trạng thái/Audit: DB gán giá trị mới đè cũ, Audit nhận người Update.\n(iv) Output: Output Log none."
        elif "xem" in title_lower:
             return "(i) Nghiệp vụ/Logic: Lấy DTO show.\n(ii) UI: Popup bật với các ô nhập liệu dạng Read-only bôi màu disable xám.\n(iii) Trạng thái/Audit: DB Readonly.\n(iv) Output: none."
        elif "e2e" in title_lower or "luồng" in title_lower:
             return "(i) Nghiệp vụ/Logic: Ràng buộc cascade liên bảng DB thành công.\n(ii) UI: View map chuẩn từng Step.\n(iii) Trạng thái/Audit: CSDL insert liên hoàn, sau cùng chốt lỗi chặn.\n(iv) Output: E2E check passed."
    
    return "(i) Nghiệp vụ/Logic: Generic Success.\n(ii) UI: Action Done.\n(iii) Trạng thái/Audit: Auditable DB Transaction.\n(iv) Output: Không."

for idx, row in df.iterrows():
    df.at[idx, 'Expected'] = standardize_expected(row['Title'], row['Type'], row['Expected'])

# Gen id sequence
df['TC_ID'] = [f"TC_SA07_{str(i+1).zfill(3)}" for i in range(len(df))]

df.to_excel(output_path, index=False)
print("Updated to:", output_path)
