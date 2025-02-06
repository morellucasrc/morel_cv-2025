import qrcode 

import streamlit as st


st.title("BIENVENIDO AL GENERADOR DE QR ")

filename = "C:/Users/ignac/Desktop/Nueva carpeta/streamlit/paginas/.streamlit/qr_code.png"

def generador_qr(url,filename):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=100,
        border=5,
    )

    qr.add_data(url)
    qr.make(fit=True)

    imagen= qr.make_image(fill_color = "black", back_color= "white")
    imagen.save(filename)

url=st.text_input("ingresar la URL")

if st.button("Generar QR"):
    generador_qr(url, filename)
    st.image(filename,use_column_width=True)
    with open (filename,"rb")as f:
                    image_data = f.read()
    descarga = st.download_button(label="descarga QR", data=image_data,file_name="QR_generador.png",)                