import streamlit as st

st.title("yieldlab")

massa = st.number_input("Massa Pereaksi")
mr = st.number_input("Mr Pereaksi")
mr_produk = st.number_input("Mr Produk")
hasil = st.number_input("Hasil Aktual")

if st.button("Hitung"):
    mol = massa / mr
    teoritis = mol * mr_produk
    rendemen = (hasil / teoritis) * 100

    st.write(f"Hasil Teoritis = {teoritis:.2f}")
    st.write(f"% Rendemen = {rendemen:.2f}%")
