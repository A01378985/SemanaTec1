# Lucio Arturo Reyes Castillo - A0137898
# Arturo Barrios Mendoza - A01168331
# Leyberth Jaaziel Castillo Guerra - A01749505
# Israel González Huerta - A01751433

import random

LadoA = ['Granjero','Zorro','Ganso','Maiz']
LadoB = []
Path = []

def estado_valido(L):
    if 'Zorro' in L and 'Ganso' in L and len(L)==2:
        return False
    if 'Maiz' in L and 'Ganso' in L and len(L)==2:
        return False
    return True

def trayecto(F, D):
    p1 = random.choice(F)
    if p1 != 'Granjero':
        F.remove(p1)
        D.append(p1)
    F.remove('Granjero')
    D.append('Granjero')
    return (p1,'Granjero')

def reinicia_sistema():
    global LadoA, LadoB, Path
    LadoA = ['Granjero','Zorro','Ganso','Maiz']
    LadoB = []
    Path = []

def HCR():
    F = LadoA
    D = LadoB
    intentos = 0
    while len(LadoB)!=4:
        p1, p2 = trayecto(F, D)
        if estado_valido(F) and estado_valido(D):
            #print('Continuamos')
            Path.append((p1, p2))
            F, D = D, F
        else:
            intentos += 1
            reinicia_sistema()
            F = LadoA
            D = LadoB
    #print('Intentos:',intentos)
    #print(Path)
    return(Path)

def solucion_optima():
    Path = HCR()
    while len(Path) > 7:
        reinicia_sistema()
        Path = HCR()
    return(Path)

#print(solucion_optima())