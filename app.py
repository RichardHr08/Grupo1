import streamlit as st
import os


############################# CONFIGURACIÓN INICIAL ##############################

# Configuración global para todas las páginas
st.set_page_config(page_title="Detección de Fraude | ISIL", layout="wide")

# Rutas de las imágenes
# Intenta cargar la imagen del logo. Primero busca en la raíz, luego en una carpeta 'assets'.
# DEBES subir el archivo 'ISIL.png' a la ubicación correcta en tu repositorio de GitHub.
ISIL_LOGO_PATHS = ["ISIL.png", "assets/ISIL.png", "images/ISIL.png"]
loaded = False

for path in ISIL_LOGO_PATHS:
    try:
        # Intenta cargar la imagen del logo en la barra lateral
        st.sidebar.image(path, caption="Grupo #1")
        # 2. Muestra la lista de integrantes como texto
         # st.sidebar.markdown("---")
         # st.sidebar.subheader("Integrantes:")
         # st.sidebar.write("- Herwuin Huaman")
         # st.sidebar.write("- Adrian Ticona")
         # st.sidebar.write("- Brenda Sanches")
         # st.sidebar.write("- Gerson Manosalva")
         # st.sidebar.markdown("---")

        
        loaded = True
        break
    except FileNotFoundError:
        continue

if not loaded:
    # Mensaje de error si la imagen no se encuentra después de todos los intentos
    st.sidebar.error(
        f"Error: Archivo 'ISIL.png' no encontrado. Asegúrate de subirlo a la raíz, '/assets/' o '/images/' en tu repositorio."
    )

#############################Pagina 1############################## 

############################# Pagina 1 ############################## 
def page1():
    st.title("Detección de Transacciones Fraudulentas")
    st.markdown("---")

    # INTRODUCCIÓN
    st.write("La Frontera Digital de la Seguridad Financiera")

    st.markdown("""
    En la era del comercio electrónico y la banca digital, la **Detección de Operaciones Fraudulentas** 
    se ha convertido en una disciplina crítica para proteger tanto a las instituciones financieras 
    como a los consumidores.

    Este proyecto explora la evolución de los sistemas antifraude, desde los primeros modelos 
    estadísticos basados en reglas fijas hasta la aplicación actual de la Inteligencia Artificial 
    y el Aprendizaje Profundo (*Deep Learning*).

    Analizaremos cómo los hitos tecnológicos han redefinido la batalla contra el crimen financiero, 
    permitiendo la identificación de patrones de riesgo sutiles y la prevención en tiempo real.
    """)


