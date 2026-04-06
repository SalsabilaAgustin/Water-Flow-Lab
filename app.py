import streamlit as st

st.set_page_config(page_title="AquaFlow", page_icon="💧", layout="wide")

st.title("💧 **AquaFlow - Simulasi Debit Air**")

# TAB 1: START
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Start", "📊 Simulasi", "🧠 Kuis", "📈 Data"])

with tab1:
    st.header("Selamat Datang!")
    st.write("Aplikasi simulasi pemakaian air harian")
    if st.button("Mulai Simulasi"):
        st.balloons()

with tab2:
    st.header("🚿 Simulasi Mandi")
    
    # Input
    waktu = st.slider("Waktu mandi (menit)", 1, 30, 10)
    jenis = st.selectbox("Jenis air", ["Shower (10L/menit)", "Keran (6L/menit)", "Ember (20L)"])
    kali = st.slider("Kali per hari", 1, 4, 2)
    
    # Hitung
    if "Shower" in jenis:
        debit = 10 * waktu
    elif "Keran" in jenis:
        debit = 6 * waktu
    else:
        debit = 20
    
    total = debit * kali
    
    # Hasil
    st.metric("Air per mandi", f"{debit} Liter")
    st.metric("Total harian", f"{total} Liter")
    
    st.write("**Grafik:**")
    st.bar_chart({"Shower": 100, "Keran": 60, "Ember": 20, "Anda": total})

with tab3:
    st.header("🧠 Kuis")
    st.write("**Soal 1:** Shower 10 menit 10L/menit = ?")
    jawaban = st.radio("Pilih:", ["10L", "100L", "1L"])
    
    if st.button("Jawab") and jawaban == "100L":
        st.success("✅ Benar!")
    elif st.button("Jawab"):
        st.error("❌ Coba lagi!")
    
    st.write("**Soal 2:** Rumus debit = ?")
    rumus = st.radio("Pilih:", ["Q = A + v", "Q = A × v", "Q = A / v"], key="rumus")
    
    if st.button("Jawab 2") and rumus == "Q = A × v":
        st.success("✅ Benar!")
    elif st.button("Jawab 2"):
        st.error("❌ Salah!")

with tab4:
    st.header("📈 Data")
    st.write("**Standar pemakaian air:**")
    st.write("- Mandi: 80L/hari")
    st.write("- Cuci tangan: 5L/hari") 
    st.write("- Cuci piring: 15L/hari")

st.markdown("---")
st.write("*Aplikasi belajar fisika - Debit air*")
