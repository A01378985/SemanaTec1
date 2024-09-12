import random

LadoA = ['granjero','zorro','ganso','maiz']
LadoB = []
Path = []

def estado_valido(L):
    if 'zorro' in L and 'ganso' in L and len(L)==2:
        return False
    if 'maiz' in L and 'ganso' in L and len(L)==2:
        return False
    return True

def trayecto(F, D):
    p1 = random.choice(F)
    if p1 != 'granjero':
        F.remove(p1)
        D.append(p1)
    F.remove('granjero')
    D.append('granjero')
    return (p1,'granjero')

def reinicia_sistema():
    global LadoA, LadoB, Path
    LadoA = ['granjero','zorro','ganso','maiz']
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
