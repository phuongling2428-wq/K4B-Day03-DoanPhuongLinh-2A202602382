# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** [Đoàn Phương Linh]  
> **Mã Sinh Viên / Mã Học viên:** [2A202602382]  
> **Chủ đề Lựa chọn:** [Trợ lý Học vụ VinUni: Tra cứu thông tin sinh viên và đặt lịch tư vấn với cố vấn học tập]  

---

> **Chủ đề Lựa chọn:** [Trợ lý Học vụ VinUni: Tra cứu thông tin sinh viên và đặt lịch tư vấn với cố vấn học tập]

---
## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)
| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Bài toán yêu cầu chia nhỏ nhiều bước suy luận tiếp nhau từ kiểm tra thông tin sinh viên, đối chiếu điều kiện cho đến tìm lịch trống của cố vấn. |
| **2. Tool Interaction** | 5 / 5 | Hệ thống bắt buộc phải kết nối với cơ sở dữ liệu sinh viên VinUni và API lịch làm việc (Google Calendar/Outlook) của cố vấn để tra cứu và đặt lịch. |
| **3. Dynamic Decision** | 4 / 5 | Bước tiếp theo phụ thuộc vào kết quả quan sát trước đó. Nếu lịch cố vấn bị trùng hoặc sinh viên không đủ điều kiện, hệ thống phải tự động chuyển hướng xử lý khác. |
| **4. Long Horizon Goal** | 4 / 5 | Hệ thống phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý, dẫn dắt sinh viên hoàn thành việc đặt lịch ngay cả khi cuộc hội thoại bị ngắt quãng hoặc kéo dài. |
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "gpa": 3.85
      }
    },
    "latency_ms": 120.5
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** ___ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** ___ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
