from tkinter import *

def bt_click():
    #Codigo para validar a entrada apenas de numeros
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric):
        num1=int(ed1.get())
        num2=int(ed2.get())
        #Se os valores não forem numericos imprime a mensagem abaixo
        lb["text"]=num1+num2
        lb["bg"]="#00FA9A"
    else:
        lb["text"]="Valores Invalidos"
        lb["bg"]="red"

def bt_click_Menos():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric):
        num1=int(ed1.get())
        num2=int(ed2.get())
        lb["text"]=num1-num2
        lb["bg"]="#00FA9A"
    else:
        lb["text"]="Valores Invalidos"
        lb["bg"]="red"        

def bt_click_Multi():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric):
        num1=int(ed1.get())
        num2=int(ed2.get())
        lb["text"]=num1*num2
        lb["bg"]="#00FA9A"
    else:
        lb["text"]="Valores Invalidos"
        lb["bg"]="red"
        
def bt_click_Divi():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric):
        num1=int(ed1.get())
        num2=int(ed2.get())
        lb["text"]=num1/num2
        lb["bg"]="#00FA9A"
    else:
        lb["text"]="Valores Invalidos"
        lb["bg"]="red"

i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb=Label(i,text="0")
lb.place(x=230,y=200)

bt=Button(i,width="20",text='Soma',command=bt_click)
bt.place(x=230,y=230)

bt=Button(i,width="20",text='Menos',command=bt_click_Menos)
bt.place(x=230,y=260)

bt=Button(i,width="20",text='Mulitplicação',command=bt_click_Multi)
bt.place(x=230,y=290)

bt=Button(i,width="20",text='Divisão',command=bt_click_Divi)
bt.place(x=230,y=320)

ed1=Entry(i)
ed1.place(x=230,y=150)

ed2=Entry(i)
ed2.place(x=230,y=180)

lbnome=Label(i,text="Vitor Daniel Macedo Gulicz")
lbnome.place(x=230,y=350)

i.mainloop()