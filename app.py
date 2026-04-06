import streamlit as st

st.set_page_config(page_title="AquaFlow", page_icon="💧", layout="wide")

# Halaman state
if 'halaman' not in st.session_state:
    st.session_state.halaman = 'start'

# ========================================
# HALAMAN AWAL - TAMPILAN LUCU
# ========================================
if st.session_state.halaman == 'start':
    st.markdown("""
    <style>
    .big-title {font-size: 5rem !important; color: #ff6b6b; text-align: center;}
    .cute-text {font-size: 2rem !important; color: #4ecdc4; text-align: center;}
    .start-btn {font-size: 2rem !important; padding: 1.5rem !important;}
    </style>
    """, unsafe_allow_html=True)
    
    # Tampilan lucu
    st.markdown('<h1 class="big-title">💦✨ AquaFlow ✨💦</h1>', unsafe_allow_html=True)
    st.markdown('<p class="cute-text">Simulasi Interaktif Fisika SMA 🛁🚿</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("🚀 **START** 🚀", use_container_width=True, key="start_btn"):
            st.session_state.halaman = 'main'
            st.rerun()
    
    # Emoji decoration
    st.markdown("🌊💧🛁🚿💦🌊")

# ========================================
# HALAMAN UTAMA - 4 TAB
# ========================================
elif st.session_state.halaman == 'main':
    # Header
    st.markdown("### 💧 **Dashboard AquaFlow** 💧")
    col1, col2 = st.columns([1,10])
    with col1:
        if st.button("🏠", key="back"):
            st.session_state.halaman = 'start'
            st.rerun()
    
    st.markdown("---")
    
    # 4 TABS
    tab1, tab2, tab3, tab4 = st.tabs(["🚿 Simulasi", "🧮 Kalkulator", "🧠 Kuis", "📈 Data"])
    
    # TAB 1: SIMULASI MANDI
    with tab1:
        st.header("🚿 **Simulasi Mandi**")
        
        # INPUT EXACT
        st.markdown("### **Waktu mandi (menit)**")
        waktu_mandi = st.slider("", 1, 30, 10)
        
        st.markdown("### **Jenis air:**")
        jenis_air = st.radio("", ["Shower 🚿 (≈ 10 liter/menit)", "Keran 🚰 (≈ 6 liter/menit)"])
        
        st.markdown("### **Frekuensi per hari (berapa kali mandi)**")
        frekuensi = st.slider("", 1, 4, 2)
        
        # HITUNG
        debit = 10 if "Shower" in jenis_air else 6
        air_per_mandi = debit * waktu_mandi
        total_harian = air_per_mandi * frekuensi
        
        # HASIL
        col1, col2 = st.columns(2)
        col1.metric("💦 Per mandi", f"{air_per_mandi:.0f} L")
        col2.metric("📅 Harian", f"{total_harian:.0f} L")
        
        # GRAFIK (TANPA "Anda")
        st.markdown("### **📊 Perbandingan Air**")
        st.bar_chart({
            "Shower 🚿": 10*waktu_mandi*frekuensi,
            "Keran 🚰": 6*waktu_mandi*frekuensi
        })
    
    # TAB 2: KALKULATOR
    with tab2:
        st.header("🧮 **Kalkulator Q = A × v**")
        col1, col2 = st.columns(2)
        diameter = col1.number_input("📏 Diameter (cm)", 0.5, 5.0, 2.0)
        kecepatan = col2.number_input("🏃 Kecepatan (m/s)", 0.1, 3.0, 1.0)
        
        r = diameter / 200
        A = 3.14 * r * r
        Q = A * kecepatan
        
        col1.metric("📐 A", f"{A:.5f} m²")
        col2.metric("💧 Q", f"{Q:.5f} m³/s")
    
    # TAB 3: KUIS 5 SOAL
    with tab3:
        st.header("🧠 **Kuis Fisika (5 Soal)**")
        
        # Soal 1
        st.markdown("**1. Shower 10 menit (10 L/menit) = ?**")
        jawab1 = st.radio("", ["10 L", "100 L", "1 L"], key="s1")
        if st.button("Cek 1", key="c1"):
            st.write("✅" if jawab1 == "100 L" else "❌")
        
        # Soal 2
        st.markdown("**2. Rumus debit?**")
        jawab2 = st.radio("", ["Q=A+v", "Q=A×v", "Q=A/v"], key="s2")
        if st.button("Cek 2", key="c2"):
            st.write("✅" if jawab2 == "Q=A×v" else "❌")
        
        # Soal 3
        st.markdown("**3. Diameter 2cm, v=1m/s, A ≈ ?**")
        jawab3 = st.radio("", ["0.0003 m²", "0.03 m²", "3 m²"], key="s3")
        if st.button("Cek 3", key="c3"):
            st.write("✅" if jawab3 == "0.0003 m²" else "❌")
        
        # Soal 4
        st.markdown("**4. Mandi 2x (8L/menit × 10 menit) = ?**")
        jawab4 = st.radio("", ["16 L", "160 L", "80 L"], key="s4")
        if st.button("Cek 4", key="c4"):
            st.write("✅" if jawab4 == "160 L" else "❌")
        
        # Soal 5
        st.markdown("**5. Unit debit Q = ?**")
        jawab5 = st.radio("", ["m/s", "m²", "m³/s"], key="s5")
        if st.button("Cek 5", key="c5"):
            st.write("✅" if jawab5 == "m³/s" else "❌")
    
    # TAB 4: DATA
    with tab4:
        st.header("📈 **Data Standar**")
        data = {
            "Kegiatan": ["Mandi", "Cuci tangan", "Cuci piring"],
            "Rata-rata": [80, 5, 15],
            "Hemat": [50, 2, 8]
        }
        st.table(data)

st.markdown("---")
st.caption("💧 AquaFlow - Simulasi Interaktif Fisika SMA")
