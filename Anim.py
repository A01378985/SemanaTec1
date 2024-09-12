# Lucio Arturo Reyes Castillo - A0137898
# Arturo Barrios Mendoza - A01168331
# Leyberth Jaaziel Castillo Guerra - A01749505
# Israel González Huerta - A01751433

#importación de librerias

import pygame
import sys
import HCR

#iniciar los modulos de pygame e inicializar la ventana para el juego
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('CropopolyGameTheme.mp3')
pygame.mixer.music.play(-1)
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

# Definicioón de las posiciones de los personajes
posiciones = {
    'granjero': [0, 100],
    'zorro': [128, 100],
    'ganso': [256, 100],
    'maiz': [384, 100],
    'barco': [10, 100]
}

# Incluir la función que soluciona el juego
viajes = HCR.solucion_optima()

#Dibuja los personajes en las posiciones asignadas
def dibujar_personajes():
    screen.blit(granjero_img, posiciones['granjero'])
    screen.blit(zorro_img, posiciones['zorro'])
    screen.blit(ganso_img, posiciones['ganso'])
    screen.blit(maiz_img, posiciones['maiz'])
    screen.blit(barco_img, posiciones['barco'])

#Función para la animación de abordaje de los personajes al bote
def abordar(personaje):
    for i in range(14):
        posiciones[personaje][1] += 10
        screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
        dibujar_personajes()
        pygame.display.flip()
        pygame.time.delay(15)

#Función para la animación  de desembarque de los personajes
def desembarcar(personaje):
    for i in range(14):
        posiciones[personaje][1] -= 10
        screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
        dibujar_personajes()
        pygame.display.flip()
        pygame.time.delay(15)

# Función que genera el movimiento en horizontal y vertical del barco y los personajes
def horizontal(direc, pers1, *args):
    if len(args) < 1:
        if direc:
            for i in range(48):
                posiciones['barco'][0] += 20 # movimiento hacia la derecha del barco
                posiciones[pers1][0] += 20     #movimiento hacia la derecha del granjero
                screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
                dibujar_personajes()
                pygame.display.flip()
                pygame.time.delay(15)
        else:
            for i in range(48):
                posiciones['barco'][0] -= 20    #movimiento hacia la izquierda del barco
                posiciones[pers1][0] -= 20      #movimiento hacia la izquierda del granjero
                screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
                dibujar_personajes()
                pygame.display.flip()
                pygame.time.delay(15)
    else:
        pers2 = args[0]
        if direc:
            for i in range(48):
                posiciones['barco'][0] += 20    #movimiento hacia la derecha del barco
                posiciones[pers1][0] += 20      #movimiento hacia la derecha del granjero y un elemento
                posiciones[pers2][0] += 20
                screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
                dibujar_personajes()
                pygame.display.flip()
                pygame.time.delay(15)
        else:
            for i in range(48):
                posiciones['barco'][0] -= 20    #movimiento hacia la izquierda del barco
                posiciones[pers1][0] -= 20      #movimiento hacia la izquierda del granjero y un elemento
                posiciones[pers2][0] -= 20
                screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
                dibujar_personajes()
                pygame.display.flip()
                pygame.time.delay(15)

# **************************************************************************************************
# **************************************************************************************************
# **************************************************************************************************

movimientos = 0
direc = True
# Bucle principal para el movimiento en conjunto de todo el juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if movimientos < len(viajes):
        if viajes[movimientos][0] == viajes[movimientos][1]:        #Revisa si el granjero viene repetido
            abordar(viajes[movimientos][0])                         #abordar el granjero
            horizontal(direc, viajes[movimientos][0])               #movimiento horizontal del barco con el granjero
            desembarcar(viajes[movimientos][0])                     #desembarcar el granjero
            movimientos += 1
            direc = not direc                                       #invierte la dirección del barco
        else:
            abordar(viajes[movimientos][0])                         #aborda al granjero y otro personaje
            abordar(viajes[movimientos][1])
            horizontal(direc, viajes[movimientos][0], viajes[movimientos][1]) #movimiento horizontal del barco
            desembarcar(viajes[movimientos][0])                     #desembarca al granjero y al otro personaje
            desembarcar(viajes[movimientos][1])
            movimientos += 1
            direc = not direc                                       #invierte la dirección del barco

    screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
    dibujar_personajes()            #dibujar los personajes
    pygame.display.flip()

    pygame.time.Clock().tick(1)