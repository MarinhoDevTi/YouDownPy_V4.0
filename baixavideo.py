import importlib
import subprocess
import os

import importlib
import subprocess

# Função para instalar a biblioteca pytube usando o pip
def install_pytube():
    try:
        subprocess.check_call(["pip", "install", "pytube"])
    except subprocess.CalledProcessError:
        print("Falha ao instalar a biblioteca pytube. Verifique sua conexão com a internet e tente novamente.")
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

# Aplicação desenvolvida por Marinho Tech Dev...

# Funcao barra superior Titulo
def barraTit():
    print("#" * 65)

# Fim da funcao

def versao():
    print("+     --=-=-=-=- ...::: YouDownPy v3.0 :::... -=-=-=-=-=--      +")

# Fim da funcao

def tituloApp():
    print("+     ....:: Programa para Baixar Vídeos do Youtube ::....      +")

# Fim da funcao

def linha():
    print("-" * 65)

# Fim da funcao

def info():
    print("!!! Obs. Seu Vídeo será salvo dentro da pasta do Aplicativo !!!")

# Fim da funcao

def espaco():
    print("")

# Fim da funcao

# função para download
def Download(link):
    baixarVideo = YouTube(link)
    baixarVideo = baixarVideo.streams.get_highest_resolution()

    # Obter a pasta "Downloads" do sistema
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    try:
        # Define o diretório de destino para o download
        baixarVideo.download(output_path=downloads_path)
    except:
        print("Um erro impediu o sucesso do download !!")
        return

    print("Download completo com sucesso! O vídeo foi salvo em: ", downloads_path)

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

linha()
link = input("Cole o endereço do link e clique em enter: ")
linha()
Download(link)
linha()
