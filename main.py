import os
import time
from yt_dlp import YoutubeDL

# Función para descargar el archivo de audio mp3
def descargar_audio(url, carpeta_salida):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{carpeta_salida}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Función para leer el archivo de entrada y descargar los archivos
def descargar_desde_archivo(archivo_entrada, carpeta_salida):
    with open(archivo_entrada, 'r') as file:
        for line in file:
            url = line.strip()
            descargar_audio(url, carpeta_salida)
            # Esperar 10 segundos entre descargas
            print("Esperando 10 segundos antes de la próxima descarga...")
            time.sleep(10)
            if url == "":
                print("URL vacía, se omitirá la descarga de esta línea")

            print("Descarga finalizada")

if __name__ == "__main__":
    archivo_entrada = "canciones.txt"
    carpeta_salida = "canciones_descargadas"

    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    descargar_desde_archivo(archivo_entrada, carpeta_salida)
