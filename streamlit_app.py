import streamlit as st

st.title("PENENTUAN BILANGAN GANJIL DAN GENAP")
st.title(":green[MASUK KE DALAM]")

number = st.number_input("insert a number":,min_value=0,max_value=10000")
if number%2==1:
    st.write("Bilangan",number,"termasuk bilangan ganjil")
else:
    st.wrtie("BIlangan",number,"termasuk bilangan genap")
st.write("Nomor sekarang adalah ",number)
