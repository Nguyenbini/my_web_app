"""Thành viên 3 - Xử lý dữ liệu."""
import pandas as pd
import streamlit as st


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Làm sạch cơ bản: bỏ dòng trống, chuẩn hóa tên cột, bỏ trùng."""
    df = df.dropna(how="all").copy()
    df.columns = [str(c).strip() for c in df.columns]
    return df.drop_duplicates()


def render():
    st.header("Xử lý dữ liệu")
    file = st.file_uploader("Tải lên file CSV hoặc Excel", type=["csv", "xlsx"])
    if not file:
        st.info("Tải một file lên để xem và làm sạch dữ liệu.")
        return
    df = pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)
    df = clean(df)
    st.write(f"{len(df)} dòng, {len(df.columns)} cột sau khi làm sạch")
    st.dataframe(df, use_container_width=True)
    st.subheader("Thống kê mô tả")
    st.dataframe(df.describe(include="all").T, use_container_width=True)
    st.session_state.data = df