#############################Pagina 2############################## 
def page2(): 
  st.set_page_config(page_title="Detección de Fraude | ISIL", layout="wide") 
  
  st.title("Detección de Transacciones Fraudulentas | Línea de Tiempo de Hitos Clave")
  st.markdown("---")
  # Autor actualizado según la solicitud del usuario
  st.write("Autor: GRUPO 1 | ISIL") 
  st.write("Explora los 5 eventos tecnológicos que transformaron la lucha contra el fraude bancario, desde la modelización estadística hasta la inteligencia artificial en tiempo real.")
  st.markdown("---")
  
  # --- URLs y Definición de Hitos con Información Ampliada ---
  
  # Se usa la URL de GitHub proporcionada por el usuario
  base_url = "https://raw.githubusercontent.com/adrianticonatapia-debug/timeline_s1/main/timeline_images/"
  
  hitos = {
      1: {
          "año": "Finales del S. XX",
          "nombre": "Sistemas de Puntuación de Riesgo (FICO)",
          "concepto": "Implementación de modelos estadísticos para asignar una puntuación de riesgo a individuos, sentando las bases de la detección predictiva.",
          "descripcion": "El desarrollo de modelos como el FICO Score introdujo la metodología de usar datos históricos y algoritmos para evaluar el riesgo en tiempo real. Aunque inicialmente se centró en la solvencia crediticia, el concepto fue adaptado rápidamente para identificar comportamientos anómalos en transacciones bancarias, migrando de reglas fijas a modelos predictivos.",
          "figura_clave": "Fair Isaac Corporation (FICO) y pioneros de la estadística.",
          "imagen_url": base_url + "timeline1.png"
      },
      2: {
          "año": "Inicios del 2000",
          "nombre": "Autenticación de Doble Factor (2FA)",
          "concepto": "Requerir dos o más factores de verificación (algo que se sabe, algo que se tiene) para el acceso a cuentas y la ejecución de transacciones.",
          "descripcion": "Este desarrollo cambió el enfoque de la detección a la prevención activa. Al exigir un segundo código de verificación (a menudo enviado al móvil del usuario), se hizo mucho más difícil para los defraudadores realizar un 'Account Takeover' (ATO) o completar transacciones no autorizadas, incluso si habían robado la contraseña principal.",
          "figura_clave": "Pioneros de la seguridad en banca online y SMS/Token.",
          "imagen_url": base_url + "timeline2.png"
      },
      3: {
          "año": "2000 - 2015",
          "nombre": "Adopción Global del Chip EMV",
          "concepto": "Transición de la banda magnética fácilmente clonable a tarjetas con un chip que genera un código criptográfico único para cada transacción.",
          "descripcion": "El chip EMV (Europay, Mastercard, Visa) eliminó casi por completo el fraude físico por clonación ('skimming') en el punto de venta. Este éxito tuvo el efecto secundario de forzar a los criminales a migrar sus esfuerzos hacia las transacciones 'Card-Not-Present' (CNP), como las compras en línea, acelerando la necesidad de soluciones avanzadas en el comercio electrónico.",
          "figura_clave": "Consorcio EMV (Europay, Mastercard, Visa).",
          "imagen_url": base_url + "timeline3.png"
      },
      4: {
          "año": "Década de 2010",
          "nombre": "El Auge de Machine Learning (ML) y Deep Learning (DL)",
          "concepto": "Uso de algoritmos de Aprendizaje Automático para analizar patrones de comportamiento y datos masivos con el fin de identificar anomalías sutiles en tiempo real.",
          "descripcion": "Los modelos de IA y ML superaron las limitaciones de las reglas fijas. Son capaces de procesar la hora, ubicación, monto, producto y comportamiento histórico del usuario para detectar transacciones que se desvían de la norma con una precisión mucho mayor, reduciendo drásticamente tanto el fraude como los falsos positivos.",
          "figura_clave": "Científicos de datos y equipos de riesgo bancario.",
          "imagen_url": base_url + "timeline4.png"
      },
      5: {
          "año": "Presente",
          "nombre": "Detección de Huellas Digitales de Dispositivos (Device Fingerprinting)",
          "concepto": "Creación de un identificador único y persistente de un dispositivo basado en sus características técnicas para evaluar su nivel de confianza.",
          "descripcion": "Esta tecnología recopila cientos de parámetros técnicos (tipo de fuente, resolución, OS, etc.) para crear una 'huella' que persiste incluso si el usuario borra cookies o cambia de IP. Es una herramienta crítica para combatir el fraude CNP y de 'mulas de dinero' al identificar instantáneamente si un dispositivo es sospechoso o si ha sido visto en transacciones fraudulentas previas.",
          "figura_clave": "Empresas de ciberseguridad y plataformas antifraude.",
          "imagen_url": base_url + "timeline5.png"
      }
  }
  
  # --- Interfaz de Streamlit ---
  
  # Slider para seleccionar el hito
  opcion = st.slider(
      "Selecciona un punto del timeline",
      min_value=1,
      max_value=5,
      value=1,
      step=1,
      format="HITO N° %d" # Formato para mejor estética
  )
  
  st.markdown("---")
  
  # Obtener los datos del hito seleccionado
  data_hito = hitos[opcion]
  
  # Uso de columnas para una mejor estética (Imagen a la izquierda, Texto a la derecha)
  col1, col2 = st.columns([1, 2.5])
  
  with col1:
      # Muestra el año/periodo de manera destacada
      st.header(data_hito["año"])
      
      # Mostrar la imagen
      st.image(data_hito["imagen_url"], caption=data_hito["nombre"], use_column_width=True)
  
  with col2:
      # Título y Subtítulo
      st.subheader(f":lock: {data_hito['nombre']}")
      st.caption(f"**Concepto Central:** {data_hito['concepto']}")
  
      # Información detallada
      st.markdown("---")
      st.write(data_hito["descripcion"])
      
      # Figura clave destacada
      st.markdown(f"**🛡️ Actores Clave:** *{data_hito['figura_clave']}*")

############################# Pagina 3 ############################## 

def page3():
  st.title("Pendiente")


############################# Pagina 4 ############################## 

def page4():
  st.title("Pendiente")

############################# Pagina 5 ############################## 

def page4():
  st.title("Pendiente")
  
page_names_to_funcs = {
  "Introducción": page1,
  "Timelime": page2,
  "EDA": page3,
  "Modelos": page4,
  "Modelos": page5
  }

  
selected_page = st.sidebar.selectbox("Selecciona", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
