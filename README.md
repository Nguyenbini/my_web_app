# my_web_app

Ứng dụng trợ lý tài chính của nhóm (Streamlit + Gemini).

## Chạy thử
```bash
pip install -r requirements.txt
cp .env.example .env      # rồi điền GEMINI_API_KEY
streamlit run main.py
```

## Phân công
- `modules/member1_chatbot.py` — Thành viên 1: Chatbot LLM
- `modules/member2_scenario.py` — Thành viên 2: Mô phỏng kịch bản
- `modules/member3_data.py` — Thành viên 3: Xử lý dữ liệu
- `prompts/` — prompt gốc của cả nhóm
- `assets/` — CSS, logo dùng chung

> File `.env` đã nằm trong `.gitignore`, không bị đẩy lên GitHub.
