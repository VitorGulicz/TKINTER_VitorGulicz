from tkinter import *
i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')


lb1=Label(i,text="Login",bg="yellow")
#componente .grid serve tambem para posicionar utilizando indicativo de linha(row) e coluna(column)
lb1.grid(row=1,column=1)

lb2=Label(i,text="Senha",bg="red")
lb2.grid(row=2,column=2)

ed1 = Entry(i)
ed1.grid(row=3,column=3)

ed2 = Entry(i)
ed2.grid(row=4,column=4)

bt1=Button(i,text="Login")
bt1.grid(row=5,column=5)

i.mainloop()