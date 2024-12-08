import streamlit as st

#1) crear las paginas 
uno= st.Page("paginas/uno.py", title="presentacion",icon=":material/star:")
dos= st.Page("paginas/dos.py" , title="teorema del valor medio" , icon="🌞")
tres= st.Page("paginas/tres.py", title="graficas", icon="🐇")
cuatro = st.Page("paginas/cuatro.py", title="Evaluación", icon="🌜")

#2) cree la navegacion
#pg= st.navigation([uno,dos,tres])
pg= st.navigation({"prueba":[uno,dos],"ejemplos":[tres],"Evaluación": [cuatro]})

#iniciar la aplicaion
pg.run()