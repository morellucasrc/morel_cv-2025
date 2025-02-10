import streamlit as st

#import PyPDF2
from PIL import Image
import requests
#from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from pathlib import Path
import pandas as pd

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
st.sidebar.write("Universidad Abierta Interamericana – Analista Programador (En curso)\n\nEspañol (nativo) \n\n Inglés (básico/intermedio)")
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

st.header(" ANALISTA PROGRAMADOR ")

st.write("---")

column_foto , column_info = st.columns(2,gap="medium", vertical_alignment="top")

with column_foto:
    st.image("C:/Users/ignac/Desktop/Nueva carpeta/streamlit/paginas/prueba.png", width=250,)

with column_info:
    st.title("Lucas Ezequiel Morel")

    st.write(""" 📲 : +54 9 11-5972-5559       
                  ✉️ : morellucasrc@gmail.com
                  """)
    



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
    </style>
""", unsafe_allow_html=True)

# Texto con estilos personalizados
st.markdown('<p class="custom-text"> Mi objetivo profesional es iniciar mi carrera en el ámbito de la programación y análisis de sistemas, aprovechando los conocimientos  adquiridos a lo largo de mi formación académica en la Universidad  Abierta Interamericana. Estoy en búsqueda de mi primera experiencia laboral en una organización que me permita integrarme a un equipo profesional, donde pueda aprender y desarrollar mis habilidades técnicas en   programación, desarrollo de software y resolución de problemas. Aspiro a crecer profesionalmente mediante la aplicación de soluciones tecnológicas eficientes e innovadoras, contribuyendo activamente a proyectos que impulsan la mejora continua y el avance tecnológico de la empresa.      Me motiva el aprendizaje constante, el trabajo en equipo y el compromiso con la excelencia en cada tarea, buscando siempre      aportar valor y adaptarme a los desafíos que el entorno profesional.</p>', unsafe_allow_html=True)

 
st.markdown('<p class="remoto-text"> ¿POR QUE PUEDO TRABAJAR DE FORMA REMOTA?:'
'  Mi formación en la Universidad Abierta Interamericana me ha permitido desarrollar habilidades clave para el trabajo remoto, ya que realicé mi carrera de manera 100%  online, gestionando mi tiempo de forma autónoma y cumpliendo con cada entrega de manera eficiente.'

'Además, me destaco por ser:'
'-✅ Organizado: Planifico mis tareas y establezco prioridades para cumplir con los plazos sin necesidad de supervisión constante.'
'-✅ Responsable: Me comprometo con mis objetivos y mantengo una comunicación fluida con el equipo.'
'-✅ Proactivo: Busco soluciones, me adapto rápidamente a nuevas herramientas y aprendo constantemente para mejorar mi desempeño.'

'Estas habilidades, sumadas a mis conocimientos en programación y análisis de sistemas, me permiten integrarme eficazmente en equipos de trabajo remoto, aportando valor desde cualquier lugar.</p>', unsafe_allow_html=True)
