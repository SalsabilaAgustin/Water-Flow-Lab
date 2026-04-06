import streamlit as st

st.set_page_config(page_title="Simulasi Mandi", page_icon="🚿")

# TITLE
st.title("🚿 **Simulasi Pemakaian Air Mandi**")

# INPUT 1
st.markdown("### ⏰ **Waktu mandi (menit)**")
waktu_mandi = st.slider("", 1, 30, 10)

# INPUT 2  
st.markdown("### 💧 **Jenis air:**")
jenis_air = st.radio(
    "",
    ["Shower 🚿 (≈ 10 liter/menit)", "Keran 🚰 (≈ 6 liter/menit)"]
)

# INPUT 3
st.markdown("### 🔄 **Frekuensi per hari (berapa kali mandi)**")
frekuensi = st.slider("", 1, 4, 2)

st.markdown("---")

# PERHITUNGAN
debit = 10 if "Shower" in jenis_air else 6
air_per_mandi = debit * waktu_mandi
total_harian = air_per_mandi * frekuensi

# HASIL
st.markdown("### **Hasil:**")
col1, col2 = st.columns(2)
col1.metric("Per mandi", f"{air_per_mandi:.0f} L")
col2.metric("Harian", f"{total_harian:.0f} L")

# GRAFIK
st.markdown("### 📊 **Grafik**")
st.bar_chart({"Shower":10*waktu_mandi*frekuensi, "Keran":6*waktu_mandi*frekuensi, "Anda":total_harian})

st.markdown("---")
st.caption("Simulasi selesai")
