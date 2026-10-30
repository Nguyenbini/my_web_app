"""
main.py - File chạy chính của ứng dụng (giao diện tổng).
Chạy:  streamlit run main.py
"""
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from modules import member1_chatbot, member2_scenario, member3_data

BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / ".env")

st.set_page_config(page_title="Trợ lý tài chính", page_icon="💰", layout="wide")

# CSS dùng chung
css_path = BASE_DIR / "assets" / "style.css"
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

# Thanh bên
logo_path = BASE_DIR / "assets" / "logo.png"
if logo_path.exists():
    st.sidebar.image(str(logo_path), width=120)
st.sidebar.title("Trợ lý tài chính")
page = st.sidebar.radio("Chọn chức năng", ["Chatbot", "Mô phỏng kịch bản", "Dữ liệu"])

if not os.getenv("GEMINI_API_KEY"):
    st.sidebar.warning("Chưa có GEMINI_API_KEY trong file .env — chatbot sẽ không hoạt động.")

if page == "Chatbot":
    member1_chatbot.render()
elif page == "Mô phỏng kịch bản":
    member2_scenario.render()
else:
    member3_data.render()
