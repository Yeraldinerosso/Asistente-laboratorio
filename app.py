import streamlit as st
from openai import OpenAI

# FUNCIONES DE CÁLCULO

# Concentración
def calcular_molaridad(masa, peso_molecular, volumen):
    moles = masa / peso_molecular
    return moles / volumen

def calcular_normalidad(masa, peso_equivalente, volumen):
    equivalentes = masa / peso_equivalente
    return equivalentes / volumen

def calcular_equivalentes(masa, peso_equivalente):
    return masa / peso_equivalente

def calcular_porcentaje_peso_peso(masa_soluto, masa_solucion):
    return (masa_soluto / masa_solucion) * 100

def calcular_porcentaje_peso_volumen(masa_soluto, volumen_solucion):
    return (masa_soluto / volumen_solucion) * 100

def calcular_porcentaje_volumen_volumen(volumen_soluto, volumen_solucion):
    return (volumen_soluto / volumen_solucion) * 100

def calcular_ppm(masa_soluto, masa_solucion):
    return (masa_soluto / masa_solucion) * 10**6

def calcular_ppb(masa_soluto, masa_solucion):
    return (masa_soluto / masa_solucion) * 10**9


# Estequiometría
def calcular_moles(masa, peso_molecular):
    return masa / peso_molecular

def calcular_masa(moles, peso_molecular):
    return moles * peso_molecular

def determinar_reactivo_limitante(moles_reactivo1, relacion1, moles_reactivo2, relacion2):
    resultado1 = moles_reactivo1 / relacion1
    resultado2 = moles_reactivo2 / relacion2
    return "Reactivo 1" if resultado1 < resultado2 else "Reactivo 2"

def calcular_producto_estequiometrico(moles_reactivo, relacion_molar, peso_molecular_producto):
    return moles_reactivo * relacion_molar * peso_molecular_producto

# Rendimiento
def calcular_rendimiento_porcentual(rendimiento_real, rendimiento_teorico):
    return (rendimiento_real / rendimiento_teorico) * 100

def calcular_porcentaje_recuperacion(cantidad_obtenida, cantidad_esperada):
    return (cantidad_obtenida / cantidad_esperada) * 100

def calcular_porcentaje_pureza(masa_pura, masa_muestra):
    return (masa_pura / masa_muestra) * 100

# Diluciones
def calcular_dilucion(C1, V1, C2=None, V2=None):
    if C2 is None and V2 is not None:
        return (C1 * V1) / V2
    elif V2 is None and C2 is not None:
        return (C1 * V1) / C2
    else:
        return "❌ Solo dejar una variable como None"


# Interfaz de Usuario con Streamlit

st.set_page_config(page_title="Asistente de Laboratorio", page_icon="🧪", layout="wide")

