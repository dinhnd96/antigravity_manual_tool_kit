# Hệ Thống Xếp Hạng Tester (Rating System)

> **Nguồn gốc**: uTest Academy - What is the tester rating system?
> **Ngày dịch**: 2026-05-17
> **Chủ đề**: platform

---

## Bản dịch

### Hệ thống xếp hạng là gì?

uTest đã xây dựng một **Hệ Thống Xếp Hạng** được thiết kế để thưởng cho tester dựa trên **hoạt động** và **chất lượng công việc** trong các test cycle. Là một tester được xếp hạng, bạn sẽ tích lũy điểm hoạt động (Activity Points) và điểm chất lượng (Quality Points), từ đó chuyển thành xếp hạng tester.

**Xếp hạng là một con số từ 0 đến 100**, cho biết vị trí của bạn so với các tester đang hoạt động khác trong Cộng đồng.

---

### 5 Hạng Tester (Rating Tiers)

| Hạng | Mô tả | Yêu cầu |
|------|-------|---------|
| ⬜ **Unrated** (Chưa xếp hạng) | Tester mới, chưa được đánh giá | Dưới 25 điểm hoạt động |
| 🟢 **Rated** (Đã xếp hạng) | Tester nằm trong top 0-49.99% | Ít nhất 25 điểm hoạt động |
| 🔵 **Proven** (Đã chứng minh) | Tester nằm trong top 50-74.99% | Vượt ngưỡng Rated |
| 🟤 **Bronze** (Đồng) | Tester nằm trong top 75-84.99% | Bonus +2.5% payout |
| ⚪ **Silver** (Bạc) | Tester nằm trong top 85-92.99% | Bonus +5% payout |
| 🥇 **Gold** (Vàng) | Top 7% tester được xếp hạng | Bonus +10% payout |

> 💡 Tất cả tester bắt đầu hành trình ở trạng thái **Unrated**. Sau khi tích đủ điểm hoạt động tối thiểu (thường sau **2-3 test cycle**), tester sẽ "tốt nghiệp" lên hạng **Rated** và bắt đầu có xếp hạng.

---

### Hành động TĂNG điểm ✅

| Hành động | Mô tả |
|-----------|-------|
| 🎯 **Tham gia (Participation)** | Chấp nhận lời mời test cycle và tham gia kiểm thử |
| 🚫 **Từ chối sớm (Declining Cycle)** | Từ chối lời mời sớm nếu không thể tham gia → nhường chỗ cho tester khác |
| 🐛 **Báo cáo lỗi (Issue Reports)** | Báo cáo lỗi được phê duyệt → tăng xếp hạng. Báo cáo **chất lượng cao và giá trị cao** → tăng **đáng kể** |
| 📋 **Test Case** | Test case được phê duyệt |
| 🔄 **Tái hiện lỗi (Reproductions)** | Cung cấp +1 tái hiện lỗi kèm tệp đính kèm |

### Hành động GIẢM điểm ❌

| Hành động | Mô tả |
|-----------|-------|
| 😶 **Không tham gia** | Chấp nhận lời mời nhưng **không tham gia** test cycle |
| 🚫 **Công việc bị từ chối** | Nộp bug report hoặc test case bị từ chối *(ngoại trừ bug bị từ chối vì "Working As Designed" - WAD không ảnh hưởng tiêu cực)* |
| ⚠️ **Chất lượng thấp** | Nhận đánh giá tính toàn vẹn thấp (low integrity) khi nộp báo cáo lỗi chất lượng kém |
| 📵 **Không phản hồi** | Không trả lời TTL hoặc TE trong test cycle |

---

### Cách tính xếp hạng

- Các hạng được **tính lại hàng đêm**
- Xếp hạng dựa trên điểm **Hoạt động** và **Chất lượng** trong một khoảng thời gian nhất định, **so sánh với tất cả tester khác**
- Do tính tương đối, hạng của bạn có thể **tăng, giảm, hoặc giữ nguyên** mà không có giải thích rõ ràng

> ℹ️ **Trường hợp đặc biệt**: Nếu xếp hạng kết thúc bằng `.2643%` (ví dụ: 49.2643%, 74.2643%, 84.2643%, 92.2643%), điều đó có nghĩa bạn có **điểm chất lượng đủ** để lên hạng cao hơn nhưng **chưa đạt đủ điểm hoạt động tối thiểu**.

---

### Tại sao nên nhắm đến xếp hạng cao?

#### 1. 💰 Tăng thu nhập (Payout Bonus)

| Hạng | Bonus trên mỗi báo cáo được duyệt |
|------|-------------------------------------|
| 🟤 Bronze | **+2.5%** |
| ⚪ Silver | **+5%** |
| 🥇 Gold | **+10%** |

#### 2. 📩 Nhiều lời mời hơn
Tester ở hạng cao hơn nhận được **nhiều lời mời** tham gia test cycle hơn.

---

### Xếp hạng riêng theo loại kiểm thử

Tester có **một xếp hạng riêng cho MỖI loại kiểm thử**. Ví dụ:
- 🥇 Gold cho **Functional Testing**
- 🔵 Proven cho **Usability Testing**

Bonus payout được tính theo xếp hạng **tương ứng với loại kiểm thử** của test cycle:

> **Ví dụ**: Nếu bạn là **Silver Functional** nhưng **Rated Usability**, bạn nhận +5% bonus cho bug Functional nhưng **không có bonus** cho bug Usability.

---

### Xem thống kê xếp hạng

Vào phần **Statistics** trên Hồ sơ Tester để xem:
- Xếp hạng hiện tại
- Lịch sử hoạt động
- Trạng thái xếp hạng

---

## Thuật ngữ quan trọng

| English | Tiếng Việt | Ghi chú |
|---------|-----------|---------|
| Rating System | Hệ thống xếp hạng | Cơ chế đánh giá tester |
| Activity Points | Điểm hoạt động | Tích lũy qua tham gia cycle |
| Quality Points | Điểm chất lượng | Tích lũy qua chất lượng công việc |
| Unrated | Chưa xếp hạng | Trạng thái ban đầu |
| Rated | Đã xếp hạng | Hạng cơ bản, top 0-49.99% |
| Proven | Đã chứng minh | Top 50-74.99% |
| Bronze | Đồng | Top 75-84.99%, +2.5% bonus |
| Silver | Bạc | Top 85-92.99%, +5% bonus |
| Gold | Vàng | Top 7%, +10% bonus |
| Working As Designed (WAD) | Hoạt động đúng thiết kế | Bug bị reject vì WAD không bị trừ điểm |
| Reproduction | Tái hiện (lỗi) | Xác nhận bug của tester khác |
| Low Integrity Rating | Đánh giá tính toàn vẹn thấp | Khi nộp báo cáo chất lượng kém |
