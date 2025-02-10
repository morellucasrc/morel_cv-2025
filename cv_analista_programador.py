import streamlit as st

#import PyPDF2
from PIL import Image
import requests
#from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from pathlib import Path
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import io
import os 

page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
background-size: 4px 45px;
background: rgb(0,0,0);
background: rgb(14,17,23);
background: linear-gradient(90deg, rgba(14,17,23,1) 0%, rgba(26,134,156,1) 4%, rgba(14,17,23,1) 42%);


</style>


"""






st.markdown(
        """
        <style>
@font-face {
  <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
  
}

    html, body,write, [class*="css"]  {
    font-family: "Poppins", serif;;
    font-size: 13px;
    padding:0px;
    margin:0px

    }
    </style>

    """,
        unsafe_allow_html=True,
    )

st.markdown(page_bg_img,unsafe_allow_html=True)


st.sidebar.title("Perfil Profesional")
st.sidebar.write("Estudiante de Analista Programador con conocimientos en Python, C#, HTML, CSS, metodologías ágiles y arquitectura de software. Apasionado por la programación y la resolución de problemas. Buscando mi primera experiencia laboral en IT.")
st.sidebar.title(" Educación")
st.sidebar.write("Universidad Abierta Interamericana – Analista Programador (En curso) \n\n Inglés: básico/intermedio( En curso)")
st.sidebar.write("---")
st.sidebar.text("Realizado con streamlit ❤️")



import streamlit as st
import requests
from streamlit_lottie import st_lottie



def load_lottieurl( url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json ()   

#url = load_lottieurl("https://lottie.host/62a12eb9-1c97-4fe6-9e16-5ec76eb273ba/aQX8Sbl9qi.json")
#st_lottie(url)

st.markdown('<p class= "titulo"> ANALISTA PROGRAMADOR ',unsafe_allow_html=True)



column_foto , column_info = st.columns(2,gap="medium", vertical_alignment="top")

with column_foto:
    st.image("paginas/prueba.png", width=250,)

with column_info:
    st.title("Lucas Morel")

    st.write(""" 📲 : +54 9 11-5972-5559       
                  ✉️ : morellucasrc@gmail.com
                  """)
    st.link_button("Ir a mi linkedin", "https://www.linkedin.com/in/lucas-morel-15a03b4423120112172020b")



st.write("\n\n---\n\n")


column_lenguajes , column_habilidades = st.columns(2, gap= "small", vertical_alignment=  "bottom")
st.write("\n")
st.write("---")




with column_lenguajes:
   st.header("Habilidades")
   st.write("""  \n ※ PYTHON \n\n※ HTML \n\n※ CSS \n\n※
    C# \n\n※ VISUAL STUDIO CORE \n\n※ JAVASCRIPT  \n\n""")
   st.write("""※ARQUITECTURA DE
SOFTWARE \n\n
※DESARROLLO DE
SISTEMAS\n\n
※METODOLOGIAS AGILES\n""")

with column_habilidades:

  url = load_lottieurl("https://lottie.host/62a12eb9-1c97-4fe6-9e16-5ec76eb273ba/aQX8Sbl9qi.json")
  st_lottie(url)

   



st.markdown("""
    <style>
    
@import url('https://fonts.googleapis.com/css2?family=42dot+Sans:wght@300..800&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    
    .custom-text {
        font-family: "Poppins", serif;
        font-size: 20px;
        color:#f8f9f9;
        text-align: center;
        border-style: double;
        padding: 40px;
            -webkit-box-shadow: 32px -27px 151px -7px rgba(111,188,189,1);
-moz-box-shadow: 32px -27px 151px -7px rgba(111,188,189,1);
box-shadow: 32px -27px 151px -7px rgba(111,188,189,1);
Copiar texto
    }
 .remoto-text {
        font-family: "Poppins", serif;
        font-size: 20px;
        color:#f8f9f9;
        text-align: center;
        border-style: double;
        padding: 40px;
            -webkit-box-shadow: 32px -27px 151px -7px rgba(111,188,189,1);
-moz-box-shadow: 32px -27px 151px -7px rgba(111,188,189,1);
box-shadow: 32px -27px 151px -7px rgba(111,188,189,1);
Copiar texto
    }  

 .proyecto-empleados{
            font-family: "Poppins", serif;
            font-size: 20px;
            padding: 40px;
            border-style: double;
            
            }
  .titulo{
        
    font-size: 100px; 
    color: #2C3E50; 
    text-transform: uppercase;
    letter-spacing: 2px;
    text-align: center;
    padding: 12px 0;
    border-bottom: 2px solid #16A085; 
    font-family: 'Arial', sans-serif;

            }          
            
                                           
    </style>
""", unsafe_allow_html=True)