st.markdown("""
    <style>
        .main { background-color: #f9f9f9; }
        h1, h2, h3 { color: #003366; }
        .stButton button { background-color: #0066cc; color: white; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("🔍 Navegación")
opcion = st.sidebar.radio("Ir a:", ["Inicio", "Cálculos de concentración", "Cálculos estequiométricos", "Cálculos de rendimiento", "Cálculos de diluciones","Asistente IA"])

# PÁGINA PRINCIPAL

if opcion == "Inicio":
    st.title("🧠 Asistente de Laboratorio Inteligente")
    st.write("""
    Herramienta interactiva para cálculos comunes en química de laboratorio y consultas a un asistente IA especializado:
    - Cálculos de concentración
    - Cálculos estequiométricos
    - Cálculos de rendimientos
    - Cálculos de diluciones
    - Asistente IA
    """)

# CONCENTRACIÓN

elif opcion == "Cálculos de concentración":
    st.header("🧪 Cálculos de concentración")
    tipo = st.selectbox("Seleccione el cálculo:", ["Molaridad", "Normalidad", "Equivalentes", "%p/p", "%p/v", "%v/v", "ppm", "ppb"])
    
    if tipo == "Molaridad":
        masa = st.number_input("Masa (g)", min_value=0.0)
        pm = st.number_input("Peso molecular (g/mol)", min_value=0.0)
        vol = st.number_input("Volumen (L)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"Molaridad: {calcular_molaridad(masa, pm, vol):.4f} mol/L")

    elif tipo == "Normalidad":
        masa = st.number_input("Masa (g)", min_value=0.0)
        pe = st.number_input("Peso equivalente (g/eq)", min_value=0.0)
        vol = st.number_input("Volumen (L)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"Normalidad: {calcular_normalidad(masa, pe, vol):.4f} eq/L")

    elif tipo == "Equivalentes":
        masa = st.number_input("Masa (g)", min_value=0.0)
        pe = st.number_input("Peso equivalente", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"Equivalentes: {calcular_equivalentes(masa, pe):.4f}")

    elif tipo == "%p/p":
        soluto = st.number_input("Masa soluto (g)", min_value=0.0)
        solucion = st.number_input("Masa solución (g)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"%p/p: {calcular_porcentaje_peso_peso(soluto, solucion):.4f} %")

    elif tipo == "%p/v":
        soluto = st.number_input("Masa soluto (g)", min_value=0.0)
        vol = st.number_input("Volumen solución (mL)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"%p/v: {calcular_porcentaje_peso_volumen(soluto, vol):.4f} %")

    elif tipo == "%v/v":
        v_soluto = st.number_input("Volumen soluto (mL)", min_value=0.0)
        v_solucion = st.number_input("Volumen solución (mL)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"%v/v: {calcular_porcentaje_volumen_volumen(v_soluto, v_solucion):.4f} %")

    elif tipo == "ppm":
        soluto = st.number_input("Masa soluto (g)", min_value=0.0)
        solucion = st.number_input("Masa solución (g)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"ppm: {calcular_ppm(soluto, solucion):.4f}")

    elif tipo == "ppb":
        soluto = st.number_input("Masa soluto (g)", min_value=0.0)
        solucion = st.number_input("Masa solución (g)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"ppb: {calcular_ppb(soluto, solucion):.4f}")


# ESTEQUIOMETRÍA

elif opcion == "Cálculos estequiométricos":
    st.header("⚗ Cálculos estequiométricos")
    tipo = st.selectbox("Seleccione el cálculo:", ["Calcular moles", "Calcular masa", "Reactivo limitante", "Producto esperado"])

    if tipo == "Calcular moles":
        masa = st.number_input("Masa (g)", min_value=0.0)
        pm = st.number_input("Peso molecular (g/mol)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"Moles: {calcular_moles(masa, pm):.4f}")

    elif tipo == "Calcular masa":
        moles = st.number_input("Moles", min_value=0.0)
        pm = st.number_input("Peso molecular (g/mol)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"Masa: {calcular_masa(moles, pm):.4f} g")

    elif tipo == "Reactivo limitante":
        m1 = st.number_input("Moles reactivo 1", min_value=0.0)
        r1 = st.number_input("Relación molar reactivo 1", min_value=0.0)
        m2 = st.number_input("Moles reactivo 2", min_value=0.0)
        r2 = st.number_input("Relación molar reactivo 2", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"Limitante: {determinar_reactivo_limitante(m1, r1, m2, r2)}")

    elif tipo == "Producto esperado":
        moles = st.number_input("Moles reactivo", min_value=0.0)
        relacion = st.number_input("Relación molar producto/reactivo", min_value=0.0)
        pm = st.number_input("Peso molecular producto (g/mol)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"Producto esperado: {calcular_producto_estequiometrico(moles, relacion, pm):.4f} g")

# RENDIMIENTO

elif opcion == "Cálculos de rendimiento":
    st.header("🔬 Cálculos de rendimiento")
    tipo = st.selectbox("Seleccione el cálculo:", ["Rendimiento porcentual", "% Recuperación", "% Pureza"])

    if tipo == "Rendimiento porcentual":
        real = st.number_input("Rendimiento real (g)", min_value=0.0)
        teorico = st.number_input("Rendimiento teórico (g)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"Rendimiento: {calcular_rendimiento_porcentual(real, teorico):.2f} %")

    elif tipo == "% Recuperación":
        obtenido = st.number_input("Cantidad obtenida (g)", min_value=0.0)
        esperado = st.number_input("Cantidad esperada (g)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"Recuperación: {calcular_porcentaje_recuperacion(obtenido, esperado):.2f} %")

    elif tipo == "% Pureza":
        pura = st.number_input("Masa pura (g)", min_value=0.0)
        muestra = st.number_input("Masa muestra total (g)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"Pureza: {calcular_porcentaje_pureza(pura, muestra):.2f} %")

# DILUCIONES

elif opcion == "Cálculos de diluciones":
    st.header("💧 Cálculos de diluciones")
    C1 = st.number_input("Concentración inicial (C1)", min_value=0.0)
    V1 = st.number_input("Volumen inicial (V1)", min_value=0.0)
    modo = st.selectbox("¿Qué deseas calcular?", ["C2", "V2"])

    if modo == "C2":
        V2 = st.number_input("Volumen final (V2)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"C2: {calcular_dilucion(C1, V1, C2=None, V2=V2):.4f}")

    elif modo == "V2":
        C2 = st.number_input("Concentración final (C2)", min_value=0.0)
        if st.button("Calcular"):
            st.success(f"V2: {calcular_dilucion(C1, V1, C2=C2, V2=None):.4f}")

# 📌 Sección del Asistente IA
# Configura Api Key
client = OpenAI(
  api_key= st.secrets["OPENAI_API_KEY"]
)

def consultar_ia(pregunta):
    respuesta = client.responses.create(
        model="gpt-4o-mini",
        input=f"""Eres un asistente experto en química de laboratorio. 
Responde en español de forma clara, directa y coherente con la pregunta. 
Da respuestas breves, sin extenderte innecesariamente (máximo 385 palabras). 
Tienes conocimientos en preparación de soluciones, fundamentos teóricos y normas de seguridad, 
pero solo menciónalos si son relevantes para la pregunta."""
              f"Pregunta: {pregunta}",
        max_output_tokens=400,
        temperature=0.3
    )
    return respuesta.output_text

# Agregar la opción en el menú lateral
if opcion == "Asistente IA":
    st.header("🤖 Consulta al Asistente IA")
    consulta = st.text_area("Escribe tu pregunta de laboratorio (preparación de soluciones, fundamentos teóricos y normas de seguridad)")
    
    if st.button("Consultar IA"):
        if consulta.strip() != "":
            with st.spinner("Consultando a la IA..."):
                respuesta = consultar_ia(consulta)
            st.markdown("### 💡 Respuesta de la IA:")
            st.write(respuesta)
        else:
            st.warning("Por favor escribe una consulta antes de enviar.") 


