#Comando abaixo importa tudo da biblioteca que é necessaria
#Para a criação de tela. (ASTERISCO significa tudo)
from tkinter import *

#i ( instanciar) recebe o objeto tk
i=Tk()
#gerar titulo da janela
i.title('Programa Financeiro')

#Propriedade que altera o tamanho da janela (980x720) e distancia da direita e topo da tela(250x30)
i.geometry('980x720+250+30')

#Propriedades graficas, cor de fundo da tela (bg)ou (background)
#Não pode passar o i com ponto! DEVE SER i[]
i["bg"]="yellow"

#Cria o icone na janela, voce deve ter a imagem no mesmo local do codigo.
#i.wm_iconbitmap('icone.ico')

#Cria um label que posiciona (place). ele em relação a tela.

lb=Label(i,text='Nome do usuario')
lb.place(x=100,y=100)

#Cria um botão e posiciona(place) ele em relação a label.

bt=Button(i,width='20',text='OK')
bt.place(x=230,y=100)

#Gera a janela grafica
i.mainloop()