# Texto con estilos personalizados
st.markdown('<p class="custom-text"> Mi objetivo profesional es iniciar mi carrera en el ámbito de la programación y análisis de sistemas, aprovechando los conocimientos  adquiridos a lo largo de mi formación académica en la Universidad  Abierta Interamericana.<br> Estoy en búsqueda de mi primera experiencia laboral en una organización que me permita integrarme a un equipo profesional, donde pueda aprender y desarrollar mis habilidades técnicas en   programación, desarrollo de software y resolución de problemas.<br> </p>', unsafe_allow_html=True)

 
st.markdown('<p class="remoto-text"> ¿POR QUE PUEDO TRABAJAR DE FORMA REMOTA?:'
' <br> Mi formación en la Universidad Abierta Interamericana me ha permitido desarrollar habilidades clave para el trabajo remoto, ya que realicé mi carrera de manera 100%  online, gestionando mi tiempo de forma autónoma y cumpliendo con cada entrega de manera eficiente.'

'Además, me destaco por ser:'
'<br>-✅ Organizado: Planifico mis tareas y establezco prioridades para cumplir con los plazos sin necesidad de supervisión constante.'
'<br>-✅ Responsable: Me comprometo con mis objetivos y mantengo una comunicación fluida con el equipo.'
'<br>-✅ Proactivo: Busco soluciones, me adapto rápidamente a nuevas herramientas y aprendo constantemente para mejorar mi desempeño.'

'<br>Estas habilidades, sumadas a mis conocimientos en programación y análisis de sistemas, me permiten integrarme eficazmente en equipos de trabajo remoto, aportando valor desde cualquier lugar\n\n.</p>\n\n', unsafe_allow_html=True)

st.header(" \n\n PROYECTO DE GENERADOR DE TABLA Y DESCARGAR EN PDF ")

st.markdown("""<p class= "proyecto-empleados"> Recientemente desarrollé una aplicación interactiva de gestión de empleados, diseñada para facilitar la visualización, edición y adición de datos en tiempo real. Con un enfoque en la eficiencia, utilicé Streamlit para crear una interfaz intuitiva y Pandas para el manejo de datos, permitiendo a los usuarios generar reportes en PDF de manera sencilla. Este proyecto refleja mis habilidades en la creación de soluciones prácticas que mejoran la productividad y organización.

""",unsafe_allow_html=True)

# Función para crear el PDF
def create_pdf(data):
    buffer = io.BytesIO()
    document = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Convertir la data de pandas a una lista de listas para la tabla
    table_data = [['#'] + data.columns.tolist()] + [[i+1] + list(row) for i, row in enumerate(data.values.tolist())]
    
    table = Table(table_data)
    
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0.5, 0.5, 0.5)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0))
    ])

    table.setStyle(style)
    
    document.build([table])

    # Mover el cursor al principio del archivo en el buffer
    buffer.seek(0)
    return buffer

# Cargar datos desde el archivo CSV si existe
def load_data():
    if os.path.exists('empleados.csv'):
        return pd.read_csv('empleados.csv')
    else:
        # Datos por defecto si el archivo no existe
        data = {
            'Nombre': ['Lucas', 'Brenda', 'Juan'],
            'Edad': [29, 30, 25],
            'Puesto': ['Desarrollador', 'Diseñadora', 'Analista'],
            'Salario': [50000.0, 45000.0, 40000.0],
            'Fecha de contratación': ['2020-01-01', '2019-08-15', '2021-03-20'],
            'Departamento': ['TI', 'Diseño', 'Analítica'],
            'Ciudad': ['Buenos Aires', 'CABA', 'Mendoza']
        }
        return pd.DataFrame(data)

