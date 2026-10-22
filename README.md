# StuDocu Free Viewer & Downloader

Một công cụ siêu nhẹ (Userscript) giúp bạn xem và tải tài liệu trên StuDocu hoàn toàn miễn phí. Không cần tài khoản Pro, không bắt buộc upload tài liệu đóng góp, không cần chạy dòng lệnh phức tạp.

**Tính năng chính**
- Tự động gỡ bỏ lớp phủ mờ (unblur) trên các trang tài liệu.
- Tự động tắt các popup yêu cầu nâng cấp Premium.
- Hỗ trợ xem toàn bộ trang và lưu dưới dạng PDF.

**Hướng dẫn cài đặt**
1. Cài đặt tiện ích mở rộng **Tampermonkey** cho trình duyệt (Chrome, Edge, Cốc Cốc, Firefox).
2. Bấm vào biểu tượng tiện ích Tampermonkey trên thanh công cụ, chọn **Create a new script...** (Tạo script mới).
3. Copy toàn bộ đoạn mã JavaScript từ file `studocu-unblur.js` trong kho lưu trữ này và dán đè lên nội dung mặc định.
4. Bấm `Ctrl + S` (hoặc `Cmd + S` trên Mac) để lưu lại.

**Cách sử dụng**
1. Mở một đường link tài liệu StuDocu bất kỳ. Kịch bản sẽ tự động dọn dẹp các lớp chắn sau khoảng 1-2 giây.
2. Lăn chuột từ từ từ trên xuống dưới cùng để trình duyệt tải toàn bộ hình ảnh văn bản sắc nét nhất.
3. Bấm tổ hợp phím `Ctrl + P` (hoặc click chuột phải chọn **Print**).
4. Ở mục Máy in (Destination), chọn **Save as PDF** (Lưu dưới dạng PDF) và bấm Lưu.