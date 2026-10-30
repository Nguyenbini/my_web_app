"""Thành viên 1 - Chatbot LLM (Gemini)."""
import os

import streamlit as st

from modules import load_prompt


def ask_llm(question: str, profile: dict, results: dict) -> str:
    import google.generativeai as genai

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key.startswith("dien_"):
        return "Chưa cấu hình GEMINI_API_KEY trong file .env."
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))
    prompt = load_prompt("chatbot_prompt.txt").format(
        profile=profile, results=results, question=question
    )
    return model.generate_content(prompt).text


def render():
    st.header("Chatbot tư vấn")
    if "history" not in st.session_state:
        st.session_state.history = []

    for role, msg in st.session_state.history:
        st.chat_message(role).write(msg)

    question = st.chat_input("Hỏi về kế hoạch tài chính của bạn...")
    if question:
        st.chat_message("user").write(question)
        profile = st.session_state.get("profile", {})
        results = st.session_state.get("scenario_results", {})
        with st.spinner("Đang trả lời..."):
            answer = ask_llm(question, profile, results)
        st.chat_message("assistant").write(answer)
        st.session_state.history += [("user", question), ("assistant", answer)]
