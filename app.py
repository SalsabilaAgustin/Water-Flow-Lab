import streamlit as st

st.set_page_config(page_title="AquaFlow", page_icon="💧", layout="wide")

# Halaman state
if 'halaman' not in st.session_state:
    st.session_state.halaman = 'start'

# ========================================
# HALAMAN AWAL - START PAGE
# ========================================
if st.session_state.halaman == 'start':
    # Judul besar
    st.markdown("# **Simulasi Interaktif Fisika SMA**")
    st.markdown("### 💧 *AquaFlow - Debit Air Harian*")
    
    st.markdown("---")
    
    # Deskripsi singkat
    st.write("""
    **Fitur aplikasi:**
    - 🚿 Simulasi mandi
    - 🧮 Kalkulator debit
    - 🧠 Kuis fisika
    - 📈 Data standar
    """)
    
    # Tombol START BESAR
    st.markdown("---")
    if st.button("**🚀 START SIMULASI**", use_container_width=True):
        st.session_state.halaman = 'main'
        st.rerun()

# ========================================
# HALAMAN UTAMA - 4 TAB
# ========================================
elif st.session_state.halaman == 'main':
    # Header dengan tombol kembali
    st.markdown("## 💧 **Dashboard Simulasi**")
    
    col1, col2 = st.columns([1, 10])
    with col1:
        if st.button("🏠 Kembali"):
            st.session_state.halaman = 'start'
            st.rerun()
    
    st.markdown("---")
    
    # 4 TAB
    tab1, tab2, tab3, tab4 = st.tabs(["🚿 Simulasi", "🧮 Kalkulator", "🧠 Kuis", "📈 Data"])
    
    # TAB 1: SIMULASI MANDI (EXACT PERMINTAAN)
    with tab1:
        st.header("**🚿 Simulasi Mandi**")
        
        # INPUT 1: Waktu mandi
        st.markdown("### **Waktu mandi (menit)**")
        waktu_mandi = st.slider("", min_value=1, max_value=30, value=10)
        
        # INPUT 2: Jenis air
        st.markdown("### **Jenis air:**")
        jenis_air = st.radio(
            "",
            ["Shower 🚿 (≈ 10 liter/menit)", "Keran 🚰 (≈ 6 liter/menit)"]
        )
        
        # INPUT 3: Frekuensi
        st.markdown("### **Frekuensi per hari (berapa kali mandi)**")
        frekuensi = st.slider("", min_value=1, max_value=4, value=2)
        
        st.markdown("---")
        
        # PERHITUNGAN
        debit = 10 if "Shower" in jenis_air else 6
        air_per_mandi = debit * waktu_mandi
        total_harian = air_per_mandi * frekuensi
        
        # HASIL
        col1, col2 = st.columns(2)
        col1.metric("💦 Air per mandi", f"{air_per_mandi:.0f} L")
        col2.metric("📅 Total harian", f"{total_harian:.0f} L")
        
        # GRAFIK
        st.markdown("### **📊 Grafik Perbandingan**")
        st.bar_chart({
            "Shower": 10*waktu_mandi*frekuensi,
            "Keran": 6*waktu_mandi*frekuensi,
            "Anda": total_harian
        })
    
    # TAB 2: KALKULATOR
    with tab2:
        st.header("**🧮 Kalkulator Debit Q = A × v**")
        col1, col2 = st.columns(2)
        diameter = col1.number_input("Diameter pipa (cm)", 0.5, 5.0, 2.0)
        kecepatan = col2.number_input("Kecepatan aliran (m/s)", 0.1, 3.0, 1.0)
        
        r = diameter / 200  # cm ke m
        A = 3.14 * r * r
        Q = A * kecepatan
        
        st.write("**Rumus:** Q = πr² × v")
        col1.metric("Luas A", f"{A:.5f} m²")
        col2.metric("Debit Q", f"{Q:.5f} m³/s")
    
    # TAB 3: KUIS
    with tab3:
        st.header("**🧠 Kuis Fisika**")
        
        # Soal 1
        st.markdown("**Q1:** Shower 10 menit (10 L/menit) = ?")
        jawab1 = st.radio("Pilih jawaban:", ["10 L", "100 L", "1 L"])
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Cek Jawaban 1"):
                if jawab1 == "100 L":
                    st.success("✅ Benar!")
                else:
                    st.error("❌ Jawaban benar: 100 L")
        
        # Soal 2
        st.markdown("**Q2:** Rumus debit yang benar?")
        jawab2 = st.radio("Pilih jawaban:", ["Q = A + v", "Q = A × v", "Q = A / v"], key="q2")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Cek Jawaban 2"):
                if jawab2 == "Q = A × v":
                    st.success("✅ Benar!")
                else:
                    st.error("❌ Jawaban benar: Q = A × v")
    
    # TAB 4: DATA
    with tab4:
        st.header("**📈 Data Standar Siswa SMA**")
        data = {
            "Kegiatan": ["Mandi", "Cuci tangan", "Cuci piring", "Cuci baju"],
            "Rata-rata (L/hari)": [80, 5, 15, 50],
            "Hemat (L/hari)": [50, 2, 8, 30]
        }
        st.table(data)

st.markdown("---")
st.caption("*Simulasi Interaktif Fisika SMA - AquaFlow*")
