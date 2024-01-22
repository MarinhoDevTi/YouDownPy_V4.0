import importlib
import subprocess
import os

# Função para instalar a biblioteca moviepy usando o pip
def install_moviepy():
    try:
        subprocess.check_call(["pip", "install", "--upgrade", "moviepy"])
    except subprocess.CalledProcessError:
        print("Falha ao atualizar a biblioteca moviepy. Verifique sua conexão com a internet e tente novamente.")
        exit()

# Função para desinstalar a biblioteca moviepy usando o pip
def uninstall_moviepy():
    try:
        subprocess.check_call(["pip", "uninstall", "moviepy", "-y"])
    except subprocess.CalledProcessError:
        print("Falha ao desinstalar a biblioteca moviepy. Verifique sua conexão com a internet e tente novamente.")
        exit()

# Verifica se a biblioteca moviepy está instalada e atualiza para a versão mais recente
try:
    importlib.import_module('moviepy')
    # Obter a versão atual do moviepy
    import moviepy
    installed_version = moviepy.__version__

    # Obter a versão mais recente do moviepy disponível no PyPI (repositório Python)
    import requests
    response = requests.get("https://pypi.org/pypi/moviepy/json")
    latest_version = response.json()["info"]["version"]

    # Verifica se a versão instalada é mais antiga que a versão mais recente
    if installed_version != latest_version:
        print(f"Versão atual do moviepy: {installed_version}")
        print(f"Versão mais recente do moviepy: {latest_version}")
        print("Atualizando para a versão mais recente...")

        # Desinstalar a versão antiga do moviepy
        uninstall_moviepy()

        # Instalar a versão mais recente do moviepy
        install_moviepy()
        print("Atualização concluída!")
    else:
        print(f"Você já possui a versão mais recente do moviepy ({latest_version}).")
except ImportError:
    print("A biblioteca moviepy não está instalada. Vamos instalar para você...")
    install_moviepy()
    
from moviepy.editor import *



# Função para instalar a biblioteca pytube usando o pip
def install_pytube():
    try:
        subprocess.check_call(["pip", "install", "--upgrade", "pytube"])
    except subprocess.CalledProcessError:
        print("Falha ao atualizar a biblioteca pytube. Verifique sua conexão com a internet e tente novamente.")
        exit()

# Função para desinstalar a biblioteca pytube usando o pip
def uninstall_pytube():
    try:
        subprocess.check_call(["pip", "uninstall", "pytube", "-y"])
    except subprocess.CalledProcessError:
        print("Falha ao desinstalar a biblioteca pytube. Verifique sua conexão com a internet e tente novamente.")
        exit()

# Verifica se a biblioteca pytube está instalada e atualiza para a versão mais recente
try:
    importlib.import_module('pytube')
    # Obter a versão atual do pytube
    import pytube
    installed_version = pytube.__version__

    # Obter a versão mais recente do pytube disponível no PyPI (repositório Python)
    import requests
    response = requests.get("https://pypi.org/pypi/pytube/json")
    latest_version = response.json()["info"]["version"]

    # Verifica se a versão instalada é mais antiga que a versão mais recente
    if installed_version != latest_version:
        print(f"Versão atual do pytube: {installed_version}")
        print(f"Versão mais recente do pytube: {latest_version}")
        print("Atualizando para a versão mais recente...")

        # Desinstalar a versão antiga do pytube
        uninstall_pytube()

        # Instalar a versão mais recente do pytube
        install_pytube()
        print("Atualização concluída!")
    else:
        print(f"Você já possui a versão mais recente do pytube ({latest_version}).")
except ImportError:
    print("A biblioteca pytube não está instalada. Vamos instalar para você...")
    install_pytube()

# Biblioteca do pytube
from pytube import YouTube

# Funcao barra superior Titulo
def barraTit():
    print("#" * 68)

# Fim da funcao

def versao():
    print("+      --=-=-=-=- ...::: YouDownPy v4.0 :::... -=-=-=-=-=--      +")

# Fim da funcao

def tituloApp():
    print("+ ....:: Programa para Baixar Vídeos ou MP3 do Youtube ::....    +")

# Fim da funcao

def linha():
    print("-" * 68)

# Fim da funcao

def info():
    print("!!! Obs. Seu arquivo será salvo dentro da pasta Downloads !!!")

# Fim da funcao

def espaco():
    print("")

# Fim da funcao

# função para download de vídeo
def DownloadVideo(link):
    video = YouTube(link)
    video_stream = video.streams.get_highest_resolution()
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    try:
        video_stream.download(output_path=downloads_path)
        print("Download de vídeo completo! O vídeo foi salvo em:", downloads_path)        
    except:
        print("Um erro impediu o sucesso do download do vídeo.")

# função para download de áudio (mp3)
def DownloadAudio(link):
    video = YouTube(link)
    audio_stream = video.streams.filter(only_audio=True).first()
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    try:
        audio_stream.download(output_path=downloads_path)
        original_filename = audio_stream.default_filename
        original_filepath = os.path.join(downloads_path, original_filename)
        mp3_filepath = os.path.join(downloads_path, f"{video.title}.mp3")

        # Convertendo o arquivo para MP3
        audio_clip = AudioFileClip(original_filepath)
        audio_clip.write_audiofile(mp3_filepath)
        audio_clip.close()

        # Excluindo o arquivo original após a conversão para MP3
        os.remove(original_filepath)

        print("Download de áudio (MP3) completo! O arquivo mp3 foi salvo em:", mp3_filepath)
    except:
        print("Um erro impediu o sucesso do download do áudio (MP3).")

# Inicio do Aplicativo
barraTit()
versao()
tituloApp()
barraTit()
linha()
info()
linha()
espaco()
espaco()

# ... (código existente)

while True:
    espaco()
    linha()
    print("Escolha a opção:")
    print("1. Baixar MP3")
    print("2. Baixar vídeo")
    print("3. Sair")
    opcao = input("Digite o número da opção desejada: ")
    linha()

    if opcao == "1":
        link = input("Cole o endereço do link e clique em enter: ")
        espaco()
        DownloadAudio(link)
    elif opcao == "2":
        link = input("Cole o endereço do link e clique em enter: ")
        espaco()
        DownloadVideo(link)
    elif opcao == "3":
        print("Saindo do programa. Até mais!")
        break  # Sai do loop
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1, 2 ou 3).")

# Fim do script

