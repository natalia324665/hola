import streamlit as st
#1) crear las paginas
 uno= st.Page("paginas/uno.py",title="presentacion",icon=":material/star:")
 dos= st.Page("paginas/dos.py",title="teorema del valor medio",icon="🌞")
 tres= st.Page("paginas/tres.py",title="graficas",icon="🐇")
 cuatro= st.Page("paginas/cuatro.py",title="evaluacion",icon="🌜")
 cinco= st.Page("paginas/cinco.py",title="referencias",icon="📚")


 #2)crear la navegacion 
 pg = st.navigation({"prueba":[uno,dos,],"ejemplos":[tres],"cuatro":[cuatro],"cinco":[cinco]})

#iniciar la aplicacion
 pg.run()