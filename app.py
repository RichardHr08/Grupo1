
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib
import pickle # Necesario para cargar el archivo .pkl
import lightgbm as lgb # Necesario para que el modelo cargado funcione
# Si usas scikit-learn para transformaciones, también impórtalo:
# from sklearn.preprocessing import StandardScaler 

# Configurar el estilo de gráficos para un mejor look en Streamlit
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 150




# ---------------------------------------------
# 1. FUNCIÓN DE CARGA DE DATOS (Se mantiene)
# ---------------------------------------------
@st.cache_data
def load_data():
    """Carga el dataset desde GitHub y lo almacena en caché."""
    DATA_URL = "https://raw.githubusercontent.com/bssanchezlopez/Grupo_1/refs/heads/main/synthetic_fraud_dataset.csv"
    try:
        df = pd.read_csv(DATA_URL)
        return df
    except Exception as e:
        st.error(f"Error al cargar el dataset desde GitHub. Verifica la URL: {e}")
        return pd.DataFrame() 

# ---------------------------------------------
# 2. FUNCIÓN DE CARGA DEL MODELO (NUEVA)
# ---------------------------------------------
@st.cache_resource # Usar st.cache_resource para objetos grandes como modelos
def load_model():
    """Carga el modelo LGBMClassifier.pkl desde GitHub o localmente."""
    # RUTA DONDE SE ENCUENTRA TU MODELO EN EL REPOSITORIO DE GITHUB
    MODEL_URL = "https://raw.githubusercontent.com/bssanchezlopez/Grupo_1/main/modelo_LGBMClassifier.pkl"
    
    try:
        # Intenta cargar el modelo directamente desde la URL (si es compatible)
        # O MEJOR, asegúrate de que el modelo esté en la misma carpeta o usa un script para descargar
        
        # --- Estrategia más robusta para Streamlit/GitHub ---
        # 1. Intenta cargar el archivo localmente si está presente (para entorno Streamlit Cloud)
        model_path = 'modelo_LGBMClassifier.pkl'
        
        # En un despliegue de Streamlit Cloud, el archivo debe estar en el repositorio.
        with open(model_path, 'rb') as file:
            model = joblib.load(file)
        
        return model
        
    except FileNotFoundError:
        st.error(f"Error: El archivo '{model_path}' no se encontró en el repositorio.")
        st.info("Asegúrate de que el archivo 'modelo_LGBMClassifier.pkl' esté subido a la raíz de tu repositorio de GitHub.")
        return None
    except Exception as e:
        st.error(f"Error al cargar el modelo LGBM. Asegúrate de tener importada la librería 'lightgbm'. Detalle: {e}")
        return None


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

    # 🔑 CARGA DE DATOS: Llama a load_data() para definir df localmente
    df = load_data() 
    
    if df.empty:
        # Se detiene si la carga falla
        return
        
    # --- ANÁLISIS DEL DATASET ---

    st.header("1. Información General del Dataset")
    
    # 1.1 Dimensiones y Target
    col_dim, col_target, col_types = st.columns(3)

    with col_dim:
        st.subheader("Dimensiones")
        st.info(f"**Filas (Observaciones):** {df.shape[0]:,}")
        st.info(f"**Columnas (Features):** {df.shape[1]:,}")

    with col_target:
        # Cuál es el target?
        st.subheader("Variable Target")
        st.success("🎯 **'Fraud_Label'**")
        st.write("Es una variable binaria: `1` (Fraude), `0` (No Fraude).")

    with col_types:
        # 1.2 Tipos de Datos
        st.subheader("Tipos de Datos")
        # Qué tipos de datos son?
        st.dataframe(df.dtypes.to_frame(name='Tipo de Dato'))

    st.markdown("---")
    
    # 1.3 Datos Faltantes
    st.header("2. Calidad de Datos (Valores Faltantes)")
    # Hay datos faltantes?
    null_counts = df.isnull().sum().sort_values(ascending=False)
    null_counts = null_counts[null_counts > 0]
    
    if null_counts.sum() > 0:
        st.error("⚠️ Se detectaron valores nulos. Requiere limpieza.")
        st.dataframe(null_counts.to_frame('Valores Nulos'))
    else:
        st.success("✅ ¡No se detectaron valores nulos en el dataset!")

    st.markdown("---")

    # --- 3. ANÁLISIS DE OUTLIERS (DATOS FUERA DE SERIE) ---
    st.header("3. Detección de Outliers (Datos Fuera de Serie)")
    st.write("Se utiliza el método del **Rango Intercuartílico (IQR)** para identificar transacciones atípicas.")

    # 1. Identificar columnas numéricas (excluyendo la binaria Fraud_Label y posiblemente Step/ID si son tratadas como índices)
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    # Excluir etiquetas binarias o IDs que no tienen sentido buscar outliers
    cols_to_exclude = ['Fraud_Label', 'IP_Address_Flag', 'Previous_Fraudulent_Activity', 'CustomerID', 'TransactionID']
    num_cols = [col for col in num_cols if col not in cols_to_exclude]
    
    st.info(f"Analizando las columnas: {', '.join(num_cols)}")

    # 2. Función para encontrar outliers por IQR
    def detectar_outliers_iqr(data_frame, col):
        Q1 = data_frame[col].quantile(0.25)
        Q3 = data_frame[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        return data_frame[(data_frame[col] < lower) | (data_frame[col] > upper)]

    # 3. Detectar outliers en cada columna numérica
    outliers_total = pd.DataFrame()
    outlier_summary = {}

    for col in num_cols:
        outliers_col = detectar_outliers_iqr(df, col)
        if not outliers_col.empty:
            outliers_total = pd.concat([outliers_total, outliers_col])
            outlier_summary[col] = outliers_col.shape[0]

    # Presentar resultados
    if not outliers_total.empty:
        total_outliers = outliers_total.drop_duplicates().shape[0]
        st.warning(f"🚨 **Outliers Detectados:** Se encontraron **{total_outliers}** filas con valores fuera de serie.")
        
        st.subheader("Resumen de Outliers por Columna")
        st.dataframe(pd.Series(outlier_summary).to_frame('Cantidad de Outliers'))
        
        # Mostrar el boxplot de las columnas con outliers para visualización
        st.subheader("Visualización de Outliers (Boxplots)")
        cols_with_outliers = list(outlier_summary.keys())
        
        num_plots = len(cols_with_outliers)
        
        # Ajustamos el tamaño de la figura automáticamente
        fig, axes = plt.subplots(ncols=1, nrows=num_plots, figsize=(8, 4 * num_plots))
        
        # Manejar el caso de un solo gráfico
        if num_plots == 1:
            axes = [axes]

        for i, col in enumerate(cols_with_outliers):
            sns.boxplot(x=df[col], ax=axes[i], color='#3498DB')
            axes[i].set_title(f'Outliers en {col}')
            
        plt.tight_layout()
        st.pyplot(fig)
        #  <- ESTABA AQUÍ Y LO COMENTO
        
    else:
        st.success("✅ No se detectaron outliers significativos mediante el método IQR en las columnas seleccionadas.")

    st.markdown("---")

    # --- 4. ANÁLISIS DE LA VARIABLE OBJETIVO ---
    st.header("4. Análisis de la Variable Objetivo (`Fraud_Label`)")
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
        sns.countplot(x='Fraud_Label', data=df, ax=ax, palette=['#4CAF50', '#FF5722'])
        ax.set_title("Distribución de Transacciones (0=No Fraude, 1=Fraude)")
        ax.set_xlabel("Fraud_Label")
        ax.set_ylabel("Frecuencia")
        st.pyplot(fig)
        

    st.markdown("---")

    # --- 5. MATRIZ DE CORRELACIÓN ---
    st.header("5. Matriz de Correlación")
    st.write("Identifica las relaciones entre variables numéricas y su impacto en el fraude.")

    numerical_df = df.select_dtypes(include=np.number)
    corr_matrix = numerical_df.corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax, linewidths=.5, linecolor='black')
    ax.set_title('Matriz de Correlación de Variables')
    st.pyplot(fig)
    #  <- ESTABA AQUÍ Y LO COMENTO   

