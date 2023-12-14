def detPosition(x, y):
    result = ""
    if int(y) == 0 and int(x) == 0:
        return "Centro"

    if int(y) != 0:
        if int(y) > 0:
            result+="Cima "
        else:
            result+="Baixo "
    else:
        result+="Centro "
    if int(x) != 0:
        if int(x) > 0:
            result+="Direita"
        else:
            result+="Esquerda"
    else:
        result+="Centro"
    
    return result
#Testes
print("(0,0):   ", detPosition(0,0))
print("(2,0):   ", detPosition(2,0))
print("(0,2):   ", detPosition(0,2))
print("(-2,0):  ", detPosition(-2,0))
print("(0,-2):  ", detPosition(0,-2))
print("(2,2):   ", detPosition(2,2))
print("(2,-2):  ", detPosition(2,-2))
print("(-2,2):  ", detPosition(-2,2))
print("(-2,-2): ", detPosition(-2,-2))