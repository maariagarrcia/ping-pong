#1.1 - Ventana de juego

import pygame
from pygame.locals import QUIT

#1.2 - Inicializamos pygame y definimos las constantes

VENTANA_HORI = 800  
VENTANA_VERT = 600  
FPS = 60
BLANCO = (255, 255, 255)  

def main():
    pygame.init()
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 1")
#1.3 - Creamos el bucle principal del código
    jugando = True
    while jugando:
        ventana.fill(BLANCO)
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()