import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurar el estilo de gráficos para un mejor look en Streamlit
sns.set_style("whitegrid")
# Aumentar la resolución para mejor calidad de imagen en la web
plt.rcParams['figure.dpi'] = 150 


# ---------------------------------------------
# 1. FUNCIÓN DE CARGA DE DATOS (Solución del NameError)
# ---------------------------------------------
@st.cache_data
def load_data():
    """Carga el dataset desde GitHub y lo almacena en caché."""
    DATA_URL = "https://raw.githubusercontent.com/bssanchezlopez/Grupo_1/refs/heads/main/synthetic_fraud_dataset.csv"
    try:
        # Aquí se carga la información que proporcionaste
        df = pd.read_csv(DATA_URL)
        return df
    except Exception as e:
        # Esto ayuda a depurar si la URL o el archivo falla
        st.error(f"Error al cargar el dataset desde GitHub. Verifica la URL: {e}")
        return pd.DataFrame() 


############################# CONFIGURACIÓN INICIAL ##############################

# Configuración global para todas las páginas
st.set_page_config(page_title="Detección de Fraude | ISIL", layout="wide")

# Rutas de las imágenes (Manteniendo tu lógica original)
ISIL_LOGO_PATHS = ["ISIL.png", "assets/ISIL.png", "images/ISIL.png"]
loaded = False

for path in ISIL_LOGO_PATHS:
    try:
        st.sidebar.image(path, caption="Grupo #1")
        loaded = True
        break
    except FileNotFoundError:
        continue

if not loaded:
    st.sidebar.error(
        f"Error: Archivo 'ISIL.png' no encontrado. Asegúrate de subirlo."
    )


# -------------------------------------------------------------------
# 2. DEFINICIÓN DE PÁGINAS (page3 contiene el EDA corregido y funcional)
# -------------------------------------------------------------------


def page1():
    st.title("Detección de Transacciones Fraudulentas")
    st.markdown("---")
    st.write("La Frontera Digital de la Seguridad Financiera")
    st.markdown("""
    En la era del comercio electrónico y la banca digital, la **Detección de Operaciones Fraudulentas** se ha convertido en una disciplina crítica para proteger tanto a las instituciones financieras 
    como a los consumidores.
    Este proyecto explora la evolución de los sistemas antifraude, desde los primeros modelos 
    estadísticos basados en reglas fijas hasta la aplicación actual de la Inteligencia Artificial 
    y el Aprendizaje Profundo (*Deep Learning*).
    Analizaremos cómo los hitos tecnológicos han redefinido la batalla contra el crimen financiero, 
    permitiendo la identificación de patrones de riesgo sutiles y la prevención en tiempo real.
    """)


def page2():
    st.title("Detección de Transacciones Fraudulentas | Línea de Tiempo de Hitos Clave")
    st.markdown("---")
    st.write("Autor: GRUPO 1 | ISIL")
    st.write("Explora los 5 eventos tecnológicos que transformaron la lucha contra el fraude bancario.")
    st.markdown("---")

    # --- URLs y Definición de Hitos con Información Ampliada ---
    base_url = "https://raw.githubusercontent.com/adrianticonatapia-debug/timeline_s1/main/timeline_images/"

    hitos = {
         1: {
              "año": "Finales del S. XX",
              "nombre": "Sistemas de Puntuación de Riesgo (FICO)",
              "concepto": "Implementación de modelos estadísticos para asignar una puntuación de riesgo a individuos.",
              "descripcion": "El desarrollo de modelos como el FICO Score introdujo la metodología de usar datos históricos y algoritmos para evaluar el riesgo en tiempo real.",
              "figura_clave": "Fair Isaac Corporation (FICO) y pioneros de la estadística.",
              "imagen_url": base_url + "timeline1.png"
          },
          2: {
              "año": "Inicios del 2000",
              "nombre": "Autenticación de Doble Factor (2FA)",
              "concepto": "Requerir dos o más factores de verificación para el acceso a cuentas y la ejecución de transacciones.",
              "descripcion": "Este desarrollo cambió el enfoque de la detección a la prevención activa, dificultando el 'Account Takeover' (ATO).",
              "figura_clave": "Pioneros de la seguridad en banca online y SMS/Token.",
              "imagen_url": base_url + "timeline2.png"
          },
          3: {
              "año": "2000 - 2015",
              "nombre": "Adopción Global del Chip EMV",
              "concepto": "Transición de la banda magnética a tarjetas con un chip que genera un código criptográfico único para cada transacción.",
              "descripcion": "El chip EMV eliminó casi por completo el fraude físico por clonación ('skimming'), forzando a los criminales a migrar a transacciones 'Card-Not-Present' (CNP).",
              "figura_clave": "Consorcio EMV (Europay, Mastercard, Visa).",
              "imagen_url": base_url + "timeline3.png"
          },
          4: {
              "año": "Década de 2010",
              "nombre": "El Auge de Machine Learning (ML) y Deep Learning (DL)",
              "concepto": "Uso de algoritmos de Aprendizaje Automático para analizar patrones de comportamiento y datos masivos con el fin de identificar anomalías sutiles en tiempo real.",
              "descripcion": "Los modelos de IA y ML superaron las limitaciones de las reglas fijas. Son capaces de procesar la hora, ubicación, monto y comportamiento histórico del usuario para detectar transacciones que se desvían de la norma.",
              "figura_clave": "Científicos de datos y equipos de riesgo bancario.",
              "imagen_url": base_url + "timeline4.png"
          },
          5: {
              "año": "Presente",
              "nombre": "Detección de Huellas Digitales de Dispositivos (Device Fingerprinting)",
              "concepto": "Creación de un identificador único y persistente de un dispositivo basado en sus características técnicas para evaluar su nivel de confianza.",
              "descripcion": "Esta tecnología recopila cientos de parámetros técnicos para crear una 'huella' que persiste, siendo crítica para combatir el fraude CNP.",
              "figura_clave": "Empresas de ciberseguridad y plataformas antifraude.",
              "imagen_url": base_url + "timeline5.png"
          }
    }

    opcion = st.slider(
        "Selecciona un punto del timeline",
        min_value=1,
        max_value=5,
        value=1,
        step=1,
        format="HITO N° %d"
    )

    st.markdown("---")

    data_hito = hitos[opcion]
    col1, col2 = st.columns([1, 2.5])

    with col1:
        st.header(data_hito["año"])
        st.image(data_hito["imagen_url"], caption=data_hito["nombre"], use_column_width=True)

    with col2:
        st.subheader(f":lock: {data_hito['nombre']}")
        st.caption(f"**Concepto Central:** {data_hito['concepto']}")
        st.markdown("---")
        st.write(data_hito["descripcion"])
        st.markdown(f"**🛡️ Actores Clave:** *{data_hito['figura_clave']}*")


