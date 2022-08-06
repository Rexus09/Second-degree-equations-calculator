from tkinter import *
import math
from tkinter import messagebox
root = Tk()
root.title("Second degree equations calculator")
#crear los widgets
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
def mensaje():
    messagebox.showinfo("Answer: ",resultado)
raiz = 0
def ecuación(a,b,c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        discriminante = (b**2) - (4 * a * c)
        global raiz
        if discriminante > 0: #Evalúa si tiene solución
            raiz = math.sqrt(discriminante)
            if a != 0:
                result  = ((-b) - raiz)/ 2 * a
                result2 = ((-b) + raiz)/ 2 * a        
        else:
            result = c/b
            result2 = c/b
        global resultado
        resultado = "{:.3 } ==> Adding   {:.3}==> Substracting".format(result, result2)
        mensaje()
    except Exception as e:
        print(e)
        print("Tu ecuación no tiene soluciones reales :(")


root.geometry("{}x{}".format(screen_width,screen_height))
button_calculate = Button(root, text= "CALCULATE !", fg = "blue", activebackground = "white", command = lambda: ecuación(field_x2.get(),field_x1.get(),field_x0.get()))
field_x2 = Entry(root, width =30)
field_x1 = Entry(root, width  = 30)
field_x0 = Entry(root, width  = 30)

field_x2.insert(0,"X**2")
field_x1.insert(0,"X")
field_x0.insert(0,"Const")

#2 -5 3 ==> 1 & 1.5

#Mostrar los widgets
field_x2.grid(row = 1, column =1 )
field_x1.grid(row = 1, column =2 )
field_x0.grid(row = 1, column =3 )
button_calculate.grid(row = 2, column= 1)










mainloop()










