from pytube import YouTube, Playlist
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
def download_audio():
    audio = YouTube.streams.filter(only_audio=True)[0]
    audio.download()
def download_playlist():
    PLAYLIST_URL =YouTube(url)
    playlist = Playlist(PLAYLIST_URL)
    for url in playlist:
    video= YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path='playlist')
    
def menu():
    print("PYTUBE DOWNLOADER")
    print("1-Download de Videos")
    print("2-Download de Playlist")
    print ("3-Download do audio")
    opc=input("Insira a opção desejada:")
    return opc


def main():
    ops=menu()