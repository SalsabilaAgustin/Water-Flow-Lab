import streamlit as st

st.set_page_config(page_title="Simulasi Mandi", page_icon="🚿", layout="wide")

st.title("🚿 **Simulasi Pemakaian Air Mandi**")
st.markdown("*Hitung kebutuhan air mandi harian*")

# ========================================
# INPUT SESUAI PERMINTAAN
# ========================================
st.markdown("---")
st.header("📊 **Input Data**")

col1, col2 = st.columns(2)

# 1. Waktu mandi (menit)
waktu_mandi = col1.slider(
    "⏰ **Waktu mandi (menit)**", 
    min_value=1, max_value=30, value=10, step=1
)

# 2. Jenis air
jenis_air = col2.selectbox(
    "💧 **Jenis air:**", 
    ["Shower 🚿 (≈ 10 liter/menit)", "Keran 🚰 (≈ 6 liter/menit)"]
)

# 3. Frekuensi per hari
frekuensi = st.slider(
    "🔄 **Frekuensi per hari (berapa kali mandi)**", 
    min_value=1, max_value=4, value=2, step=1
)

st.markdown("---")

# ========================================
# PERHITUNGAN
# ========================================
if "Shower" in jenis_air:
    debit_per_menit = 10  # L/menit
elif "Keran" in jenis_air:
    debit_per_menit = 6   # L/menit

air_per_mandi = debit_per_menit * waktu_mandi
total_harian = air_per_mandi * frekuensi

# ========================================
# HASIL
# ========================================
st.header("📈 **Hasil Perhitungan**")

col1, col2, col3 = st.columns(3)
col1.metric("⏰ Waktu mandi", f"{waktu_mandi} menit")
col2.metric("💧 Debit", f"{debit_per_menit} L/menit")
col3.metric("🔄 Frekuensi", f"{frekuensi} kali")

col1, col2 = st.columns(2)
col1.metric("💦 **Air per mandi**", f"{air_per_mandi:.0f} **Liter**")
col2.metric("📅 **Total HARIAN**", f"{total_harian:.0f} **Liter**")

# ========================================
# GRAFIK
# ========================================
st.subheader("📊 **Perbandingan**")

# Data untuk grafik
data_grafik = {
    "Shower": 10 * waktu_mandi * frekuensi,
    "Keran": 6 * waktu_mandi * frekuensi,
    "Anda": total_harian
}

st.bar_chart(data_grafik)

# ========================================
# RINCIAN & TIPS
# ========================================
st.markdown("---")
st.subheader("📋 **Rincian**")

rincian = {
    "Keterangan": ["Waktu per mandi", "Debit per menit", "Air per mandi", "Frekuensi", "Total harian"],
    "Hasil": [f"{waktu_mandi} menit", f"{debit_per_menit} L/menit", f"{air_per_mandi:.0f} L", f"{frekuensi} kali", f"{total_harian:.0f} L"]
}

st.table(rincian)

# Tips hemat
st.subheader("💡 **Tips Hemat**")
if total_harian > 100:
    st.error(f"⚠️ **Tinggi!** {total_harian:.0f}L/hari")
    st.info("• Mandi <10 menit\n• Pakai ember\n• Tutup keran")
elif total_harian > 60:
    st.warning(f"📈 Sedang: {total_harian:.0f}L")
else:
    st.success(f"✅ **Hemat!** {total_harian:.0f}L")

st.markdown("---")
st.caption("💧 Simulasi Mandi - AquaFlow")
