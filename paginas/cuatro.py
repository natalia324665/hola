import streamlit as st
import sympy as sy
# Estilos personalizados con fondo de examen
st.markdown(
    """
    <style>
    body {
        background-color: #e0f7fa;  # Color de fondo
        font-family: 'Arial', sans-serif;
         background-color: #fce4ec;  # Color de fondo rosado
        font-family: 'Arial', sans-serif;
        
    }
    .success {
        color: green;
        font-weight: bold;
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
        background-color: #e8f5e9;  # Fondo suave verde para la respuesta correcta
    }
    .error {
        color: red;
        font-weight: bold;
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
        background-color: #ffebee;  # Fondo suave rojo para la respuesta incorrecta
    }
    .title {
        color: pink;
        font-size: 40px;
        font-weight: bold;
    }
    .header {
        color: #2E8B57;
        font-size: 30px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True
)

# Título del examen
st.markdown('<div class="title">📝 Examen de Retroalimentación: Teorema del Valor Medio</div>', unsafe_allow_html=True)

# Descripción del examen
st.markdown("""
Este examen te ayudará a reforzar lo aprendido sobre el *Teorema del Valor Medio*. Responde las siguientes preguntas seleccionando la opción correcta.
""")

# Pregunta 1: Concepto básico del TVM
st.header("1. ¿Qué establece el Teorema del Valor Medio?")

opciones_1 = st.radio(
    "Selecciona la opción correcta:",
    (
        "Si una función es continua en un intervalo cerrado y diferenciable en su interior, existe al menos un punto donde la derivada de la función es igual a la pendiente de la secante que conecta los extremos del intervalo.",
        "Si una función es continua y diferenciable en todo su dominio, entonces la derivada en cualquier punto es cero.",
        "El teorema establece que el valor medio de la función es igual a su valor en los extremos del intervalo.",
        "El teorema establece que la derivada de una función siempre será positiva."
    ),
    key="opciones_1",  # Añadimos un key único para identificar la respuesta
    index=None  # Aquí no asignamos ningún valor predeterminado (ninguna opción seleccionada)
)

# Verificar la respuesta solo después de la selección
if opciones_1:
    with st.container():  # Contenedor para la respuesta
        if opciones_1 == "Si una función es continua en un intervalo cerrado y diferenciable en su interior, existe al menos un punto donde la derivada de la función es igual a la pendiente de la secante que conecta los extremos del intervalo.":
            st.markdown('<div class="success">¡Correcto! Esto es lo que establece el Teorema del Valor Medio.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error">Incorrecto. El TVM relaciona la pendiente de la secante con la derivada de la función en algún punto del intervalo.</div>', unsafe_allow_html=True)

# Pregunta 2: Condiciones para aplicar el TVM
st.header("2. ¿Cuáles son las condiciones necesarias para aplicar el Teorema del Valor Medio?")

opciones_2 = st.radio(
    "Selecciona la opción correcta:",
    (
        "La función debe ser continua en el intervalo cerrado y diferenciable en el intervalo abierto.",
        "La función debe ser continua en todo su dominio.",
        "La función debe ser derivable en todos los puntos del intervalo.",
        "La función debe ser diferenciable en todo su dominio."
    ),
    key="opciones_2",  # Añadimos un key único para identificar la respuesta
    index=None  # Aquí no asignamos ningún valor predeterminado (ninguna opción seleccionada)
)

# Verificar la respuesta solo después de la selección
if opciones_2:
    with st.container():  # Contenedor para la respuesta
        if opciones_2 == "La función debe ser continua en el intervalo cerrado y diferenciable en el intervalo abierto.":
            st.markdown('<div class="success">¡Correcto! Esas son las condiciones que se deben cumplir para aplicar el TVM.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error">Incorrecto. Recuerda que el TVM requiere continuidad en el intervalo cerrado y diferenciabilidad en el intervalo abierto.</div>', unsafe_allow_html=True)

# Pregunta 3: Fórmula del TVM
st.header("3. ¿Cuál es la fórmula que establece el Teorema del Valor Medio?")

opciones_3 = st.radio(
    "Selecciona la opción correcta:",
    (
        "f'(c) = (f(b) - f(a)) / (b - a)",
        "f'(c) = (f(a) + f(b)) / 2",
        "f'(c) = (f(b) - f(a)) * (b - a)",
        "f'(c) = (f(b) - f(a)) / (a - b)"
    ),
    key="opciones_3",  # Añadimos un key único para identificar la respuesta
    index=None  # Aquí no asignamos ningún valor predeterminado (ninguna opción seleccionada)
)

# Verificar la respuesta solo después de la selección
if opciones_3:
    with st.container():  # Contenedor para la respuesta
        if opciones_3 == "f'(c) = (f(b) - f(a)) / (b - a)":
            st.markdown('<div class="success">¡Correcto! Esta es la fórmula que relaciona la derivada en el punto c con la pendiente de la secante.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error">Incorrecto. La fórmula correcta es f\'(c) = (f(b) - f(a)) / (b - a), donde c está en el intervalo (a, b).</div>', unsafe_allow_html=True)

# Pregunta 4: Aplicación del TVM
st.header("4. ¿Qué valor de c cumple el Teorema del Valor Medio para la función \(f(x) = x^2 - 2x + 3\) en el intervalo [1, 4]?")

opciones_4 = st.radio(
    "Selecciona la opción correcta:",
    (
        "c = 1.5",
        "c = 2.5",
        "c = 3",
        "c = 4"
    ),
    key="opciones_4",  # Añadimos un key único para identificar la respuesta
    index=None  # Aquí no asignamos ningún valor predeterminado (ninguna opción seleccionada)
)

# Verificar la respuesta solo después de la selección
if opciones_4:
    # Definimos la función f(x)
    x = sy.symbols("x")
    func = x**2 - 2*x + 3
    vi, vf = 1, 4
    f_val = sy.lambdify(x, func)
    
    # Calculamos la pendiente de la secante
    m_secante = (f_val(vf) - f_val(vi)) / (vf - vi)
    
    # Derivada de la función
    derivada = sy.diff(func, x)
    
    # Solucionamos para c
    c_sol = sy.solve(derivada - m_secante, x)
    c_sol = [sol.evalf() for sol in c_sol if vi < sol.evalf() < vf]
    
    # Verificamos la respuesta del usuario
    with st.container():  # Contenedor para la respuesta
        if opciones_4 == f"c = {c_sol[0]:.1f}":
            st.markdown(f'<div class="success">¡Correcto! El valor de c es aproximadamente {c_sol[0]:.2f}.</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="error">Incorrecto. El valor de c es aproximadamente {c_sol[0]:.2f}.</div>', unsafe_allow_html=True)

# Pregunta 5: Función no derivable
st.header("5. ¿Por qué el Teorema del Valor Medio no se puede aplicar a la función \(f(x) = |x|\) en el intervalo [-1, 1]?")

opciones_5 = st.radio(
    "Selecciona la opción correcta:",
    (
        "Porque la función no es continua.",
        "Porque la función no es derivable en el punto x=0.",
        "Porque la función no es diferenciable en todo el intervalo.",
        "Porque la derivada de la función no existe en ningún punto."
    ),
    key="opciones_5",  # Añadimos un key único para identificar la respuesta
    index=None  # Aquí no asignamos ningún valor predeterminado (ninguna opción seleccionada)
)

# Verificar la respuesta solo después de la selección
if opciones_5:
    with st.container():  # Contenedor para la respuesta
        if opciones_5 == "Porque la función no es derivable en el punto x=0.":
            st.markdown('<div class="success">¡Correcto! La función no es derivable en x=0.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error">Incorrecto. Recuerda que el TVM no se aplica cuando la función no es derivable en algún punto del intervalo.</div>', unsafe_allow_html=True)