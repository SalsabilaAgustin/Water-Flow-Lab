import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="💧AquaFlow Mandi", page_icon="🚿", layout="wide")

st.title("🚿 **AquaFlow - Kalkulator Air Mandi**")
st.markdown("*Estimasi Pemakaian Air Harian Siswa*")

# SIDEBAR INPUT
st.sidebar.header("📊 Input Data")
waktu_mandi = st.sidebar.slider("⏱️ Waktu mandi", 1, 30, 10, 1)
jenis_air = st.sidebar.selectbox("💧 Jenis air", 
                                ["Shower 🚿 (10 L/menit)", "Keran 🚰 (6 L/menit)", "Ember 🪣 (20 L/mandi)"])
frekuensi = st.sidebar.slider("🔄 Frekuensi per hari", 1, 4, 2, 1)

# DEBIT PER MENIT
if "Shower" in jenis_air:
    debit = 10  # L/menit
elif "Keran" in jenis_air:
    debit = 6   # L/menit
else:
    debit = 20  # L/mandi (langsung)

# HITUNG
if "Ember" in jenis_air:
    air_per_mandi = debit  # Fixed 20L
    total_harian = air_per_mandi * frekuensi
else:
    air_per_mandi = debit * waktu_mandi
    total_harian = air_per_mandi * frekuensi

# DISPLAY 3 KOLOM
col1, col2, col3, col4 = st.columns(4)
col1.metric("⏱️ Waktu mandi", f"{waktu_mandi} menit")
col2.metric("💧 Debit", f"{debit} L/menit")
col3.metric("🔄 Frekuensi", f"{frekuensi}x/hari")
col4.metric("🚿 Jenis", jenis_air)

# HASIL UTAMA
st.markdown("---")
col1, col2 = st.columns(2)
col1.metric("💦 **Air per mandi**", f"{air_per_mandi:.0f} **Liter**")
col2.metric("📅 **Total HARIAN**", f"{total_harian:.0f} **Liter**")

# GRAFIK PEMAKAIAN
st.subheader("📈 Perbandingan Harian")
data = {
    "Jenis Mandi": ["Shower", "Keran", "Ember"],
    f"{frekuensi}x/hari": [10*waktu_mandi*frekuensi, 6*waktu_mandi*frekuensi, 20*frekuensi]
}
df = pd.DataFrame(data)
st.bar_chart(df.set_index("Jenis Mandi"))

# TABEL DETAIL
st.subheader("📋 Rincian Lengkap")
tabel = {
    "Keterangan": ["Waktu per mandi", "Debit", "Air per mandi", "Frekuensi", "Total harian"],
    "Nilai": [f"{waktu_mandi} menit", f"{debit} L/menit", f"{air_per_mandi:.0f} L", f"{frekuensi}x", f"{total_harian:.0f} L"]
}
st.dataframe(tabel, use_container_width=True)

# REKOMENDASI
st.markdown("---")
st.subheader("💡 **Tips Hemat Air**")
if total_harian > 80:
    st.error(f"⚠️ **Tinggi!** {total_harian:.0f}L/hari (Rata-rata 60-80L)")
elif total_harian > 50:
    st.warning(f"ℹ️ Sedang: {total_harian:.0f}L/hari")
else:
    st.success(f"✅ **Hemat!** {total_harian:.0f}L/hari")

st.info("""
**Tips:**
- Gunakan shower <10 menit
- Tutup keran saat sabun
- Pakai ember 20L
- Mandi 1-2x/hari
""")

st.markdown("---")
st.caption("*AquaFlow - Edukasi Hemat Air Siswa*")
