# Git Rules

## Quy tắc thực thi Git (Mandatory)

1. **CẤM** tự động thực hiện lệnh `git push` mà chưa có sự đồng ý rõ ràng từ USER.
2. Trước khi thực hiện bất kỳ lệnh `git push` nào, AI phải:
   - Liệt kê danh sách các file đã thay đổi (git status).
   - Giải thích ngắn gọn nội dung commit.
   - Chờ USER phản hồi "Đồng ý" hoặc "Push đi" mới được thực thi.
3. Các lệnh `git commit`, `git add` có thể thực hiện để chuẩn bị, nhưng bước `push` là bước bắt buộc phải có sự xác nhận.
