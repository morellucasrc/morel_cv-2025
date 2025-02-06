import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
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

info_pagina = st.Page(
    page= "C:/Users/ignac/Desktop/Nueva carpeta/streamlit/paginas/info.py",
    title= "Sobre mi",
    icon="👀",
    default= True,
)

proyecto1= st.Page(
    page = "C:/Users/ignac/Desktop/Nueva carpeta/streamlit/paginas/proyecto1.py",
    title="proyecto 1",
    icon="📱",
)

proyecto2 = st.Page(
    page= "C:/Users/ignac/Desktop/Nueva carpeta/streamlit/paginas/proyecto2.py",
    title="proyecto 2",
    icon="🤖"
)

proyecto3 = st.Page(
    page= "C:/Users/ignac/Desktop/Nueva carpeta/streamlit/paginas/proyecto3.py",
    title= "proyecto 3",
    icon= "✉️"

)




#pg = st.navigation(pages=[info_pagina, proyecto1, proyecto2])
pg = st.navigation({
    "info": [info_pagina],
    #"proyectos": [proyecto1,proyecto2,proyecto3]
    
})

st.sidebar.title("Perfil Profesional")
st.sidebar.write("Estudiante de Analista Programador con conocimientos en Python, C#, HTML, CSS, metodologías ágiles y arquitectura de software. Apasionado por la programación y la resolución de problemas. Buscando mi primera experiencia laboral en IT.")
st.sidebar.title(" Educación")
st.sidebar.write("Universidad Abierta Interamericana – Analista Programador (En curso)\n\nEspañol (nativo) \n\n Inglés (básico/intermedio)")
st.sidebar.write("---")
st.sidebar.text("Realizado con streamlit ❤️")

pg.run()
