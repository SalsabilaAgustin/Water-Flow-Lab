import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator Debit Air",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💧 Kalkulator Debit Fluida - Pemakaian Air Harian")
st.markdown("---")

# Fungsi perhitungan debit
@st.cache_data
def hitung_debit(kecepatan, luas_penampang):
    """Q = A × v (Debit = Luas Penampang × Kecepatan)"""
    return luas_penampang * kecepatan

@st.cache_data
def estimasi_pemakaian(waktu, debit):
    """Volume total = debit × waktu"""
    return debit * waktu

# SIDEBAR - Input Parameter
st.sidebar.header("⚙️ Pengaturan")
st.sidebar.markdown("---")

col1, col2 = st.sidebar.columns(2)
with col1:
    diameter = st.number_input("📏 Diameter pipa (cm)", 
                              min_value=0.1, max_value=10.0, value=2.0, step=0.1)
with col2:
    kecepatan = st.number_input("🏃 Kecepatan aliran (m/s)", 
                               min_value=0.1, max_value=5.0, value=1.0, step=0.1)

waktu_penggunaan = st.sidebar.slider("⏰ Waktu penggunaan (jam/hari)", 
                                     0.0, 24.0, 2.0, 0.5)

# Jenis aktivitas
aktivitas = st.sidebar.selectbox("🏠 Jenis Aktivitas",
                                ["Mandi", "Cuci piring", "Mencuci baju", "Siram tanaman", "Custom"])

# Estimasi otomatis berdasarkan aktivitas
if aktivitas != "Custom":
    estimasi = {
        "Mandi": {"diameter": 1.5, "kecepatan": 1.2, "waktu": 10},
        "Cuci piring": {"diameter": 1.0, "kecepatan": 0.8, "waktu": 15},
        "Mencuci baju": {"diameter": 2.0, "kecepatan": 1.5, "waktu": 30},
        "Siram tanaman": {"diameter": 0.8, "kecepatan": 0.5, "waktu": 20}
    }
    data = estimasi[aktivitas]
    diameter = data["diameter"]
    kecepatan = data["kecepatan"]
    waktu_penggunaan = data["waktu"]

# Perhitungan
luas_penampang = np.pi * (diameter / 200)**2  # cm → m
debit = hitung_debit(kecepatan, luas_penampang)
volume_harian = estimasi_pemakaian(waktu_penggunaan/24*3600, debit)  # m³/hari

# DISPLAY HASIL - 3 Kolom
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📏 Diameter Pipa", f"{diameter} cm")
    st.metric("🏃 Kecepatan Aliran", f"{kecepatan} m/s")

with col2:
    st.metric("📐 Luas Penampang", f"{luas_penampang:.4f} m²", delta=None)
    st.metric("⏰ Waktu Penggunaan", f"{waktu_penggunaan} jam")

with col3:
    st.metric("💧 **DEBIT (Q)**", f"{debit:.4f} m³/s", delta=None)
    st.metric("🚰 **Volume Harian**", f"{volume_harian:.2f} L", delta=None)

# Visualisasi 1: Grafik Hubungan Q-A-v
st.subheader("📊 Analisis Hubungan Debit (Q = A × v)")
col1, col2 = st.columns(2)

with col1:
    # Grafik 3D Surface
    A = np.linspace(0.0001, 0.01, 30)
    v = np.linspace(0.1, 3.0, 30)
    A, v = np.meshgrid(A, v)
    Q = A * v
    
    fig = go.Figure(data=[go.Surface(z=Q, x=A*10000, y=v, colorscale='Viridis')])
    fig.update_layout(title="Hubungan Q-A-v", scene=dict(xaxis_title="Luas (cm²)", 
                                                         yaxis_title="Kecepatan (m/s)",
                                                         zaxis_title="Debit (m³/s)"))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Grafik perubahan debit
    diameters = np.linspace(0.5, 5.0, 100)
    areas = np.pi * (diameters/200)**2
    Q_var = areas * kecepatan
    
    fig2 = px.line(x=diameters, y=Q_var*1000, 
                   labels={'x':'Diameter (cm)', 'y':'Debit (L/s)'},
                   title="Pengaruh Diameter terhadap Debit")
    st.plotly_chart(fig2, use_container_width=True)

# Tabel Perbandingan Standar
st.subheader("📋 Perbandingan Standar Pemakaian Air")
data_standar = {
    "Aktivitas": ["Mandi", "Cuci piring", "Mencuci baju", "Siram tanaman", "Anda"],
    "Volume Standar (L)": [50, 20, 100, 30, volume_harian*1000],
    "Efisiensi (%)": ["100", "100", "100", "100", f"{min(volume_harian*1000/75*100, 100):.0f}"]
}

st.dataframe(data_standar, use_container_width=True)

# Tips Penghematan
st.subheader("💡 Tips Penghematan Air")
tips = [
    "✅ Gunakan shower head hemat air",
    "✅ Tutup keran saat menggosok gigi",
    "✅ Cuci piring dalam wadah",
    "✅ Perbaiki kebocoran pipa segera"
]
for tip in tips:
    st.success(tip)

# Footer
st.markdown("---")
st.markdown("**Dibuat untuk mempermudah pemahaman siswa Fisika - Debit Fluida**")
st.caption("Q = A × v | Volume = Q × t")
