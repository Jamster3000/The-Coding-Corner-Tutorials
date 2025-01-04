import pygame
import sys

#initilise pygame
pygame.init()

# Some basic constant variables
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
FPS = 60

#constant colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer-er")

#use symbols instead to create the entire map
game_map = [
    "                                        ",
    "                                        ",
    "                                        ",
    "                                        ",
    "          ###                           ",
    "                                        ",
    "     ###                                ",
    "                                        ",
    "                        ###             ",
    "                                        ",
    "###############################         "
]

platforms = []

#loop throw each (horizontal) row in the map
for row_index, row, in enumerate(game_map):
    #loop through each column in each row
    for col_index, col in enumerate(row):
        #if the col (character) is # then create a square of that platform
        if col == '#':
                        platforms.append(pygame.Rect(col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE))

camera_x = 0

#clock to say how fast the game should go
clock = pygame.time.Clock()

# a class to hold all the functions and procedures that are used for the game
class Main_game():
    def draw_game(self):
        screen.fill(WHITE)#sets the screen to plain white

        #loops through all the platforms and draws on screen after the white
        for platform in platforms:
            pygame.draw.rect(screen, GREEN, (platform.x - camera_x, platform.y, TILE_SIZE, TILE_SIZE))

        #visually updates the display
        pygame.display.update()

#The main game where all the loop and main part of the game runs
def main():
    #calls the class so the functions can be used.
    game = Main_game()

    run_game_loop = True

    while run_game_loop is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        game.draw_game()

        clock.tick(FPS)

if __name__ == "__main__":
    main()