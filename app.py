from pytube import YouTube
from time import sleep as espere
from os import system as cmd
def download_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path)
        print(f"Vídeo '{yt.title}' baixado com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
url = input("Insira a URL do vídeo: ")   
output_path = input("Digite o caminho de saída (pressione Enter para usar o diretório atual): ")
download_video(url, output_path)

    