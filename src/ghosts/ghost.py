from abc import ABC, abstractmethod
from ..box import Box
import pygame
from ..solver import Solver, Dijkstra, BFS, Glouton
# je dois connaitre
# la position du player
# comment utiliser cette classe ghost
#  en fonction du niveau on peut augmenter ou non le nombre de ghost
# par exemple le niveau 1 contient un seule ghost
# j'initialise mon niveau
# je genere le nombre de ghost

# dans la boucle du jeu 
# je fais ghost.chase()
# je retourne la position avec get_pos
# grace a cette function get_pos je peux pacilement placer
# le ghost sur le maze
# je retourne regarde si player et ghost sont sur la meme pos
# je si oui j'appele ghost.eaten()
# je pourrais facilement le placer sur la maze 
# if player eeat super pastille , ghost.frightened
# if player eat ghost
# ghost.eaten()


# so last time i have created this abstractghsot class 
# i now have the assets img for the ghost 
# i will now have to test the appear one the screen 
# then i will have to fix the little errors
# and then i will have to update the algos for each 
# now that i have the ghost in the screen 
# i need to handle when he it the pacman
# so maybe the function play ghost can return a certain int
# and when this int is being returned we will handle the pacman action to do 

class Ghost(ABC):
    def __init__(self, grid: list[list[Box]], cell_size: int) -> None:
        self.score: int = 0
        self.cell_size = cell_size
        self.is_chasing: bool = False
        self.scatter: bool = False
        self.is_frightened: bool = False
        self.is_eaten: bool = False
        self.grid: list[list[Box]] = grid
        self.pos: tuple[int, int] = self.find_spawn(self.grid)
        self.solver: Dijkstra = Dijkstra(self.grid)

    def chase(self, pacman_pos: tuple[int, int]) -> None:
        print(f"ghost pos: {self.pos}, pacman pos: {pacman_pos}")
        self.solver.algo(self.pos, pacman_pos)
        # print(f"distances computed: {len(self.solver.distance)} cells")
        path: list[tuple[int, int]] = self.solver.path_to(self.pos, pacman_pos)
        # print(f"path: {path}")
        if len(path) > 1:
            self.set_pos(path[1])

    def find_spawn(self, grid: list[list[Box]]) -> tuple[int, int]:
        for y, row in enumerate(grid):
            for x, box in enumerate(row):
                if box.type_box != 1 and box.type_box != 2:
                    return (x, y)
        return (1, 1)

    def frightened(self) -> None:
        pass

    def eaten(self) -> None:
        # to i need to do thing here
        # maybe handle reaparition
        pass    

    def get_pos(self) -> tuple[int, int]:
        return self.pos

    def set_pos(self, pos: tuple[int, int]) -> None:
        self.pos = pos

    # TODO CHANGE THIS FUNCTION TO DRAW TO ADERATE WITH CURRENT CODE ARCHITECTURE
    # def draw(self, screen: pygame.Surface, x_display_center) -> None:
    #     #print(x_display_center)
    #     #print(self.cell_size)

    #     x = (self.pos[0] * self.cell_size) + x_display_center
    #     y = (self.pos[1] * self.cell_size) + 100
    #     screen.blit(self.ghost_img, (x, y))
    #     # so i have to center the pos or it will not be displayed 
    #     # i must use existing function 
    #     print(f"{self.name} at pos: x: {x}, {y}")


    # puisque pinky cible la position quelque devant pacman pour lui tendre une embuscasde
    # nous auront besoin de cette fonction qui nous permettra de calculer cette pos
    # aussi Inky a besoin de cette function mais veut une pos apres pacman plus proche donc 
    # nous auront besoin de cette function ici
    def get_after_pacman_pos(self, pacman_pos: int, closeness: int):
        #  TODO calculate the position some case before pacman
        # this function will help me get the front pos of pacman
        # TODO add a function in algo to get_front_neigbor of a pos 
        after_pacman_pos = self.algos.get_front_neigbor(pacman_pos, closeness)
        return after_pacman_pos


    def play_ghost(self, pacman_pos: tuple[int, int], screen: pygame.Surface, x_display_center) -> int:
        if self.pos == pacman_pos:
        
            self.eaten()
            return -1
        else:
            self.draw(screen, x_display_center)
            self.chase(pacman_pos)
            return 0


# blinky le rouge
# sa strategy est la poursuite directe
# donc il devra connaitre la position du joueur
# et appliquer un algo de path finding type dyjkstra vers cette cyble
# la particularite de son comportement il accelere quand il reste peu de pastilles
# ( c'est le mode "cruise elroy") 
# class Blinky(Ghost):

#     def __init__(self, grid: list[list[Box]], cell_size: int):
#         super().__init__(grid, cell_size)
#         self.speed = 20
#         self.is_speeded = False
#         self.algo: str = "bfs"
#         self.pos: tuple[int, int] = self.find_spawn(grid)
#         self.ghost_img: pygame.Surface = GhostIcone.dir_ghost("blinky")[0]
        


#     def play_ghost(self, pacman_pos, screen, x_display_center):
#         if self.pos == pacman_pos:
#             self.eaten()
#             return -1
#         else:
#             # here i need to implement a tracking of pastille ? maybe i can i just 
#             # see based on the score i need also to implement the speed attribute
#             # and the is_speeded to track the state
#             self.draw(screen, x_display_center)

