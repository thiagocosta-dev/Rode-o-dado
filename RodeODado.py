"""
Erros para corrigir:
#  Procurar como mostrar dado depois de clicar no botão Só mostra a 1° vez.
Link do vídeo para dicas: https://youtu.be/AiBC01p58oI
"""

from tkinter import *

janela = Tk()
janela.title('Rode o Dado')  # Titulo da janela

texto_orientacao = Label(janela, text='Clique no botão para rodar o dado.')
texto_orientacao.grid(column=2, row=2, padx=10, pady=10)

texto_dado = Label(janela, text='')  # Variável que mostra número sorteado pelo dado
texto_dado.grid(column=2, row=4, padx=10, pady=10)  # Localização do número
texto_dado.configure(font=('Courier', 30, 'bold'))  # Configuração do número


def rodar_o_dado():  # Função que sorteia os números
    from random import randint
    dado = randint(1, 6)
    dado_rodado = dado
    texto_dado["text"] = dado_rodado  # Label que aponta para texto do dado
    return dado

#  Procurar como mostrar dado depois de clicar no botão


# num_dado = rodar_o_dado()
# if num_dado == 1:
#     img_dado_1 = PhotoImage(file='imagens_dado/dado_1.png')
#     dado_1 = Label(janela, image=img_dado_1)
#     dado_1.grid(column=2, row=5, padx=10, pady=10)
# elif num_dado == 2:
#     img_dado_2 = PhotoImage(file='imagens_dado/dado_2.png')
#     dado_2 = Label(janela, image=img_dado_2)
#     dado_2.grid(column=2, row=5, padx=10, pady=10)
# elif num_dado == 3:
#     img_dado_3 = PhotoImage(file='imagens_dado/dado_3.png')
#     dado_3 = Label(janela, image=img_dado_3)
#     dado_3.grid(column=2, row=5, padx=10, pady=10)
# elif num_dado == 4:
#     img_dado_4 = PhotoImage(file='imagens_dado/dado_4.png')
#     dado_4 = Label(janela, image=img_dado_4)
#     dado_4.grid(column=2, row=5, padx=10, pady=10)
# elif num_dado == 5:
#     img_dado_5 = PhotoImage(file='imagens_dado/dado_5.png')
#     dado_5 = Label(janela, image=img_dado_5)
#     dado_5.grid(column=2, row=5, padx=10, pady=10)
# else:
#     img_dado_6 = PhotoImage(file='imagens_dado/dado_6.png')
#     dado_6 = Label(janela, image=img_dado_6)
#     dado_6.grid(column=2, row=5, padx=10, pady=10)


botao = Button(janela, text='RODAR DADO', command=rodar_o_dado)  # Botão que roda dado
botao.grid(column=2, row=3, padx=10, pady=10)  # Localização do botão


janela.mainloop()
