import os
import random
import string

import cv2
from pytube import YouTube

def download_youtube_video(url, output_path='video.mp4'):
    # Descargar el video de YouTube
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(filename=output_path)
    print(f'Video descargado: {output_path}')

def generate_random_string(length=8):
    # Generar una cadena aleatoria de longitud especificada
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def extract_frames(video_path, frames_folder,frame_interval=1):
    # Crear la carpeta de frames si no existe
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)

        # Abrir el video
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        saved_frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % frame_interval == 0:
                random_string = generate_random_string()
                frame_filename = os.path.join(frames_folder, f'frame_{saved_frame_count:04d}_{random_string}.jpg')
                cv2.imwrite(frame_filename, frame)
                saved_frame_count += 1
            frame_count += 1

        cap.release()
        print(f'Frames guardados en la carpeta: {frames_folder}')

if __name__ == "__main__":
    youtube_url = 'https://www.youtube.com/shorts/vfNzP7gkaJc'
    video_path = 'video.mp4'
    frames_folder = 'frames/tinku3'
    frame_interval = 4
    # Descargar el video
    download_youtube_video(youtube_url, video_path)

    # Extraer los frames
    extract_frames(video_path, frames_folder,frame_interval)

    #TOBAS