# --- 6. DIAGRAMA DE PARES (PAIRPLOT) ---
    st.header("6. Relación Bivariada (Pairplot) 📊")
    st.write("El **Diagrama de Pares** muestra las distribuciones y relaciones entre las variables clave. La clase **Fraude (Rojo)** ayuda a identificar si existe alguna **separación lineal**.")

    # Variables que se ven en la imagen de ejemplo:
    features_subset = ['Transaction_Amount', 'Account_Balance', 'IP_Address_Flag', 
                       'Previous_Fraudulent_Activity', 'Daily_Transaction_Count', 'Fraud_Label']

    df_pairplot = df[features_subset]

    # Creamos el Pairplot
    try:
        # Usamos hue='Fraud_Label' para colorear por la clase objetivo
        fig_pairplot = sns.pairplot(
            df_pairplot, 
            hue='Fraud_Label', 
            diag_kind='kde', # Muestra la densidad en la diagonal
            palette={0: 'green', 1: 'red'} # Definimos los colores Fraude y No Fraude
        )
        plt.suptitle("Relación Bivariada y Distribución (Fraude vs. No Fraude)", y=1.02)
        
        # Mostramos el gráfico
        st.pyplot(fig_pairplot)
        
    except Exception as e:
        st.warning(f"No se pudo generar el Diagrama de Pares. Asegúrate de tener las columnas correctas. (Excepción: {e})")
        
    st.markdown("---")
    st.write("Para el procesamiento de los datos la columna Timestamp se debe convertir en tipo de datos fecha ademas los tipo object en numerico de ser necesario.")


