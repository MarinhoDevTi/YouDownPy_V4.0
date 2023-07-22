import importlib

# Função para instalar a biblioteca pytube usando o pip
def install_pytube():
    import subprocess
    try:
        subprocess.check_call(["pip", "install", "pytube"])
    except subprocess.CalledProcessError:
        print("Falha ao instalar a biblioteca pytube. Verifique sua conexão com a internet e tente novamente.")
        exit()

# Verifica se a biblioteca pytube está instalada
try:
    importlib.import_module('pytube')
except ImportError:
    print("A biblioteca pytube não está instalada. Vamos instalar para você...")
    install_pytube()

#Biblioteca do pytube
from pytube import YouTube

#Aplicação desenvolvida por Marinho Tech Dev... 

#funcao barra superior Titulo
def barraTit():
    print("#" * 65)
#Fim da funcao 

def versao():
    print("+      --=-=-=-=- ...::: YouDownPy v1.0 :::... -=-=-=-=-=--      +")
#Fim da funcao

def tituloApp():
    print("+     ....:: Programa para Baixar Vídeos do Youtube ::....      +")
#Fim da funcao

def linha():
    print("-" * 65)
#Fim da funcao

def info():
    print("!!! Obs. Seu Vídeo será salvo dentro da pasta do Aplicativo !!!")
#Fim da funcao

def espaco():
    print("")
#Fim da funcao


#função para download 
def Donwload(link):
        
    baixarVideo = YouTube(link)
    #baixarVideo = baixarVideo.streams.get_lowest_resolution()
    baixarVideo = baixarVideo.streams.get_highest_resolution()
    #exceções 
    try:
        baixarVideo.download()
    except:
        print("Um erro impediu o exito de seu download !!")
    print("Download completo com sucesso !")
    

#Inicio do Aplicativo
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
Donwload(link)
linha()