def page3():
    st.title("Análisis Exploratorio de Datos (EDA) 🔍")
    st.markdown("---")

    # 🔑 CORRECCIÓN CLAVE: Llama a load_data() aquí para definir df localmente
    df = load_data() 
    
    if df.empty:
        # Se detiene si la carga falla
        return

    st.header("1. Estructura y Resumen del Dataset")

    col_shape, col_info = st.columns(2)
    
    with col_shape:
        st.subheader("Dimensiones")
        st.info(f"**Filas (Observaciones):** {df.shape[0]:,}")
        st.info(f"**Columns (Features):** {df.shape[1]:,}")
        st.markdown("---")
        st.subheader("Primeras 5 Filas")
        st.dataframe(df.head())

    with col_info:
        st.subheader("Tipos de Datos y Nulos")
        buffer = pd.io.common.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
        
        null_counts = df.isnull().sum()
        if null_counts.sum() > 0:
            st.error("⚠️ Se detectaron valores nulos. Requiere limpieza.")
            st.dataframe(null_counts[null_counts > 0].to_frame('Valores Nulos'))
        else:
            st.success("✅ ¡No se detectaron valores nulos!")

    st.markdown("---")

    st.header("2. Análisis de la Variable Objetivo (`Fraud_Label`)")
    st.write("En la detección de fraude, es crucial analizar el **desbalance** de la clase.")

    col_count, col_dist = st.columns(2)
    
    with col_count:
        st.subheader("Recuento de Clases")
        value_counts = df["Fraud_Label"].value_counts().rename({0: "No Fraude", 1: "Fraude"})
        st.dataframe(value_counts.to_frame())
        
        total = df.shape[0]
        fraude_count = value_counts.loc["Fraude"]
        fraude_ratio = (fraude_count / total) * 100
        
        st.warning(f"🚨 **Ratio de Fraude:** Solo el **{fraude_ratio:.2f}%** de las transacciones son fraudulentas. Esto es un problema de **Desbalance de Clases**.")

    with col_dist:
        st.subheader("Visualización de Desbalance")
        fig, ax = plt.subplots()
        # Gráfico de barras con colores distintivos
        sns.countplot(x='Fraud_Label', data=df, ax=ax, palette=['#4CAF50', '#FF5722']) 
        ax.set_title("Distribución de Transacciones (0=No Fraude, 1=Fraude)")
        ax.set_xlabel("Fraud_Label")
        ax.set_ylabel("Frecuencia")
        st.pyplot(fig)
        

    st.markdown("---")

    st.header("3. Matriz de Correlación")
    st.write("Identifica las relaciones entre variables numéricas y su impacto en el fraude.")

    numerical_df = df.select_dtypes(include=np.number)
    corr_matrix = numerical_df.corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    # Matriz de correlación con anotaciones y mapa de calor
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax, linewidths=.5, linecolor='black')
    ax.set_title('Matriz de Correlación de Variables')
    st.pyplot(fig)


def page4():
    st.title("Modelos de Machine Learning 🤖")
    st.markdown("---")
    st.info("Esta sección será implementada para la fase de modelado y despliegue de los algoritmos de detección de fraude.")


############################# NAVEGACIÓN PRINCIPAL ##############################

page_names_to_funcs = {
    "Introducción": page1,
    "Timelime": page2,
    "EDA": page3, # Aquí se cargará la página con el EDA corregido
    "Modelos": page4
}

selected_page = st.sidebar.selectbox("Selecciona una Sección", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
