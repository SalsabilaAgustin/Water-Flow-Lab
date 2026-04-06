import streamlit as st
import numpy as np

st.set_page_config(page_title="💧AquaFlow", page_icon="💧", layout="wide")

st.title("💧 **AquaFlow - Kalkulator Debit Air**")
st.markdown("*Fisika Kelas 11 - Q = A × v*")

# Input
col1, col2 = st.columns(2)
diameter = col1.number_input("📏 Diameter (cm)", 0.1, 10.0, 2.0)
kecepatan = col2.number_input("🏃 Kecepatan (m/s)", 0.1, 5.0, 1.0)
waktu = st.slider("⏰ Waktu (jam)", 0.0, 24.0, 2.0)

# HITUNG
r = diameter / 200
A = 3.1416 * (r ** 2)
Q = A * kecepatan
volume = Q * waktu * 3600 * 1000

# HASIL
st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("📐 Luas (A)", f"{A:.5f} m²")
col2.metric("💧 DEBIT (Q)", f"{Q:.5f} m³/s")
col3.metric("🚰 Volume", f"{volume:.0f} L")

# GRAFIK
st.subheader("📈 Pengaruh Diameter")
diameter_list = np.array([0.5, 1, 2, 3, 4])
Q_list = 3.1416 * (diameter_list/200)**2 * kecepatan * 1000

df = {"Diameter": diameter_list, "Debit (ml/s)": Q_list}
st.bar_chart(df)

# RUMUS
st.markdown("### 🔬 **Rumus Debit**")
st.latex("Q = A \\times v")
st.info("Q = Debit, A = Luas, v = Kecepatan")
st.balloons()
