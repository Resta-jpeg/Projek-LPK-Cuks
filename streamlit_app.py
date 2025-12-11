import streamlit as st

st.title("PENENTUAN BILANGAN GANJIL DAN GENAP")
st.title(":green[MASUK KE DALAM]")
import streamlit as st

number = st.number_input("Masukkan bilangan:,min_value=0,max_value=10000")
if number%2==1:
    st.write("Bilangan",number,"termasuk bilangan ganjil")
else:
    st.wrtie("BIlangan",number,"termasuk bilangan genap")
st.write("Nomor sekarang adalah ",number)
