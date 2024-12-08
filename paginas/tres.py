import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

#Título y descripción del ejemplo
st.title ("🧮 Ejemplos Interactivos del Teorema")
st.markdown("""En estos ejemplos, puedes introducir una función y ajustar los valores del intervalo [a, b]. El sistema calculará automáticamente el punto c que cumple con el *Teorema del Valor Medio* y mostrará la gráfica correspondiente.""")

# columnas
c1,c2 =st.columns([1,2],vertical_alignment="center")
with c1 :
 func = st.text_input("$f(x)=$",value="x**2 -2*x+3")
 vi, vf=st.slider("intervalo",min_value=-100,max_value=100,value=(1,100))

# crear una expresion con sympy
x= sy.symbols("x")
exp= sy.parse_expr(func)
f= sy.lambdify(x,exp)  #para poder evaluar vectores 

with c1 :
 st.latex(sy.latex(sy.parse_expr(func)))

#) creamos los vectores
x= np.linspace(vi, vf , 1000)  
y= f(x)

fig,ax =plt.subplots()

ax.plot(x,y)

#ecuacion pendiente secante
m_secante= (f(vf) - f(vi)) / (vf - vi)

#recta secante
x_secante= np.linspace(vi, vf, 1000)  
y_secante= m_secante * (x_secante - vi) + f(vi)  # Ecuación de la secante

#Graficar la secante
ax.plot(x_secante, y_secante,label="secante",color="orange" ,linestyle='--')

# punto medio del intervalo c
c= (vi + vf) / 2

#recta tangente 
y_tangente= m_secante * (x - c) + f(c)
ax.plot(x_secante, y_tangente, label="Tangente",color="green" )

ax.legend ()
  
with c2 :
 st.pyplot(fig)

st.divider ()

st.markdown ("Este es un ejemplo de cómo las tangentes a una función pueden ser paralelas a una secante entre dos puntos de la curva.")

#Entrada de la función
funcion= st.text_input("$f(x)=$", value="sin(x)")

#Convertir a una expresión matemática
x= sy.symbols("x")
exp= sy.parse_expr(funcion)
f= sy.lambdify(x, exp)

st.latex (sy.latex(exp))

#Selección de los valores de a y b, asegurándose de que cada slider tenga una key única
a, b = st.slider("Valores $a$ y $b$ del teorema:", value=(10, 4), min_value=0, max_value=10, key="slider_a_b")

#Graficar
fig,ax = plt.subplots()

xi= np.linspace(0, 10, 1000)
yi= f(xi)

#Graficar la función
ax.plot(xi, yi, label="$f(x)$",color="orange", linewidth=2)

#Graficar la secante entre los puntos a y b
ax.plot([a, b],[exp.subs(x, a), exp.subs(x, b)], c="red", marker="o", label="Secante", linewidth=2)

#Calcular la pendiente de la secante
m= (f(b) - f(a)) / (b - a)
der= exp.diff(x)

#Resolver para la tangente
sols= sy.solve(der - m, x)
for c in sols :
    if a < c < b :
        inter= exp.subs(x, c) - m * c
        yi_tangente= m * xi + inter
        ax.plot(xi, yi_tangente,c="blue",label="Tangente paralela", linewidth=2)
        

#Añadir etiquetas
ax.set_xlabel ("x")
ax.set_ylabel ("$f(x)$")

#Mostrar el gráfico
st.pyplot (fig)

#Mostrar la pendiente de la secante
st.latex(f"m= {m}")

st.divider ()

# funcion no derivable 

#Título y descripción del ejemplo
st.title ("🧮 Ejemplo de una función que no cumple el Teorema del Valor Medio")

st.markdown("""En este ejemplo, utilizamos una función *no derivable* dentro del intervalo. 
Esto rompe uno de los requisitos clave del *Teorema del Valor Medio*, lo que lo hace inválido.""")

#Configuración inicial
c1, c2= st.columns([1, 2], vertical_alignment="center")
with c1 :
    func= st.text_input("$f(x)=$", value="Abs(x)")  # Usamos valor absoluto como ejemplo
    vi, vf= st.slider("Intervalo", min_value=-10, max_value=10, value=(-3, 3))

#Crear una expresión con Sympy
x= sy.symbols("x")
exp= sy.parse_expr(func)
f= sy.lambdify(x, exp, modules=["numpy"])  # Para trabajar con numpy

#Mostrar la función matemática
with c1 :
 st.latex(sy.latex(exp))

#) Crear los vectores
x_vals= np.linspace(vi, vf, 1000)  
y_vals= f(x_vals)

fig,ax = plt.subplots()

#graficar la función
ax.plot(x_vals,y_vals, label="Función $f(x)$", color="blue")

#Calcular pendiente de la secante
m_secante= (f(vf) - f(vi)) / (vf - vi)

#Recta secante
x_secante= np.linspace(vi, vf, 1000)  
y_secante= m_secante * (x_secante - vi) + f(vi)

#Graficar la secante
ax.plot(x_secante, y_secante,label="Secante", color="orange", linestyle="--")

#Marcar los puntos de no derivabilidad (en este caso, x=0)
if vi < 0 < vf :
 ax.scatter([0], [f(0)], color="red", label="Punto no derivable (x=0)", zorder=5)

#Configuración del gráfico
ax.axhline(0,color="black", linewidth=0.8, linestyle="--")
ax.axvline(0,color="black", linewidth=0.8, linestyle="--")
ax.legend ()
ax.set_title ("Función no derivable (No cumple el TVM)")
ax.set_xlabel ("$x$")
ax.set_ylabel ("$f(x)$")

#Mostrar el gráfico en Streamlit
with c2 :
 st.pyplot(fig)