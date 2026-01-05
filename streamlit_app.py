import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Kalkulator Kimia Analisis",
    page_icon="⚗️",
    layout="centered"
)

# =========================
# CSS STYLE
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #e3f2fd, #ffffff);
    }
    h1, h2, h3 {
        color: #0d47a1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# JUDUL APLIKASI
# =========================
st.title("🧪 Kalkulator Kimia Analisis")
st.write("### Silakan pilih jenis perhitungan di bawah ini")

# =========================
# MENU UTAMA (SATU KALI)
# =========================
menu = st.selectbox(
    "Pilih jenis perhitungan:",
    (
        "Faktor Pengenceran",
        "Molaritas",
        "Normalitas",
        "Mg/L",
        "% b/v",
        "% b/b",
        "% v/v"
    )
)

st.markdown("---")

# =========================
# DATABASE Mr
# =========================
mr_database = {
    "NaCl": 58.44,
    "HCl": 36.46,
    "H2SO4": 98.08,
    "NaOH": 40.00,
    "KOH": 56.11,
    "CH3COOH": 60.05,
    "NH3": 17.03,
    "KMnO4": 158.04,
    "AgNO3": 169.87,
    "CaCO3": 100.09
}

# =====================================================
# FAKTOR PENGENCERAN
# =====================================================
if menu == "Faktor Pengenceran":

    st.subheader("⚗️ Faktor Pengenceran")

    sub_menu = st.radio(
        "Pilih perhitungan:",
        ("Faktor pengenceran", "Volume yang harus diambil")
    )

    if sub_menu == "Faktor pengenceran":
        volume_labu = st.number_input("Volume labu takar (mL)", min_value=0.0)
        volume_pipet = st.number_input("Volume yang dipipet (mL)", min_value=0.0)

        if st.button("Hitung"):
            if volume_pipet == 0:
                st.error("Volume pipet tidak boleh 0")
            else:
                hasil = volume_labu / volume_pipet
                st.success(f"Faktor pengenceran = **{hasil:.3f}**")

    else:
        c1 = st.number_input("Konsentrasi awal", min_value=0.0)
        c2 = st.number_input("Konsentrasi akhir", min_value=0.0)
        v2 = st.number_input("Volume akhir (mL)", min_value=0.0)

        if st.button("Hitung"):
            if c1 == 0:
                st.error("Konsentrasi awal tidak boleh 0")
            else:
                v1 = (c2 * v2) / c1
                st.success(f"Volume yang diambil = **{v1:.3f} mL**")

# =====================================================
# MOLARITAS
# =====================================================
elif menu == "Molaritas":

    st.subheader("⚗️ Perhitungan Molaritas")

    metode = st.radio(
        "Metode perhitungan:",
        ("Input Mr manual", "Pilih dari database")
    )

    volume = st.number_input("Volume larutan (L)", min_value=0.0)
    massa = st.number_input("Massa zat (gram)", min_value=0.0)

    if metode == "Input Mr manual":
        mr = st.number_input("Mr zat", min_value=0.0)
    else:
        senyawa = st.selectbox("Pilih senyawa", list(mr_database.keys()))
        mr = mr_database[senyawa]
        st.info(f"Mr {senyawa} = {mr}")

    if st.button("Hitung"):
        if volume == 0 or mr == 0:
            st.error("Volume dan Mr tidak boleh 0")
        else:
            molaritas = massa / (mr * volume)
            st.success(f"Molaritas = **{molaritas:.4f} M**")

# =====================================================
# NORMALITAS
# =====================================================
elif menu == "Normalitas":

    st.subheader("⚗️ Perhitungan Normalitas")

    volume = st.number_input("Volume larutan (L)", min_value=0.0)
    massa = st.number_input("Massa zat (gram)", min_value=0.0)
    faktor = st.number_input("Faktor ekivalen (n)", min_value=0.0)

    senyawa = st.selectbox("Pilih senyawa", list(mr_database.keys()))
    mr = mr_database[senyawa]
    st.info(f"Mr {senyawa} = {mr}")

    if st.button("Hitung"):
        if volume == 0 or mr == 0 or faktor == 0:
            st.error("Volume, Mr, dan faktor ekivalen tidak boleh 0")
        else:
            normalitas = (massa * faktor) / (mr * volume)
            st.success(f"Normalitas = **{normalitas:.4f} N**")

# =====================================================
# Mg/L
# =====================================================
elif menu == "Mg/L":

    st.subheader("⚗️ Konsentrasi mg/L")

    massa = st.number_input("Massa zat (mg)", min_value=0.0)
    volume = st.number_input("Volume larutan (L)", min_value=0.0)

    if st.button("Hitung"):
        if volume == 0:
            st.error("Volume tidak boleh 0")
        else:
            hasil = massa / volume
            st.success(f"Konsentrasi = **{hasil:.4f} mg/L**")

# =====================================================
# % b/v
# =====================================================
elif menu == "% b/v":

    st.subheader("⚗️ % Berat/Volume")

    massa = st.number_input("Massa zat (gram)", min_value=0.0)
    volume = st.number_input("Volume larutan (mL)", min_value=0.0)

    if st.button("Hitung"):
        if volume == 0:
            st.error("Volume tidak boleh 0")
        else:
            persen = (massa / volume) * 100
            st.success(f"Konsentrasi = **{persen:.4f} % b/v**")

# =====================================================
# % b/b
# =====================================================
elif menu == "% b/b":

    st.subheader("⚗️ % Berat/Berat")

    massa_zat = st.number_input("Massa zat terlarut (gram)", min_value=0.0)
    massa_total = st.number_input("Massa campuran (gram)", min_value=0.0)

    if st.button("Hitung"):
        if massa_total == 0:
            st.error("Massa campuran tidak boleh 0")
        else:
            persen = (massa_zat / massa_total) * 100
            st.success(f"Konsentrasi = **{persen:.4f} % b/b**")

# =====================================================
# % v/v
# =====================================================
elif menu == "% v/v":

    st.subheader("⚗️ % Volume/Volume")

    volume_zat = st.number_input("Volume zat terlarut (mL)", min_value=0.0)
    volume_total = st.number_input("Volume larutan (mL)", min_value=0.0)

    if st.button("Hitung"):
        if volume_total == 0:
            st.error("Volume larutan tidak boleh 0")
        else:
            persen = (volume_zat / volume_total) * 100
            st.success(f"Konsentrasi = **{persen:.4f} % v/v**")
