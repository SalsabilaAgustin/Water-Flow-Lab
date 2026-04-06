import streamlit as st

st.set_page_config(page_title="AquaFlow", page_icon="💧", layout="wide")

# PAGE STATE
if "page" not in st.session_state:
    st.session_state.page = "home"

# HOME PAGE (START)
if st.session_state.page == "home":
    st.title("💧 **AquaFlow**")
    st.write("*Simulasi Air Mandi Harian*")
    
    st.write("---")
    st.write("""
    **Input yang dibutuhkan:**
    - Waktu mandi (menit)
    - Jenis air (Shower/Keran)  
    - Frekuensi per hari
    """)
    
    if st.button("**🚀 MULAI SIMULASI**"):
        st.session_state.page = "simulasi"
        st.rerun()

# SIMULASI PAGE
elif st.session_state.page == "simulasi":
    st.title("🚿 **Simulasi Mandi**")
    
    # BACK BUTTON
    if st.button("🏠 Kembali"):
        st.session_state.page = "home"
        st.rerun()
    
    st.write("---")
    
    # INPUT 1: Waktu mandi
    st.subheader("⏰ **Waktu mandi (menit)**")
    waktu_mandi = st.slider("Pilih waktu:", 1, 30, 10)
    
    # INPUT 2: Jenis air  
    st.subheader("💧 **Jenis air:**")
    jenis_air = st.radio(
        "Pilih jenis:", 
        ["Shower 🚿 (10 liter/menit)", "Keran 🚰 (6 liter/menit)"]
    )
    
    # INPUT 3: Frekuensi
    st.subheader("🔄 **Frekuensi per hari**")
    frekuensi = st.slider("Berapa kali mandi:", 1, 4, 2)
    
    st.write("---")
    
    # PERHITUNGAN
    if "Shower" in jenis_air:
        debit = 10
    else:
        debit = 6
    
    air_per_mandi = debit * waktu_mandi
    total_harian = air_per_mandi * frekuensi
    
    # HASIL
    st.subheader("**Hasil:**")
    col1, col2 = st.columns(2)
    col1.metric("Per mandi", f"{air_per_mandi} L")
    col2.metric("Total harian", f"{total_harian} L")
    
    # GRAFIK
    st.subheader("Grafik:")
    chart_data = {"Shower": 10*waktu_mandi*frekuensi, "Keran": 6*waktu_mandi*frekuensi, "Anda": total_harian}
    st.bar_chart(chart_data)
    
    # TABEL
    st.subheader("Rincian:")
    st.write(f"- Waktu: {waktu_mandi} menit")
    st.write(f"- Debit: {debit} L/menit") 
    st.write(f"- Frekuensi: {frekuensi} kali")
    st.write(f"- Total: {total_harian} Liter/hari")

st.write("---")
st.caption("AquaFlow - Simulasi Mandi")
