import streamlit as st
import numpy as np
import pandas as pd
import random

st.set_page_config(page_title="💧AquaFlow Full", page_icon="💧", layout="wide")

# ========================================
# HALAMAN UTAMA - MENU
# ========================================
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Mulai Simulasi", "📊 Simulasi", "🧠 Kuis", "📈 Data"])

with tab1:
    st.header("🎮 **Selamat Datang di AquaFlow!**")
    st.markdown("""
    **Pilih simulasi pemakaian air harian:**
    1. 🚿 **Mandi** - Shower/Keran/Ember
    2. 🧼 **Cuci tangan/piring**  
    3. 👕 **Cuci baju**
    4. 🌱 **Siram tanaman**
    
    **Klik "Simulasi" untuk mulai!**
    """)
    
    if st.button("🚀 **START SIMULASI**", type="primary"):
        st.session_state['simulasi_active'] = True
        st.success("✅ Simulasi dimulai!")
        st.rerun()

with tab2:
    # SIMULASI MANDI
    st.header("🚿 **Simulasi Mandi**")
    
    # INPUT
    col1, col2 = st.columns(2)
    waktu = col1.slider("⏱️ Waktu mandi (menit)", 1, 30, 10)
    jenis = col2.selectbox("💧 Jenis", ["Shower (10L/m)", "Keran (6L/m)", "Ember (20L)"])
    frekuensi = st.slider("🔄 Kali/hari", 1, 4, 2)
    
    # DEBIT
    debit = {"Shower": 10, "Keran": 6, "Ember": 20}
    air_per_mandi = debit["Ember"] if "Ember" in jenis else debit[jenis.split()[0]] * waktu
    total_harian = air_per_mandi * frekuensi
    
    # HASIL
    col1, col2 = st.columns(2)
    col1.metric("💦 Per mandi", f"{air_per_mandi:.0f} L")
    col2.metric("📅 Harian", f"{total_harian:.0f} L")
    
    # GRAFIK
    st.subheader("📊 Visualisasi")
    df = pd.DataFrame({
        "Jenis": ["Shower", "Keran", "Ember", "Anda"],
        "Liter": [10*waktu*frekuensi, 6*waktu*frekuensi, 20*frekuensi, total_harian]
    })
    st.bar_chart(df.set_index("Jenis"))

with tab3:
    # KUIS INTERAKTIF
    st.header("🧠 **Kuis Debit Air**")
    
    if 'score' not in st.session_state:
        st.session_state.score = 0
        st.session_state.answered = []
    
    # SOAL KUIS
    soal = [
        {"q": "Shower 10 menit, debit 10L/menit = ?", "a": [100, 10, 1], "jawab": 100},
        {"q": "Keran 5 menit, 6L/menit, 3x/hari = ?", "a": [90, 30, 900], "jawab": 90},
        {"q":