# Guardar los datos en un archivo CSV
def save_data(df):
    df.to_csv('empleados.csv', index=False)

# Cargar los datos desde el archivo CSV
st.session_state.df = load_data()

# Mostrar la tabla editable en Streamlit
st.write("tabla de empleados:")

# Modificar las filas de la tabla para que comiencen desde 1
st.session_state.df.index = range(1, len(st.session_state.df) + 1)

# Seleccionar la fila que deseas editar
row_to_edit = st.selectbox("Selecciona una fila para editar", st.session_state.df.index)

# Mostrar campos de entrada para la fila seleccionada
st.session_state.df.at[row_to_edit, 'Nombre'] = st.text_input("Nombre", st.session_state.df.at[row_to_edit, 'Nombre'])
st.session_state.df.at[row_to_edit, 'Edad'] = st.number_input("Edad", value=st.session_state.df.at[row_to_edit, 'Edad'], min_value=0)
st.session_state.df.at[row_to_edit, 'Puesto'] = st.text_input("Puesto", st.session_state.df.at[row_to_edit, 'Puesto'])

# Opción de salario: directamente en pesos argentinos (sin mostrar USD)
salary_in_ars = st.number_input("Salario (Pesos)", value=float(st.session_state.df.at[row_to_edit, 'Salario']), min_value=0.0)
st.session_state.df.at[row_to_edit, 'Salario'] = salary_in_ars  # Actualizamos el salario en ARS

# Cambiar 'Fecha de contratación' a un campo de datetime
st.session_state.df.at[row_to_edit, 'Fecha de contratación'] = st.date_input("Fecha de contratación", pd.to_datetime(st.session_state.df.at[row_to_edit, 'Fecha de contratación']))

# Menú desplegable para seleccionar departamento
departamentos = ['TI', 'Diseño', 'Analítica', 'Marketing', 'Ventas', 'Recursos Humanos']
st.session_state.df.at[row_to_edit, 'Departamento'] = st.selectbox("Departamento", departamentos, index=departamentos.index(st.session_state.df.at[row_to_edit, 'Departamento']))

st.session_state.df.at[row_to_edit, 'Ciudad'] = st.text_input("Ciudad", st.session_state.df.at[row_to_edit, 'Ciudad'])

# Usar un expander para mostrar los campos para agregar una nueva fila
with st.expander("Agregar un nuevo empleado"):
    new_name = st.text_input("Nuevo Nombre")
    new_age = st.number_input("Nueva Edad", min_value=0)
    new_position = st.text_input("Nuevo Puesto")
    new_salary_ars = st.number_input("Nuevo Salario (Pesos)", min_value=0.0)
    
    # Fecha de contratación con un datetime picker
    new_hire_date = st.date_input("Nueva Fecha de contratación")
    
    # Menú desplegable para el nuevo empleado
    new_department = st.selectbox("Nuevo Departamento", departamentos)
    
    new_city = st.text_input("Nueva Ciudad")

    if st.button("Agregar nuevo empleado"):
        if new_name and new_age and new_position and new_salary_ars and new_hire_date and new_department and new_city:
            new_row = pd.DataFrame({
                'Nombre': [new_name],
                'Edad': [new_age],
                'Puesto': [new_position],
                'Salario': [float(new_salary_ars)],  # Aseguramos que el salario sea float
                'Fecha de contratación': [new_hire_date],
                'Departamento': [new_department],
                'Ciudad': [new_city]
            })
            st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)

# Mostrar la tabla editable
st.dataframe(st.session_state.df)

# Guardar los datos cuando se realicen cambios
save_data(st.session_state.df)

# Botón para generar y descargar el PDF
if st.button("Generar PDF"):
    pdf_buffer = create_pdf(st.session_state.df)
    st.download_button(
        label="Descargar PDF",
        data=pdf_buffer,
        file_name="tabla_empleados.pdf",
        mime="application/pdf"
    )
