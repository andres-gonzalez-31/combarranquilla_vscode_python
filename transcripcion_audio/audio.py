import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import which
import os

# Forzar a pydub a usar los ejecutables de ffmpeg y ffprobe
AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")


def transcribir_audio(ruta_audio):
    """
    Convierte un archivo de audio a texto. Soporta formatos MP3, WAV y OPUS.
    """
    temp_wav_file = None  # aseguramos que exista la variable
    try:
        # Crea un objeto Recognizer
        r = sr.Recognizer()
        
        # Carga el archivo de audio con pydub
        audio = AudioSegment.from_file(ruta_audio)
        
        # Crea un archivo WAV temporal para la transcripción
        temp_wav_file = "temp_audio.wav"
        audio.export(temp_wav_file, format="wav")

        # Abre el archivo WAV temporal
        with sr.AudioFile(temp_wav_file) as source:
            audio_data = r.record(source)
            
            # Transcribe el audio a texto usando la API de Google
            texto = r.recognize_google(audio_data, language="es-ES")
            return texto

    except sr.UnknownValueError:
        return "No se pudo entender el audio."
    except sr.RequestError as e:
        return f"Error en la solicitud a la API de Google: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"
    finally:
        # Asegura que el archivo temporal se borre si se creó
        if temp_wav_file and os.path.exists(temp_wav_file):
            os.remove(temp_wav_file)


# --- Proceso principal ---

# 1. Coloca aquí la ruta a tu carpeta de audios
carpeta_audios = "audios"  # Carpeta donde están los audios

# 2. Obtiene la lista de archivos de audio en la carpeta
if not os.path.exists(carpeta_audios):
    print(f"Error: La carpeta '{carpeta_audios}' no existe. Por favor, revisa la ruta.")
else:
    archivos_audio = [
        os.path.join(carpeta_audios, f)
        for f in os.listdir(carpeta_audios)
        if f.lower().endswith(('.mp3', '.wav', '.opus'))
    ]
    
    if not archivos_audio:
        print(f"No se encontraron archivos de audio en la carpeta '{carpeta_audios}'.")
    else:
        print("Rutas de los archivos de audio encontrados:")
        for ruta in archivos_audio:
            print(ruta)
        print(f"\nIniciando la transcripción de {len(archivos_audio)} archivos...")
        
        for i, ruta_completa in enumerate(archivos_audio):
            nombre_archivo = os.path.basename(ruta_completa)
            print(f"\n--- Procesando archivo {i+1}: {nombre_archivo} ---")
            
            texto_transcrito = transcribir_audio(ruta_completa)
            
            print("Resultado de la transcripción:")
            print(texto_transcrito)
            print("---------------------------------------")
            
            # Guarda la transcripción en un archivo de texto
            carpeta_transcripciones = "transcripciones"
            if not os.path.exists(carpeta_transcripciones):
                os.makedirs(carpeta_transcripciones)
            nombre_txt = os.path.splitext(nombre_archivo)[0] + ".txt"
            ruta_txt = os.path.join(carpeta_transcripciones, nombre_txt)
            with open(ruta_txt, "w", encoding="utf-8") as f:
                f.write(texto_transcrito)
            print(f"Transcripción guardada en: {ruta_txt}")
