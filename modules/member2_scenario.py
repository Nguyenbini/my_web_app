"""Thành viên 2 - Mô phỏng kịch bản (VD: lạm phát 4%)."""
import pandas as pd
import streamlit as st


def simulate(monthly: float, rate: float, inflation: float, years: int) -> pd.DataFrame:
    """Tiết kiệm đều mỗi tháng (triệu đồng), lãi kép theo tháng.
    Trả về bảng giá trị danh nghĩa và giá trị thực (đã trừ lạm phát) theo từng năm."""
    r_m = rate / 100 / 12
    rows, balance = [], 0.0
    for month in range(1, years * 12 + 1):
        balance = balance * (1 + r_m) + monthly
        if month % 12 == 0:
            y = month // 12
            real = balance / (1 + inflation / 100) ** y
            rows.append({"Năm": y, "Danh nghĩa (triệu)": round(balance, 1),
                         "Giá trị thực (triệu)": round(real, 1)})
    return pd.DataFrame(rows)


def render():
    st.header("Mô phỏng kịch bản")
    c1, c2 = st.columns(2)
    monthly = c1.number_input("Tiết kiệm mỗi tháng (triệu đồng)", 0.0, 1000.0, 5.0, 0.5)
    years = c1.slider("Số năm", 1, 40, 10)
    rate = c2.slider("Lợi nhuận kỳ vọng (%/năm)", 0.0, 15.0, 6.0, 0.5)
    inflation = c2.slider("Lạm phát (%/năm)", 0.0, 10.0, 4.0, 0.5)

    df = simulate(monthly, rate, inflation, years)
    st.line_chart(df.set_index("Năm"))
    st.dataframe(df, use_container_width=True, hide_index=True)

    last = df.iloc[-1]
    st.session_state.scenario_results = {
        "so_nam": years, "lam_phat": inflation, "loi_nhuan": rate,
        "danh_nghia_trieu": float(last["Danh nghĩa (triệu)"]),
        "gia_tri_thuc_trieu": float(last["Giá trị thực (triệu)"]),
    }
    st.caption("Kết quả là mô phỏng theo giả định, không phải dự báo hay cam kết.")
