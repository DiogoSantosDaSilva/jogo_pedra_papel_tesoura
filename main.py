import tkinter
from tkinter import *
from tkinter import ttk

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"


# Configurando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)
janela.resizable(False, False)


# Dividindo a janela
frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Configurando a label jogador
app_1_jogador = Label(frame_cima, text='Jogador', height=1, anchor='center',
                      font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1_jogador.place(x=25, y=70)

# Criando a barra de vitória ou perca.
app_1_barra_1 = Label(frame_cima, height=10, anchor='center', bg=co0, fg=co0)
app_1_barra_1.place(x=0, y=0)

# Criando o placar do jogador
app_1_placar = Label(frame_cima, text='0', height=1,
                     anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co0)
app_1_placar.place(x=30, y=5)

# Criando os dois pontos centrais

app_dois_pontos = Label(frame_cima, text=':', height=1,
                        anchor='center', font=('Ivy 20 bold'), bg=co1, fg=co0)
app_dois_pontos.place(x=120, y=25)

# Criando o placar do pc jogador

app_2_placar_2 = Label(frame_cima, text='0', height=1,
                       anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co0)
app_2_placar_2.place(x=180, y=5)


# Configurando a label pc jogador

app_2_jogador_2 = Label(frame_cima, text='PC', height=1, anchor='center',
                        font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2_jogador_2.place(x=190, y=70)

# Crinado a barra de vitória ou perca  do pc jogador

app_2_barra_2 = Label(frame_cima, height=10, anchor='center', bg=co0, fg=co0)
app_2_barra_2.place(x=255, y=0)

barra_placar_inf = Label(frame_cima, width=255,
                         anchor='center', bg=co0, fg=co0)
barra_placar_inf.place(x=0, y=95)

janela.mainloop()
