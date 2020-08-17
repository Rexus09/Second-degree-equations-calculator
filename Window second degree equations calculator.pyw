from tkinter import *
import math
from tkinter import messagebox
root = Tk()
root.title("Second degree equations calculator")
#crear los widgets
def mensaje():
    messagebox.showinfo("Answer",resultado)
def ecuación(a,b,c):
    
    a = int(a)
    b = int(b)
    c = int(c)
    raiz = (b**2) - (4 * a * c)
    if raiz > 0: #Evalúa si tiene solución
        raiz_final = math.sqrt(raiz)
    result  = ((-b) - raiz_final)/ 2 * a
    result2 = ((-b) + raiz_final)/ 2 * a
    global resultado
    resultado = "Results:\n {:.3} if we substract \nAnd\n {:.3} if we add".format(result, result2)
    mensaje()
    
    print("The equation has no solution, or sth went wrong")
root.geometry("1080x200")
button_calculate = Button(root, text= "CALCULATE !", fg = "blue", activebackground = "white", command = lambda: ecuación(field_x2.get(),field_x1.get(),field_x0.get()))
field_x2 = Entry(root, width = 50)
field_x1 = Entry(root, width = 50)
field_x0 = Entry(root, width = 50)

field_x2.insert(0,"X Grado 2")
field_x1.insert(0,"X Grado 1")
field_x0.insert(0,"Grado 0")





#Mostrar los widgets
field_x2.grid(row = 1, column =1 )
field_x1.grid(row = 1, column =2 )
field_x0.grid(row = 1, column =3 )
button_calculate.grid(row = 2, column= 4)










mainloop()










