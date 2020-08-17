#Second degree equations calculator
import math
print("Simple Mode:\nStructure--> ax_2 + bx + c = 0")
def ecuación():
    a  = int(input("Introduce squared x\t"))
    b = int(input("Introduce first degree x\t"))
    c = int(input("Introduce the cero degree value\t"))
    try:#Operaciones
        raiz = (b**2) - (4 * a * c)
        if raiz > 0: #Evalúa si tiene solución
            raiz_final = math.sqrt(raiz)
        result  = ((-b) - raiz_final)/ 2 * a
        result2 = ((-b) + raiz_final)/ 2 * a
        print("Results:\n {:.3} if we substract \nAnd\n {:.3} if we add".format(result, result2))
    except:
        print("The equation has no solution, or sth went wrong")
    #Tell if they`re positive or negative
    if result <0 and result2 <0:
        var = "Both results are negative"
    elif result >0 and result2 >0:
        var = "Both results are positive"
    else:
        var= "There`s only one positive number"
    print(var,)

ecuación()





try:#Operaciones
        raiz = (b**2) - (4 * a * c)
        if raiz > 0: #Evalúa si tiene solución
            raiz_final = math.sqrt(raiz)
        result  = ((-b) - raiz_final)/ 2 * a
        result2 = ((-b) + raiz_final)/ 2 * a
        print("Results:\n {:.3} if we substract \nAnd\n {:.3} if we add".format(result, result2))
    except:
        print("The equation has no solution, or sth went wrong")