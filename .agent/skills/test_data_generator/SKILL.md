---
name: test_data_generator
description: Kỹ năng Test Data Engineer để sinh dữ liệu kiểm thử (Mock Data) chuẩn xác dựa trên Test Case hoặc định dạng Schema, phục vụ Manual Test hoặc Automation (Data-driven).
---

# Kỹ năng Sinh Dữ Liệu Kiểm Thử (Test Data Generator)

Kỹ năng này định hướng AI hoạt động như một Data Engineer phục vụ trực tiếp cho đội Test (QA).
Nhiệm vụ chính: Từ danh sách Test Case hoặc bảng cấu trúc Data Schema do user cung cấp, tự động bóc tách các điều kiện biên (Boundary value), điều kiện bất thường (Negative cases) và điều kiện chuẩn (Happy cases) để **sinh ra một tập dữ liệu giả lập (Mock Data) cực kỳ thực tế.**

## 1. Yêu Cầu Về Nghiệp Vụ Sinh Dữ Liệu
AI phải luôn phân tích kỹ các điều kiện trong Test Case để sinh data sao cho khớp:
- **Dữ liệu Hợp lệ (Valid/Happy):** Các dòng dữ liệu hoàn hảo, vượt qua mọi form validation. (VD: "Nguyễn Văn A", Số ĐT: "0981234567").
- **Dữ liệu Không Hợp lệ (Invalid/Negative):** Cố ý làm sai format chuẩn để bắt lỗi bắt Exception của hệ thống. (VD: SĐT thừa số "09812345678", Email "nguyenvan.a@@gmail.com", Tuổi "-5").
- **Dữ liệu Biên (Boundary):** Dữ liệu chạm sát giới hạn (Ví dụ: Số tiền tối đa "999,999,999", Chuỗi string dài đúng 255 ký tự).

## 2. Tính Đặc Thù Bản Địa (Localization - Tiếng Việt)
Nếu không có yêu cầu đặc biệt từ user, mặc định sinh dữ liệu với bối cảnh Việt Nam:
- **Tên người:** Tên chuẩn Việt Nam có dấu (Trần Thị Bích, Lê Văn Cường...).
- **Số điện thoại:** Đầu số các nhà mạng VN hợp lệ (Viettel 098/03x, Mobi 090/07x, Vina 091/08x).
- **Căn Cước Công Dân (CCCD):** Dãy số 12 chữ số hợp lệ.
- **Tài khoản ngân hàng:** Dãy số thực tế hoặc tên định dạng phổ biến.

## 3. Quy Tắc Đầu Ra (Output Format)
AI trả kết quả qua 2 bước:
1. **Phân tích chiến lược:** Chỉ ra có bao nhiêu Test Case, từ đó nhóm thành bao nhiêu loại Data (VD: Nhóm data đăng ký thành công, Nhóm data đăng ký thất bại do CCCD sai...).
2. **Cung cấp File Script Sinh Data:** Mặc định AI **phải tự viết mã Python (dùng thư viện `Faker`, `pandas` hoặc `csv`)** thông qua công cụ `write_to_file`, sau đó gọi công cụ `run_command` để chạy script và sinh thẳng ra một file `.csv`, `.xlsx` hoặc `.json` trên đĩa gốc (VD: `/Users/mac/antigravity-testing-kit/TestData.csv`). 
*Không yêu cầu user tự copy paste một cục text vĩ đại trừ khi user chỉ xin vài dòng mẫu.*

## 4. Xử Lý Luồng Đặc Biệt
- **Tính lặp (Volume):** Nếu user yêu cầu "sinh 10,000 dòng" -> BẮT BUỘC phải dùng Python script để sinh ra file cục bộ. Không in ra cửa sổ chat.
- **Tính liên kết (Relational Data):** Nếu có nhiều bảng (Ví dụ Bảng User và Bảng Đơn Hàng) -> Đảm bảo ID liên kết giữa các file/bảng phải matching thực tế (Foreign Keys).
- **Tránh Hallucination:** Nếu format User đưa cho quá phức tạp (Ví dụ JSON API Payload chứa 3 tầng Object), AI phải sinh cấu trúc test data tôn trọng 100% định nghĩa gốc, không tự ý bịa thêm field lạ.