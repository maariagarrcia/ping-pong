# ping-pong

La tarea consiste en trabajar de forma conjunta con un repositorio compartido (máximo 3 personas) donde al menos se mostrarán 10 commits, 10 miltones y 5 proyects en el repositorio conjunto con varias ramas por persona y realizar la tarea pendiente que se presenta al final del documento

Historia de Pong:

Aunque desde la aparición de los ordenadores programables en los años 40 del siglo XX se han escrito programas que podían considerarse juegos, se suele considerar que el primer videojuego fue Computer Tennis. Este videojuego fue creado en 1958 para la exposición anual del Laboratorio Nacional de Brookhaven (EEUU) y simulaba un pista de tenis vista lateralmente. El juego se visualizaba en la pantalla de un osciloscopio y se convirtió en la mayor atracción de esa exposición. Aunque al año siguiente la exposición contó con una versión mejorada, tras ella el equipo se desmontó para reutilizar los componentes en el Laboratorio.

Bastante años después, en septiembre de 1972, se comercializó la primera videoconsola de la historia dirigida a los hogares, Magnavox Odyssey. Esta videoconsola se conectaba a una pantalla de televisor y uno de los juegos incluidos era Table Tennis. En este juego cada jugador controlaba una paleta que golpeaba una pelota. El mismo año, pero en noviembre, la compañía Atari comercializó Pong, una de las primeras máquinas de arcade, destinadas a lugares públicos.

Para poder realizar nuestro trabajo hemos creado un repositorio compartido en el cual a través de Milestones e Issues nos hemos organizado el trabajo, de modo que cada una debía realizar 3 de las 9 tareas que permitían elaborar nuestro código. (Adjunto URL del repositorio: https://github.com/maariagarrcia/ping-pong.git )

Como ya habíamos mencionado, entre las 3 hemos elaborado un código que que representa un juego de ping pong y para ello cada una ha trabajado partes distintas del mismo que hemos unido obteniendo lo siguiente:
``` import random
from typing import Text
import pygame
from pygame.locals import QUIT

#Inicializamos pygame y definimos las constantes
VENTANA_HORI = 800  
VENTANA_VERT = 600  
FPS = 60
BLANCO = (255, 255, 255)  
NEGRO = (0,0,0)
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
        #Puntuación
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
            self.puntuacion +=1
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
       if self.y + self.alto >= VENTANA_VERT:
           self.y = VENTANA_VERT - self.alto

    # Mover la raqueta con una estrategia definida  
    def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3
        elif self.y < pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y

#creamos una función que permita golpear la pelota
    def golpear(self, pelota):
        if (
            pelota.x < self.x + self.ancho
            and pelota.x > self.x
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho
    
    #Metodo similar al de golpear del humano pero con la inteligencia artificial
    def golpear_ia(self, pelota):
        if (
            pelota.x + pelota.ancho > self.x
            and pelota.x < self.x + self.ancho
            and pelota.y + pelota.alto > self.y
            and pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.ancho

def main():
    # Inicialización de Pygame
    pygame.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Pong 2")
    # Iniciación de la fuente 
    fuente = pygame.font.Font(None, 60)
    pelota = PelotaPong("bola_roja.png")
    
    # Creacion de las raquetas ya que  esta creada su clase, creando dos variables, modificando sus caracteristicas
    raqueta_1 = RaquetaPong()
    raqueta_1.x = 60
    raqueta_2 = RaquetaPong()
    raqueta_2.x = VENTANA_HORI - 60 - raqueta_2.ancho
#BP
    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()
        raqueta_2.mover_ia(pelota)
        raqueta_1.golpear(pelota)
        raqueta_2.golpear_ia(pelota)
        # Dibujar raquetas
        ventana.fill(BLANCO)
        ventana.blit(pelota.imagen, (pelota.x, pelota.y))
        ventana.blit(raqueta_1.imagen, (raqueta_1.x, raqueta_1.y))
        ventana.blit(raqueta_2.imagen, (raqueta_2.x, raqueta_2.y))
        Text = f"{pelota.puntuacion} : {pelota.puntuacion_ia}"
        letrero = fuente.render(Text, False, NEGRO)
        ventana.blit(letrero, (VENTANA_HORI/ 2 - fuente.size(Text)[0]/ 2,50))
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
