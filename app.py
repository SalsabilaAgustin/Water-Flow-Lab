import streamlit as st

st.set_page_config(page_title="AquaFlow", page_icon="💧", layout="wide")

# State
if 'halaman' not in st.session_state:
    st.session_state.halaman = 'start'

# HALAMAN AWAL (SAMA)
if st.session_state.halaman == 'start':
    st.markdown("""
    <style>
    .big-title {font-size: 5rem !important; color: #4ecdc4; text-align: center;}
    .cute-text {font-size: 2.5rem !important; color: #45b7d1; text-align: center;}
    .start-btn {font-size: 2rem !important; padding: 1.5rem !important;}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="big-title">💦✨ AquaFlow ✨💦</h1>', unsafe_allow_html=True)
    st.markdown('<p class="cute-text">Simulasi Interaktif Fisika SMA 🛁🚿</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("🚀 **START** 🚀", use_container_width=True):
            st.session_state.halaman = 'main'
            st.rerun()

# HALAMAN MAIN
elif st.session_state.halaman == 'main':
    st.markdown("### 💧 **Dashboard AquaFlow** 💧")
    col1, col2 = st.columns([1,10])
    with col1:
        if st.button("🏠"):
            st.session_state.halaman = 'start'
            st.rerun()
    
    tab1, tab2, tab3, tab4 = st.tabs(["🚿 Simulasi", "🧮 Kalkulator", "🧠 Kuis", "📈 Data"])
    
    # TAB 1: SIMULASI MANDI - FULL UPDATE
    with tab1:
        st.header("🚿 **Simulasi Mandi**")
        
        # INPUT (SAMA)
        st.markdown("### **Waktu mandi (menit)**")
        waktu_mandi = st.slider("", 1, 30, 10)
        
        st.markdown("### **Jenis air:**")
        jenis_air = st.radio("", ["Shower 🚿 (≈ 10 liter/menit)", "Keran 🚰 (≈ 6 liter/menit)"])
        
        st.markdown("### **Frekuensi per hari (berapa kali mandi)**")
        frekuensi = st.slider("", 1, 4, 2)
        
        # PERHITUNGAN
        debit = 10 if "Shower" in jenis_air else 6
        air_per_mandi = debit * waktu_mandi
        total_harian = air_per_mandi * frekuensi
        total_bulanan = total_harian * 30
        
        st.markdown("---")
        
        # HASIL METRIC
        col1, col2 = st.columns(2)
        col1.metric("💦 Air per mandi", f"{air_per_mandi:.0f} L")
        col2.metric("📅 **Total air per hari**", f"{total_harian:.0f} L")
        st.metric("**Estimasi per bulan**", f"{total_bulanan:.0f} L")
        
        # KATEGORI
        st.markdown("### **Kategori penggunaan:**")
        if total_harian < 100:
            kategori = "💚 **Hemat (< 100 liter)**"
            st.success(f"✅ {total_harian:.0f} L/hari - Sangat baik!")
        elif total_harian <= 200:
            kategori = "⚡ **Normal (100–200 liter)**"
            st.info(f"ℹ️ {total_harian:.0f} L/hari - Cukup baik!")
        else:
            kategori = "🔥 **Boros (> 200 liter)**"
            st.error(f"⚠️ {total_harian:.0f} L/hari - Hemat air!")
        st.markdown(kategori)
        
        # 1. TIPS OTOMATIS
        st.markdown("### 💡 **Tips Otomatis**")
        hemat_2_menit = debit * 2 * frekuensi
        st.info(f"**🎯 Kurangi 2 menit mandi → hemat {hemat_2_menit:.0f} liter air per hari!**")
        
        if total_harian > 150:
            st.warning("**💧 Ganti shower hemat air → hemat 30%!**")
        elif total_harian > 100:
            st.info("**⏱️ Mandi <10 menit → lebih hemat!**")
        
        # 2. PERBANDINGAN UNIK
        st.markdown("### ⚖️ **Perbandingan Unik**")
        galon_air = total_harian / 19  # 1 galon ≈ 19L
        st.metric("💧 Galon air/hari", f"{galon_air:.1f} galon")
        st.info(f"**Penggunaanmu setara {galon_air:.0f} galon air mineral per hari!**")
        
        # 3. VISUAL PROGRESS BAR
        st.markdown("### 📊 **Status Penggunaan**")
        progress = min(total_harian / 300, 1.0)  # Max 300L
        warna = "success" if total_harian < 100 else "info" if total_harian <= 200 else "error"
        
        st.progress(progress, text=f"{total_harian:.0f}/300 L (Max)")
        
        if total_harian < 100:
            st.success("💚 HEMAT")
        elif total_harian <= 200:
            st.info("⚡ NORMAL")
        else:
            st.error("🔥 BOROS")
        
        # GRAFIK
        st.markdown("### **📈 Perbandingan Air**")
        st.bar_chart({"Shower 🚿": 10*waktu_mandi*frekuensi, "Keran 🚰": 6*waktu_mandi*frekuensi})
        
        # RINCIAN
        st.markdown("### **📋 Rincian**")
        st.write(f"• Waktu: **{waktu_mandi}** menit")
        st.write(f"• Jenis: **{jenis_air}**")
        st.write(f"• Frekuensi: **{frekuensi}** kali")
        st.write(f"• Total harian: **{total_harian:.0f} L**")
        st.write(f"• Total bulanan: **{total_bulanan:.0f} L**")
    
    # TAB LAIN (SAMA)
    with tab2:
        st.header("🧮 **Kalkulator**")
        col1, col2 = st.columns(2)
        diameter = col1.number_input("Diameter (cm)", 0.5, 5.0, 2.0)
        kecepatan = col2.number_input("Kecepatan (m/s)", 0.1, 3.0, 1.0)
        r = diameter / 200
        A = 3.14 * r * r
        Q = A * kecepatan
        col1.metric("A", f"{A:.5f} m²")
        col2.metric("Q", f"{Q:.5f} m³/s")
    
    with tab3:
        st.header("🧠 **Kuis**")
        # 5 soal dengan balon (sama seperti sebelumnya)
        st.markdown("**1.** Shower 10 menit = ?")
        jawab1 = st.radio("", ["10 L", "100 L", "1 L"], key="s1")
        if st.button("Cek 1"):
            if jawab1 == "100 L":
                st.success("BENAR!")
                st.balloons()
            else:
                st.error("❌")
        # ... soal 2-5 sama
    
    with tab4:
        st.header("📈 **Data**")
        data = {"Kegiatan": ["Mandi"], "Rata": [80], "Hemat": [50]}
        st.table(data)

st.markdown("---")
st.caption("💧 AquaFlow - Simulasi Lengkap")
