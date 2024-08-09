# Creando mi módulo:

def helloWorld(name):
    return f"Hi, {name}, how are you today?"

def calculator(number1, number2, basics = False):
    sum = number1 + number2
    minus = number1 - number2
    multiplication = number1 * number2
    divition = number1 / number2
    
    string = ""
    
    if basics != False:
        string += "Suma: " + str(sum)
        string += "\n"
        string += "Resta: " + str(minus)
        string += "\n"
    else:
        string += "Multiplicación: " + str(multiplication)
        string += "\n"
        string += "División: " + str(divition)
        string += "\n"
        
    return string

calculator(10,33, True)