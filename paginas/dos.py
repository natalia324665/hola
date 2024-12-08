import streamlit as st

# Custom CSS for design improvements
st.markdown(
    """
    <style>
        .title {
            color: #4CAF50;
            font-size: 36px;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }
        .section-header {
            color: #3E7C7A;
            font-size: 28px;
            font-family: 'Arial', sans-serif;
        }
        .content-text {
            font-size: 18px;
            font-family: 'Helvetica', sans-serif;
        }
        .image-container {
            text-align: center;
            margin-bottom: 20px;
        }
        .video-container {
            text-align: center;
            margin-top: 20px;
        }
    </style>
    """, unsafe_allow_html=True
)
##

import streamlit as st

# Custom CSS for the title
st.markdown(
    """
    <style>
        .custom-title {
            font-size: 50px;
            color:  orange;   
            font-weight: bold;
            text-align: center;  
            text-transform: uppercase;  # Make text uppercase
            font-family: 'Arial', sans-serif;  # Use Arial font
        }
    </style>
    """, unsafe_allow_html=True
)

# Create a title with custom styling
st.markdown('<h1 class="custom-title">🧮 Teorema del Valor Medio 📐</h1>', unsafe_allow_html=True)



# Image Example
st.markdown('<div class="image-container"><img src="https://www.teoremas.club/wp-content/uploads/2023/10/teorema-del-valor-medio-jpg.webp" style="width:70%; height:auto;"></div>', unsafe_allow_html=True)


###33##33#33
st.header("💡Introducción")

st.markdown("""El Teorema del Valor Medio es un principio fundamental en el cálculo que establece una relación entre el comportamiento de una función y su derivada. Este teorema es crucial para entender cómo las funciones cambian y se comportan en intervalos específicos. Se basa en la idea de que si una función es continua en un intervalo cerrado y diferenciable en el intervalo abierto correspondiente, entonces existe al menos un punto dentro de ese intervalo donde la pendiente de la tangente a la curva es igual a la pendiente de la secante que conecta los extremos del intervalo.""")

# Video Section
st.markdown('<div class="video-container"><iframe width="560" height="315" src="https://www.youtube.com/embed/e2byfEjtD7s" frameborder="0" allowfullscreen></iframe></div>', unsafe_allow_html=True)




# Historia
st.divider()
st.header("🕰️ Historia del Teorema del Valor Medio")
col1, col2 = st.columns(2)

with col1:
 st.image("https://www.fisicalab.com/sites/all/files/contenidos/matematicas/2798_t_valor_medio/lagrange.jpg")
with col2:
 st.header("""Joseph-Louis """)
 st.markdown("""El teorema del valor medio, formulado por Joseph-Louis Lagrange en el siglo XVIII, establece que, si una función es continua en un intervalo cerrado y diferenciable en su interior, existe al menos un punto donde la derivada es igual a la pendiente de la secante. Su primera mención se atribuye a Paramésuara en el siglo XV, y fue formalmente demostrado por Cauchy en 1823""")


with st.container(border=True):
 st.header("🌟Enunciado del Teorema Valor Medio🌟")
 st.markdown("“El teorema de el valor medio establece que si una función es continua en el intervalo cerrado [a,b] y diferenciable en el intervalo abierto (a,b), entonces existe un punto c contenido en el intervalo (a,b) tal que f'(c) es igual a la razón de cambio promedio de la función en [a,b]. En otras palabras, la tangente de la gráfica en algún punto es paralela a la recta secante que pasa por (a,f(a)) y (b,f(b)).”")
 st.latex(r"f'(c) = \frac{f(b) - f(a)}{b - a}.")

# Demostración
st.divider()
st.header("📜 Demostración del Teorema ")


st.markdown("""la demostracion de este teorema consiste en aplicar el teorema de Rolle en [a, b] a la funcion auxiliar.Como la pendiente de esa línea es:""")

st.latex(r"\text{Pendiente} = \frac{f(b) - f(a)}{b - a}")

st.markdown("""y la línea pasa por el punto  (a,f(a)), la ecuación de esa línea se puede escribir como.""")

st.latex(r"y = \frac{f(b) - f(a)}{b - a}(x - a) + f(a)")

st.markdown("Supongamos que  g(x) denota la diferencia vertical entre el punto  [x,f(x)] y el punto  (x,y) en esa línea. Por lo tanto,")
st.latex(r"g(x) = f(x) - \left( \frac{f(b) - f(a)}{b - a}(x - a) + f(a) \right)")



st.markdown("""Por lo tanto,  g satisface los criterios del teorema de Rolle. En consecuencia, existe un punto  c∈(a,b) de manera que  g'(c)=0. Dado que""")
st.latex(r"g'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}")

st.markdown("""veamos que""")
st.latex(r"g'(c) = f'(c) - \frac{f(b) - f(a)}{b - a}.")

st.markdown("""Dado que  g'(c)=0, concluimos que""")
st.latex(r"f'(c) = \frac{f(b) - f(a)}{b - a}.")

# Gráfica

st.header("📊 Gráfica del Teorema del Valor Medio")

st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://openstax.org/apps/archive/20241024.164013/resources/8f22590bb46713efdae2b7cc7ee843d9a4eeee4e" alt="Teorema del Valor Medio" style="width:80%; height:auto;">
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown("""Como la derivada de una función en un punto es la tangente del ángulo α que forma la recta tangente en ese punto, las tangentes de los ángulos de las dos rectas, la recta secante que pasa por AB y la recta tangente en el punto (c, f(c)) son paralelas y la tangente de ambas es f’(c).""")



st.header("🔚 Conclusion")

st.markdown("""
El Teorema del Valor Medio es una herramienta poderosa en el cálculo diferencial, ya que conecta las propiedades de una función con su tasa de cambio en un intervalo. A través de este teorema, podemos entender mejor cómo se comportan las funciones y encontrar puntos específicos de interés en su dominio. Es un teorema esencial en el análisis matemático y tiene aplicaciones prácticas en diversas áreas, como la física, la economía y la ingeniería.
""")
