from tkinter import *
i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')


lb1=Label(i,text="Login",bg="yellow")
#componente .grid serve tambem para posicionar utilizando indicativo de linha(row) e coluna(column)
#lb1.grid(row=1,column=1)
lb1.place(x=740,y=120)

lb2=Label(i,text="Senha",bg="red")
#lb2.grid(row=2,column=2)
lb2.place(x=740,y=200)

ed1 = Entry(i)
#ed1.grid(row=3,column=3)
ed1.place(x=700,y=100)

ed2 = Entry(i)
#ed2.grid(row=4,column=4)
ed2.place(x=700,y=180)

bt1=Button(i,text="Login")
#bt1.grid(row=5,column=5)
bt1.place(x=440,y=420)

i.mainloop()