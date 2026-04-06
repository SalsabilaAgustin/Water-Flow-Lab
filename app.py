import streamlit as st

# KONFIGURASI
st.set_page_config(page_title="AquaFlow", page_icon="💧", layout="wide")

# STATE UNTUK HALAMAN
if 'page' not in st.session_state:
    st.session_state.page = "start"

# ========================================
# HALAMAN START
# ========================================
if st.session_state.page == "start":
    st.markdown("""
    <style>
    .main-header {font-size: 4rem; color: #1f77b4; text-align: center;}
    .start-btn {font-size: 2rem; padding: 1rem;}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-header">💧 AquaFlow</h1>', unsafe_allow_html=True)
    st.markdown("### *Simulasi Debit Air Harian Siswa*")
    
    st.markdown("---")
    st.write("""
    **Fitur:**
    - 📊 **Simulasi** pemakaian air mandi
    - 🧮 **Kalkulator** debit Q = A × v  
    - 🧠 **Kuis** interaktif
    - 📈 **Data** standar siswa
    """)
    
    col1, col2 = st.columns([1,3])
    with col1:
        if st.button("🚀 **MULAI SIMULASI**", key="start", help="Klik untuk masuk"):
            st.session_state.page = "main"
            st.rerun()
    
    st.markdown("---")
    st.caption("Fisika Kelas 11 - Debit Fluida")

# ========================================
# HALAMAN UTAMA (SETELAH START)
# ========================================
elif st.session_state.page == "main":
    # HEADER + BACK BUTTON
    st.markdown("## 💧 **Dashboard AquaFlow**")
    col1, col2, col3 = st.columns([1,3,1])
    with col1:
        if st.button("🏠 Kembali", key="back"):
            st.session_state.page = "start"
            st.rerun()
    
    # TABS
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Simulasi", "🧮 Kalkulator", "🧠 Kuis", "📈 Data"])
    
    with tab1:
        st.header("🚿 **Simulasi Mandi**")
        waktu = st.slider("⏰ Waktu (menit)", 1, 30, 10)
        jenis = st.selectbox("💧 Jenis", ["Shower 10L/menit", "Keran 6L/menit", "Ember 20L"])
        kali = st.slider("🔄 Per hari", 1, 4, 2)
        
        # Hitung
        if "Shower" in jenis:
            debit = 10 * waktu
        elif "Keran" in jenis:
            debit = 6 * waktu
        else:
            debit = 20
        
        total = debit * kali
        
        st.metric("💦 Per mandi", f"{debit} L")
        st.metric("📅 Harian", f"{total} L")
        
        st.bar_chart({"Shower":100, "Keran":60, "Ember":20, "Anda":total})
    
    with tab2:
        st.header("🧮 **Kalkulator Debit Q = A × v**")
        col1, col2 = st.columns(2)
        diameter = col1.number_input("📏 Diameter (cm)", 0.5, 5.0, 2.0)
        kecepatan = col2.number_input("🏃 Kecepatan (m/s)", 0.1, 3.0, 1.0)
        
        # Hitung
        r = diameter / 200  # cm to m
        A = 3.14 * r * r
        Q = A * kecepatan
        
        st.latex(r"Q = A \times v = \pi r^2 \times v")
        st.metric("📐 Luas A", f"{A:.5f} m²")
        st.metric("💧 Debit Q", f"{Q:.5f} m³/s")
    
    with tab3:
        st.header("🧠 **Kuis Interaktif**")
        
        # Kuis 1
        st.write("**Q1:** Shower 10 menit (10L/menit) = ?")
        jawab1 = st.radio(":", ["10L", "100L", "1L"])
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Cek") and jawab1 == "100L":
                st.success("Benar! +10 poin")
            elif st.button("✅ Cek"):
                st.error("Salah!")
        
        # Kuis 2
        st.write("**Q2:** Rumus debit yang benar?")  
        jawab2 = st.radio(":", ["Q = A + v", "Q = A × v", "Q = A / v"], key="q2")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Cek 2") and jawab2 == "Q = A × v":
                st.success("Benar!")
            elif st.button("✅ Cek 2"):
                st.error("Salah!")
    
    with tab4:
        st.header("📈 **Data Standar**")
        data = {
            "Aktivitas": ["Mandi", "Cuci tangan", "Cuci piring", "Cuci baju"],
            "Normal (L/hari)": [80, 5, 15, 50],
            "Hemat (L/hari)": [50, 2, 8, 30]
        }
        st.table(data)
