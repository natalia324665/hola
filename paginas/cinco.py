import streamlit as st
#titulo de la aplicación
st.title("Referencias")
#lista de referencias

referencias=[
    {
        "Autor":"Wikipedia",
        "Título":"Teorema del valor medio",
        "Año":2024
    },
    {
        "Autor":"OpenStax",
        "Título":"El teorema del valor medio - Cálculo volumen 1",
        "Año":2022
    },
    {
        "Autor":"González, Mauricio",
        "Título":"Una aplicación poco frecuente: teorema del valor medio para integrales aplicado a ingeniería química",
        "Año":2005
    },
    {
        "Autor":"Martínez de la Rosa, Félix",
        "Título":"Panorámica de los Teoremas de Valor Medio",
        "Año":2024
    },
    {
        "Autor":"Navia Lora, Mauricio",
        "Título":"El Teorema del Valor Intermedio y la Completitud de los Reales",
        "Año":2001
    }
]
#mostrar las referencias en la aplicacion 
for ref in referencias:
    st.write(f"{ref['Autor']} ({ref['Año']}) - {ref['Título']}")
