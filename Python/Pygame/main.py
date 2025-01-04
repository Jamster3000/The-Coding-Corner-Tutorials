import pygame
import sys
from PIL import Image #use pill to process the frames in the gif

pygame.init()

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
FPS = 60

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer-er")

clock = pygame.time.Clock()

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)
    
    def draw(self, camera_x):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))

    def update(self):
        pass

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.gravity = 1
        self.jump_strength = -24
        self.on_ground = False
        self.state = "alive"  #track death/alive state

        self.image_left = pygame.image.load("Images/player-left.png") 
        self.image_right = pygame.image.load("Images/player-right.png")
        self.image_dead_frames = self.load_gif("Images/death.gif")  #load the gif image

        self.image = pygame.transform.scale(self.image_right, (TILE_SIZE, TILE_SIZE))
        self.dead_frame_index = 0  #keep track of which frame player is on
        self.dead_animation_done = False  #bool to check if animation finished or not
        self.last_frame_time = pygame.time.get_ticks()  #apply a delay between frames
        self.frame_delay = 100  #the amount of time in milliseconds to wait before moving onto the next frame

    #loads the gi
    def load_gif(self, gif_path):
        gif = Image.open(gif_path)#opens the gif image
        frames = []
        
        while True:
            frame = pygame.image.fromstring(gif.tobytes(), gif.size, gif.mode)#gets required information from gif
            frame = pygame.transform.scale(frame, (TILE_SIZE, TILE_SIZE))#scales the frame of gif
            frames.append(frame)
            
            try:
                gif.seek(gif.tell() + 1)  # Move to the next frame
            except EOFError:
                break
        
        return frames #returns the frame which allows pygame to iterate through each frame to show it as an animation.

    def handle_input(self):
        if self.state == "dead":
            return  # No movement if player is dead

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
            self.image = pygame.transform.scale(self.image_left, (TILE_SIZE, TILE_SIZE)) 
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
            self.image = pygame.transform.scale(self.image_right, (TILE_SIZE, TILE_SIZE))
        else:
            self.velocity_x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_strength

    def apply_gravity(self):
        if self.state == "dead":
            return  # No gravity if player is dead
        self.velocity_y += self.gravity

    def move(self):
        if self.state == "dead":
            return  # No movement if player is dead

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
        if self.state == "dead" and not self.dead_animation_done:
            current_time = pygame.time.get_ticks()

            # Only switch to the next frame if the frame_delay has passed
            if current_time - self.last_frame_time > self.frame_delay:
                self.dead_frame_index += 1
                self.last_frame_time = current_time  # Reset the frame time

                if self.dead_frame_index >= len(self.image_dead_frames):
                    self.dead_frame_index = len(self.image_dead_frames) - 1  # Stay on last frame
                    self.dead_animation_done = True  # Animation is finished
            return  # Don't update other player logic if dead

        self.handle_input()
        self.apply_gravity()
        self.move()

    def draw(self, camera_x):
        if self.state == "dead":
            # Draw the current frame of the death animation
            screen.blit(self.image_dead_frames[self.dead_frame_index], (self.rect.x - camera_x, self.rect.y))
        else:
            screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))


game_map = [
    "                                                                ",
    "                                                                ",
    "                                                                ",
    "                                                                ",
    "          ###                                                   ",
    "                                                                ",
    "     ###E                                                       ",
    "                                                                ",
    "                       E###                                     ",
    "                                                                ",
    "############################### ########E  #############    ##  ##    #####    ####",
]

platforms = []
enemies = []

for row_index, row in enumerate(game_map):
    for col_index, col in enumerate(row):
        if col == "#":
            platforms.append(pygame.Rect(col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        elif col == "E":
            enemies.append(Enemy(col_index * TILE_SIZE, row_index * TILE_SIZE)) 

class Main_game:
    def __init__(self):
        self.camera_x = 0

    def handle_scrolling(self, player):
        if player.rect.x > WIDTH // 2:
            self.camera_x = player.rect.x - WIDTH // 2

        if self.camera_x < 0:
            self.camera_x = 0

    def draw_game(self, player, enemies):
        screen.fill(WHITE)

        for platform in platforms:
            pygame.draw.rect(screen, GREEN, (platform.x - self.camera_x, platform.y, TILE_SIZE, TILE_SIZE))

        for enemy in enemies:
            enemy.draw(self.camera_x)

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

        # Check if player collides with any enemy
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                player.state = "dead"  # Set the player's state to "dead" on collision
                print("Player died!")

        game.handle_scrolling(player)
        game.draw_game(player, enemies)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