#     # TODO CHANGE THIS FUNCTION TO DRAW TO ADERATE WITH CURRENT CODE ARCHITECTURE
#     def draw(self, screen: pygame.Surface, x_display_center) -> None:
#         #print(x_display_center)
#         #print(self.cell_size)

#         x = (self.pos[0] * self.cell_size) + x_display_center
#         y = (self.pos[1] * self.cell_size) + 100
#         screen.blit(self.ghost_img, (x, y))
#         # so i have to center the pos or it will not be displayed 
#         # i must use existing function 
#         print(f"Blinky at pos: x: {x}, {y}")
            



# this is the blue ghost i dont know what it should do yet
class BlueGhost(Ghost):
        def __init__(self, grid, cell_size, name="blue_ghost", score=20):
            super().__init__(grid, cell_size, name, score)


# pinky le rose 
# sa strategy est l'anticipation
# son algoritme cible sa poition situe quelque cases devant Pac-Man en fonction de sa direction 
# effet tente de tendre une embuscade
class Pinky(Ghost):

    def __init__(self, grid, cell_size, name="pinky", score=30):
        super.__init__(self, grid, cell_size, name, score)
        pass

    def chase(self) -> None:
        pass

   
        
    def play_ghost(self, pacman_pos, screen, x_display_center):
        if self.pos  == pacman_pos:
            self.eaten()
        
        else:
            self.draw(screen, x_display_center)
            pos = self.get_after_pacman_pos(pacman_pos, 2)
            self.chase(pos)
            return 0

# inky bleu cyan 
# strategie , vectorielle complexe
# algo :
# prend un point devamt Pac-Man (comme Pinky, mais plus proche)
# calcule le vexteur entre Blinky et ce point 
# double ce vecteur pour obtenir la cible finale 
# effet : comportement instable et defficile a predire
class Inky(Ghost):

    def __init__(self, grid, cell_size, name="inky", score=30):
        super.__init__(self, grid, cell_size, name, score)
        pass

    def chase(self) -> None:
        pass

    def play_ghost(self, pacman_pos, screen, x_display_center):
        if self.pos == pacman_pos:
            self.eaten()
            return -1

        else:
            self.draw(screen, x_display_center)
            pos = self.get_after_pacman_pos(pacman_pos, 1)
            self.chase(pos)
            return 0



# algoritme :
# strategie ; Hybride (poursuite + fuite)
# si distance a pac-man > seuil
# cible = Pac-man (comme blinky)
# Sinon :
# cible coin bas gauche du labyrinthe 
class Clyde(Ghost):

    def __init__(self, grid, cell_size,  name="clyde", score=50):
        super.__init__(self, grid, cell_size, name, score)
        pass
    
    def chase(self) -> None:
        pass

    # calculate a distance between a pos a and a pos b 
    def get_dist(pos_a, pos_b):
        pass

    # get the pos o the left dowbn pos of the grid
    # usefull for Clyde only
    def get_left_down_pos(self):
        # TODO add a function to get left_down pos in the grid
        return self.algo.get_left_down_pos()
        pass

    def play_ghost(self, pacman_pos, screen, x_display_center):
        if self.pos == pacman_pos:
            self.eaten()
            return -1
        else:
            self.draw(screen, x_display_center)
            seuil = 3
            if self.get_dist(pacman_pos, self.pos) > seuil:
                pos = self.get_after_pacman_pos(pacman_pos, 1)
            else:
                pos = self.get_left_down_pos()
            self.chase(pos)
            return 0

# 1. Blinky (rouge)
# Stratégie : poursuite directe
# Algorithme :
# Cible = position actuelle de Pac-Man
# Se déplace en minimisant la distance (souvent distance de Manhattan) vers cette cible
# Comportement particulier : accélère quand il reste peu de pastilles (mode “Cruise Elroy”)
# 2. Pinky (rose)
# Stratégie : anticipation
# Algorithme :
# Cible = position située quelques cases devant Pac-Man (en fonction de sa direction)
# Bug connu : si Pac-Man monte, décalage supplémentaire vers la gauche
# Effet : tente de tendre une embuscade
# 3. Inky (bleu/cyan)
# Stratégie : vectorielle complexe
# Algorithme :
# Prend un point devant Pac-Man (comme Pinky, mais plus proche)
# Calcule le vecteur entre Blinky et ce point
# Double ce vecteur pour obtenir la cible finale
# Effet : comportement instable et difficile à prédire
# 4. Clyde (orange)
# Stratégie : hybride (poursuite + fuite)
# Algorithme :
# Si distance à Pac-Man > seuil :
# → cible = Pac-Man (comme Blinky)
# Sinon :
# → cible = coin bas gauche du labyrinthe
# Effet : alterne entre agressivité et dispersion
# États globaux (communs à tous)

# Les fantômes partagent une machine à états :

# Chase (poursuite) : applique leur algorithme spécifique
# Scatter (dispersion) : chacun vise un coin fixe du labyrinthe
# Frightened (apeuré) : déplacement pseudo-aléatoire après une super pastille
# Eaten (mangé) : retourne à la base avec une logique de chemin direct
# Mécanique de déplacement (simplifiée)
# À chaque intersection :
# Évalue les directions possibles (sans demi-tour sauf exceptions)
# Calcule la distance à la cible pour chaque direction
# Choisit la direction minimisant cette distance
# Priorité en cas d’égalité : ordre fixe (haut > gauche > bas > droite, selon implémentation)