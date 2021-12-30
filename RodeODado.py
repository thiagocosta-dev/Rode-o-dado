# Autor: Thiago Costa Pereira
# Email: thiago.devpython@gmail.com


#  Passo 1: importar bibliotecas que irei usar
import random
from tkinter import *
from PIL import Image, ImageTk

#  Passo 2: criar a janela com título do projeto
janela = Tk()
janela.geometry('400x400')
janela.title('Rode o Dado')

#  Passo 3
# Label introdução da Janela
label_texto = Label(janela, text='')
label_texto.pack()
# Label para formatação da Janela
label_texto1 = Label(janela, text='SIMULADOR DE DADO',
                     fg='black',
                     font='Arial 16 bold italic')
label_texto1.pack()

#  Passo 4: imagens dos dados a serem sorteadas.
dados = ['imagens_dado/dado_1.png', 'imagens_dado/dado_2.png', 'imagens_dado/dado_3.png', 'imagens_dado/dado_4.png',
         'imagens_dado/dado_5.png', 'imagens_dado/dado_6.png']
dado_capa = ImageTk.PhotoImage(file='imagens_dado/Dado.png')
label_capa = Label(janela, image=dado_capa)
label_capa.image = dado_capa
label_capa.pack(expand=True)


#  Passo 5: criar função para ação do botão que irá escolher uma imagem da lista que contem imagem dos dados
def rodar_dado():
    imagem = ImageTk.PhotoImage(Image.open(random.choice(dados)))
    #  Mostrar imagem
    label_capa.configure(image=imagem)
    label_capa.image = imagem


# Adicionando botão de ação
botao = Button(janela, text='Rode o dado', command=rodar_dado)
botao.pack(expand=True)

janela.mainloop()
