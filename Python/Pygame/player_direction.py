import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
FPS = 60

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer-er")

clock = pygame.time.Clock()

game_map = [
    "                                                                                  #",
    "                                                                                  #",
    "                                                                                  #",
    "                                                                                  #",
    "          ###                                                                     #",
    "                                                                                  #",
    "     ###                                                                          #",
    "                                                                                  #",
    "                        ###                                                       #",
    "                                                                                  #",
    "############################### #########  #############    ##  ##    #####    ####"
]

platforms = []

for row_index, row in enumerate(game_map):
    for col_index, col in enumerate(row):
        if col == "#":
            platforms.append(pygame.Rect(col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE))


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.gravity = 1
        self.jump_strength = -24
        self.on_ground = False

        #load the left and right player image in
        self.image_left = pygame.image.load("Images/player-left.png") 
        self.image_right = pygame.image.load("Images/player-right.png") 
        
        self.image = pygame.transform.scale(self.image_right, (TILE_SIZE, TILE_SIZE))  # Scale the image to the correct size

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed

            #use left image
            self.image = pygame.transform.scale(self.image_left, (TILE_SIZE, TILE_SIZE))
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed

            #use right image
            self.image = pygame.transform.scale(self.image_right, (TILE_SIZE, TILE_SIZE))
        else:
            self.velocity_x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_strength

    def apply_gravity(self):
        self.velocity_y += self.gravity

    def move(self):
        self.rect.x += self.velocity_x
        self.check_collision(True)

        self.rect.y += self.velocity_y
        self.check_collision(False)

        if self.rect.x < 0:
            self.rect.x = 0

    def check_collision(self, horizontal):
        self.on_ground = False
        for platform in platforms:
            if platform.colliderect(self.rect):
                if horizontal:
                    if self.velocity_x > 0:
                        self.rect.right = platform.left
                    elif self.velocity_x < 0:
                        self.rect.left = platform.right
                else:
                    if self.velocity_y > 0:
                        self.rect.bottom = platform.top
                        self.velocity_y = 0
                        self.on_ground = True
                    elif self.velocity_y < 0:
                        self.rect.top = platform.bottom
                        self.velocity_y = 0

    def update(self):
        self.handle_input()
        self.apply_gravity()
        self.move()

    def draw(self, camera_x):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))


class Main_game:
    def __init__(self):
        self.camera_x = 0

    def handle_scrolling(self, player):
        if player.rect.x > WIDTH // 2:
            self.camera_x = player.rect.x - WIDTH // 2

        if self.camera_x < 0:
            self.camera_x = 0

    def draw_game(self, player):
        screen.fill(WHITE)

        for platform in platforms:
            pygame.draw.rect(screen, GREEN, (platform.x - self.camera_x, platform.y, TILE_SIZE, TILE_SIZE))

        player.draw(self.camera_x)

        pygame.display.update()


def main():
    game = Main_game()
    player = Player(100, HEIGHT - TILE_SIZE - 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update()
        game.handle_scrolling(player)
        game.draw_game(player)

        clock.tick(FPS)


if __name__ == "__main__":
    main()