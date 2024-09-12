import pygame
import sys
import HCR

pygame.init()

screen = pygame.display.set_mode((1500, 750))
pygame.display.set_caption('AnimalCrossingPirata')

BLUE = (196, 202, 220)

# Cargar las imágenes
granjero_img = pygame.image.load('granjero.png')
zorro_img = pygame.image.load('zorro.png')
ganso_img = pygame.image.load('ganso.png')
maiz_img = pygame.image.load('maiz.png')
barco_img = pygame.image.load('barco.png')
fondo_img = pygame.image.load('fondobueno.png')  # Cargar la imagen del fondo

posiciones = {
    'granjero': [0, 100],
    'zorro': [128, 100],
    'ganso': [256, 100],
    'maiz': [384, 100],
    'barco': [10, 100]
}

viajes = HCR.solucion_optima()

def dibujar_personajes():
    screen.blit(granjero_img, posiciones['granjero'])
    screen.blit(zorro_img, posiciones['zorro'])
    screen.blit(ganso_img, posiciones['ganso'])
    screen.blit(maiz_img, posiciones['maiz'])
    screen.blit(barco_img, posiciones['barco'])

def abordar(personaje):
    for i in range(14):
        posiciones[personaje][1] += 10
        screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
        dibujar_personajes()
        pygame.display.flip()
        pygame.time.delay(15)

def desembarcar(personaje):
    for i in range(14):
        posiciones[personaje][1] -= 10
        screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
        dibujar_personajes()
        pygame.display.flip()
        pygame.time.delay(15)

def horizontal(direc, pers1, *args):
    if len(args) < 1:
        if direc:
            for i in range(48):
                posiciones['barco'][0] += 20
                posiciones[pers1][0] += 20
                screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
                dibujar_personajes()
                pygame.display.flip()
                pygame.time.delay(15)
        else:
            for i in range(48):
                posiciones['barco'][0] -= 20
                posiciones[pers1][0] -= 20
                screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
                dibujar_personajes()
                pygame.display.flip()
                pygame.time.delay(20)
    else:
        pers2 = args[0]
        if direc:
            for i in range(48):
                posiciones['barco'][0] += 20
                posiciones[pers1][0] += 20
                posiciones[pers2][0] += 20
                screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
                dibujar_personajes()
                pygame.display.flip()
                pygame.time.delay(20)
        else:
            for i in range(48):
                posiciones['barco'][0] -= 20
                posiciones[pers1][0] -= 20
                posiciones[pers2][0] -= 20
                screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
                dibujar_personajes()
                pygame.display.flip()
                pygame.time.delay(20)

# **************************************************************************************************
# **************************************************************************************************
# **************************************************************************************************

movimientos = 0
direc = True
# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if movimientos < len(viajes):
        if viajes[movimientos][0] == viajes[movimientos][1]:
            abordar(viajes[movimientos][0])
            horizontal(direc, viajes[movimientos][0])
            desembarcar(viajes[movimientos][0])
            movimientos += 1
            direc = not direc
        else:
            abordar(viajes[movimientos][0])
            abordar(viajes[movimientos][1])
            horizontal(direc, viajes[movimientos][0], viajes[movimientos][1])
            desembarcar(viajes[movimientos][0])
            desembarcar(viajes[movimientos][1])
            movimientos += 1
            direc = not direc

    screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
    dibujar_personajes()
    pygame.display.flip()

    pygame.time.Clock().tick(1)