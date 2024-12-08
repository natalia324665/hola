import streamlit as st

#titulos
uno= st.Page("paginas/uno.py",title="Presentacion", icon=":material/star:")
dos=st.Page("paginas/dos.py", title="Teorema del valor medio", icon="🌞")
tres=st.Page("paginas/tres.py", title="graficas", icon="🐇")
cuatro=st.Page("paginas/cuatro.py", title="Evaluacion", icon="🌜")
cinco=st.Page("paginas/cinco.py", title="Referencias", icon="📚")

#2)crear la pagina
pg= st.navigation({"prueba":[uno,dos], "ejempos":[tres], "Evaluacion":[cuatro],"Referencias":[cinco]})

#3)iniciar la aplicacio
pg.run()