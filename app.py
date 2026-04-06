import streamlit as st

st.set_page_config(page_title="AquaFlow Full", page_icon="💧", layout="wide")

# STATE HALAMAN
if 'page' not in st.session_state:
    st.session_state.page = "start"

# ========================================
# HALAMAN 1: START PAGE
# ========================================
if st.session_state.page == "start":
    st.markdown("""
    <style>
    .main-title {font-size: 4rem; color: #1f77b4; text-align: center; margin-bottom: 2rem;}
    .start-btn {font-size: 1.5rem; padding: 1rem 2rem; height: 3rem;}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-title">💧 AquaFlow</h1>', unsafe_allow_html=True)
    st.markdown("### *Simulasi & Edukasi Debit Air Harian*")
    
    st.markdown("---")
    st.write("""
    **✨ Fitur Lengkap:**
    - 🚿 **Simulasi Mandi** (Shower/Keran)
    - 🧮 **Kalkulator** Q = A × v  
    - 🧠 **Kuis** interaktif
    - 📈 **Data** standar siswa
    """)
    
    col1, col2 = st.columns([1,3])
    with col1:
        if st.button("🚀 **MASUK SIMULASI**", key="start", help="Klik untuk mulai", use_container_width=True):
            st.session_state.page = "main"
            st.rerun()
    
    st.markdown("---")
    st.caption("👨‍🎓 Dibuat untuk siswa Fisika Kelas 11")

# ========================================
# HALAMAN 2: DASHBOARD UTAMA
# ========================================
elif st.session_state.page == "main":
    # HEADER + BACK
    st.markdown("### 💧 **Dashboard AquaFlow**")
    col1, col2, col3 = st.columns([1,4,1])
    with col1:
        if st.button("🏠 Kembali", key="back", use_container_width=True):
            st.session_state.page = "start"
            st.rerun()
    
    st.markdown("---")
    
    # 4 TABS
    tab1, tab2, tab3, tab4 = st.tabs(["🚿 Simulasi Mandi", "🧮 Kalkulator", "🧠 Kuis", "📈 Data"])
    
    # TAB 1: SIMULASI MANDI (SESUAI PERMINTAAN)
    with tab1:
        st.header("⏰ **Waktu mandi (menit)**")
        waktu_mandi = st.slider("⏰ Waktu mandi", 1, 30, 10, 1)
        
        st.header("💧 **Jenis air:**")
        jenis_air = st.radio(
            "Pilih:", 
            ["Shower 🚿 (≈ 10 liter/menit)", "Keran 🚰 (≈ 6 liter/menit)"]
        )
        
        st.header("🔄 **Frekuensi per hari**")
        frekuensi = st.slider("Berapa kali mandi", 1, 4, 2, 1)
        
        # HITUNG
        debit = 10 if "Shower" in jenis_air else 6
        air_per_mandi = debit * waktu_mandi
        total_harian = air_per_mandi * frekuensi
        
        # HASIL
        st.markdown("---")
        col1, col2 = st.columns(2)
        col1.metric("💦 Per mandi", f"{air_per_mandi:.0f} Liter")
        col2.metric("📅 Harian", f"{total_harian:.0f} Liter")
        
        # GRAFIK
        st.subheader("📊 Perbandingan")
        st.bar_chart({
            "Shower (10L/m)": 10*waktu_mandi*frekuensi,
            "Keran (6L/m)": 6*waktu_mandi*frekuensi, 
            "Anda": total_harian
        })
    
    # TAB 2: KALKULATOR
    with tab2:
        st.header("🧮 **Kalkulator Debit Q = A × v**")
        col1, col2 = st.columns(2)
        diameter = col1.number_input("📏 Diameter (cm)", 0.5, 5.0, 2.0)
        kecepatan = col2.number_input("🏃 Kecepatan (m/s)", 0.1, 3.0, 1.0)
        
        r = diameter / 200
        A = 3.14 * r * r
        Q = A * kecepatan
        
        st.latex(r"Q = \pi r^2 \times v")
        col1, col2, col3 = st.columns(3)
        col1.metric("📐 A (m²)", f"{A:.5f}")
        col2.metric("💧 Q (m³/s)", f"{Q:.5f}")
        col3.metric("🏃 v (m/s)", f"{kecepatan}")
    
    # TAB 3: KUIS
    with tab3:
        st.header("🧠 **Kuis Cepat**")
        
        st.write("**Q1:** Shower 10 menit (10L/menit) = ?")
        jawab1 = st.radio("Pilih:", ["10L", "100L", "1L"])
        if st.button("✅ Jawab Q1") and jawab1 == "100L":
            st.success("🎉 Benar!")
        elif st.button("✅ Jawab Q1"):
            st.error("❌ Jawaban: 100L")
        
        st.write("**Q2:** Rumus debit?")
        jawab2 = st.radio("Pilih:", ["Q=A+v", "Q=A×v", "Q=A/v"], key="q2")
        if st.button("✅ Jawab Q2") and jawab2 == "Q=A×v":
            st.success("🎉 Benar!")
        elif st.button("✅ Jawab Q2"):
            st.error("❌ Jawaban: Q=A×v")
    
    # TAB 4: DATA
    with tab4:
        st.header("📈 **Data Standar Siswa**")
        data = {
            "Aktivitas": ["Mandi Shower", "Mandi Keran", "Cuci Tangan", "Cuci Piring"],
            "Rata-rata (L/hari)": [120, 80, 5, 15],
            "Hemat (L/hari)": [60, 40, 2, 8]
        }
        st.table(data)

# FOOTER
st.markdown("---")
st.caption("💧 AquaFlow - Full Simulasi | Fisika Kelas 11")
