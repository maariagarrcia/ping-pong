import random
import pygame
from pygame.locals import QUIT
#Inicializamos pygame y definimos las constantes
VENTANA_HORI = 800  
VENTANA_VERT = 600  
FPS = 60
BLANCO = (255, 255, 255)  
# Definimos la clase pelota y dentro sus características
class PelotaPong:
    def __init__(self, fichero_imagen):
        # ---- C A R A C T E R I S T I C A S
        # La imagen
        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()
        # Dimensiones
        self.ancho, self.alto = self.imagen.get_size()
        # Posición 
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        # Dirección de movimiento 
        self.dir_x = random.choice([-5, 5])
        self.dir_y = random.choice([-5, 5])
        #Puntación de la pelota
        self.puntuacion = 0
        self.puntuacion_ia = 0

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y
# a continuación queremos crear una función para hacer que nuestra pelota rebote
# nuestra función rebotar detecta que si la pelota sale por la izq o derecha, se inicia una nueva jugada
    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ia += 1
        if self.x >= VENTANA_HORI:
            self.reiniciar()
            self.puntuacion += 1
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= VENTANA_VERT:
            self.dir_y = -self.dir_y
# añadimos una función para poder reiniciar la jugada
    def reiniciar(self):
        self.x = VENTANA_HORI / 2 - self.ancho / 2
        self.y = VENTANA_VERT / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-5, 5])
# Añadimos las clase raqueta que es muy parecida al de la pelota y incluimos tambien sus caracteristicas       
class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("raqueta.png").convert_alpha()
        #---- C A R A C T E R I S T I C A S
        # Dimensiones
        self.ancho, self.alto = self.imagen.get_size()
        # Posición
        self.x = 0
        self.y = VENTANA_VERT / 2 - self.alto / 2
        # Dirección de movimiento
        self.dir_y = 0
    def mover(self):
       self.y += self.dir_y
       if self.y <= 0: 
           self.y = 0
       if self.y +self.alto >= VENTANA_VERT:
           self.y = VENTANA_VERT - self.alto

def main():
    # Inicialización de Pygame
    pygame.init()
    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 2")
    pelota = PelotaPong("bola_roja.png")
    

    # Creacion de las raquetas ya que  esta creada su clase, creando dos variables, modificando sus caracteristicas
    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60
    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()
        # Dibujar raquetas
        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

        #Se detecta la pulsación de una tecla
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_w:
                    raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 5
        #Se detecta que la tecla ha sido soltada
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta_1.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    main()
