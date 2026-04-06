import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="💧AquaFlow", page_icon="💧", layout="wide")

# MENU TAB
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Start", "📊 Simulasi", "🧠 Kuis", "📈 Data"])

with tab1:
    st.header("🎮 AquaFlow - Simulasi Air")
    st.write("**Pilih tab Simulasi untuk mulai!**")
    if st.button("🚀 MULAI", type="primary"):
        st.success("✅ Siap simulasi!")

with tab2:
    st.header("🚿 Simulasi Mandi")
    
    # INPUT SIMPEL
    waktu = st.slider("⏰ Waktu mandi (menit)", 1, 30, 10)
    jenis = st.selectbox("💧 Jenis", ["Shower 10L/m", "Keran 6L/m", "Ember 20L"])
    frekuensi = st.slider("🔄 Kali/hari", 1, 4, 2)
    
    # HITUNG
    if "Shower" in jenis:
        debit = 10
    elif "Keran" in jenis:
        debit = 6
    else:
        debit = 20
    
    air_mandi = debit * waktu if "Ember" not in jenis else debit
    total = air_mandi * frekuensi
    
    # HASIL
    col1, col2 = st.columns(2)
    col1.metric("💦 Per mandi", f"{air_mandi} L")
    col2.metric("📅 Harian", f"{total} L")
    
    # GRAFIK
    st.bar_chart({"Shower": 10*waktu*frekuensi, "Keran": 6*waktu*frekuensi, "Ember": 20*frekuensi, "Anda": total})

with tab3:
    st.header("🧠 Kuis Sederhana")
    
    # SOAL 1
    st.write("**Q1:** Shower 10 menit = ?")
    jawab1 = st.radio("Pilih:", ["100L", "10L", "1L"])
    if st.button("Cek Q1") and jawab1 == "100L":
        st.success("✅ Benar!")
    elif st.button("Cek Q1"):
        st.error("❌ Salah!")
    
    # SOAL 2  
    st.write("**Q2:** Debit = ?")
    jawab2 = st.radio("Pilih:", ["A×v", "A+v", "A/v"], key="q2")
    if st.button("Cek Q2", key="b2") and jawab2 == "A×v":
        st.success("✅ Benar!")
    elif st.button("Cek Q2", key="b2"):
        st.error("❌ Salah!")

with tab4:
    st.header("📈 Data Standar")
    
    data = {
        "Aktivitas": ["Mandi", "Cuci tangan", "Cuci piring"],
        "Rata-rata": [80, 5, 15]
    }
    st.dataframe(data)

st.markdown("---")
st.caption("💧 AquaFlow v2.0 - No Error!")
