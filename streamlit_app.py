import streamlit as st

st.title("PENENTUAN BILANGAN GANJIL DAN GENAP")
st.title(":green[MASUK KE DALAM]")
import streamlit as st

number = st.number_input(label, min_value=None, max_value=None, value="min", step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", icon=None, width="stretch")
if number%2==1:
    st.write("Bilangan",number,"termasuk bilangan ganjil")
else:
    st.wrtie("BIlangan",number,"termasuk bilangan genap")
st.write("Nomor sekarang adalah ",number)
