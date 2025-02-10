import streamlit as st
import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
#OPEN_AI_KEY="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"

load_dotenv(find_dotenv(),override=True)

apikey = os.environ.get('OPEN_AI_KEY')

cliente = OpenAI(api_key=  apikey)

la_voz = ["alloy", "nova"]

st.title ("Bienvenido al generador de audio ")

texto = st.text_area("ingrese algun texto:", height= 200)

voces = st.selectbox("seleccionar la voz:", la_voz)


if st.button( "GENERAR "):
    if texto:
        respuesta = cliente.audio.speech.create(
            model= "tts-1",
            voice= la_voz,
            input=texto,
        )
        audio_path = "audio.mp3"
        with open(audio_path,'wb')as output_file:
            for chnk in respuesta.iter_bytes():
                if chnk :
                    output_file.write(chnk)

        st.success("AUDIO GENERADO Y GUARDADO")            


        audio_file =open(audio_path,'rb')
        audio_byte = audio_file.read()
        st.audio(audio_byte,format="audio/mp3")

    