def page4():
    st.title("Modelos de Machine Learning 🤖 | Predicción de Fraude")
    st.markdown("---")
    
    # Cargar el modelo
    model = load_model()
    
    if model is None:
        st.error("No se pudo cargar el modelo de Machine Learning. Revise los errores anteriores.")
        return
        
    st.success("✅ Modelo LightGBM (LGBMClassifier) cargado exitosamente.")
    st.write("Utiliza el panel de la izquierda para ingresar los datos de la transacción y predecir la probabilidad de fraude.")
    
    # -----------------------------------------------------------
    # 1. OBTENER INPUTS DEL USUARIO (AJUSTA ESTAS COLUMNAS SEGÚN LAS QUE USA TU MODELO)
    # -----------------------------------------------------------
    
    st.sidebar.header("Parámetros de la Transacción")

    # Ejemplo de entradas numéricas
    transaction_amount = st.sidebar.number_input("Monto de Transacción", min_value=0.0, max_value=5000.0, value=500.0)
    account_balance = st.sidebar.number_input("Saldo de Cuenta", min_value=0.0, max_value=100000.0, value=15000.0)
    daily_count = st.sidebar.slider("Conteo Diario de Transacciones", min_value=1, max_value=50, value=5)
    
    # Ejemplo de entradas categóricas/binarias
    prev_fraud = st.sidebar.selectbox("Actividad Fraudulenta Previa", options=[0, 1], format_func=lambda x: 'Sí' if x == 1 else 'No')
    ip_flag = st.sidebar.selectbox("Bandera de Dirección IP", options=[0, 1], format_func=lambda x: 'IP de Alto Riesgo' if x == 1 else 'IP Segura')
    
    # Crear el DataFrame de entrada (Asegúrate de que los nombres coincidan exactamente con el entrenamiento)
    # ¡IMPORTANTE! Reemplaza estas con las columnas exactas que usa tu modelo LightGBM.
    input_data = pd.DataFrame([[
        transaction_amount, 
        account_balance, 
        ip_flag, 
        prev_fraud, 
        daily_count
    ]], 
    columns=[
        'Transaction_Amount', 
        'Account_Balance', 
        'IP_Address_Flag', 
        'Previous_Fraudulent_Activity', 
        'Daily_Transaction_Count'
    ])
    
    # -----------------------------------------------------------
    # 2. PREDICCIÓN
    # -----------------------------------------------------------
    st.subheader("Datos Ingresados")
    st.dataframe(input_data)
    
    if st.button("PREDECIR PROBABILIDAD DE FRAUDE"):
        
        try:
            # Si tu modelo requiere un preprocesamiento (ej. escalado), aplícalo aquí.
            # pred_input = scaler.transform(input_data) # Si usaste un StandardScaler
            
            # Predecir probabilidad (clase 1 = Fraude)
            prob_fraude = model.predict_proba(input_data)[:, 1][0] * 100
            
            st.markdown("---")
            st.subheader(f"Resultado de la Predicción")
            
            # Mostrar resultado basado en la probabilidad
            if prob_fraude >= 50: # Umbral de decisión
                st.error(f"❌ ¡ALERTA DE FRAUDE! Probabilidad: {prob_fraude:.2f}%")
                st.balloons()
            elif prob_fraude >= 10:
                 st.warning(f"⚠️ RIESGO MODERADO. Probabilidad: {prob_fraude:.2f}%")
            else:
                st.success(f"✅ Transacción SEGURA. Probabilidad de Fraude: {prob_fraude:.2f}%")
                
            st.progress(prob_fraude / 100, text=f"Nivel de Riesgo ({prob_fraude:.2f}%)")
            
            
        except Exception as e:
            st.error(f"Error al realizar la predicción. Asegúrate de que los datos de entrada coincidan con el entrenamiento del modelo. Detalle: {e}")


# El resto de tu código (page1, page2, page3, configuración inicial y navegación) se mantiene igual.
# Asegúrate de reemplazar la definición original de page4 con esta nueva función.


############################# NAVEGACIÓN PRINCIPAL ##############################

page_names_to_funcs = {
    "Introducción": page1,
    "Timelime": page2,
    "EDA": page3, # Aquí se cargará la página con el EDA corregido
    "Modelos": page4
}

selected_page = st.sidebar.selectbox("Selecciona una Sección", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
