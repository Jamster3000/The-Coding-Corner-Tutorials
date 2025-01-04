If you would like to follow this tutorial step by step, below are a list of files that breaks up the code. If you just want the whole code completed, take a look at the [main.py](https://github.com/Jamster3000/The-Coding-Corner-Tutorials/blob/main/Python/Pygame/main.py)

1. basic_setup_alternitive.py
2. player (includes side-scrolling)
3. player-image
4. Player_direction.py
5. enemy.py
6. gif-animation-death.py

---

In this tutorial, you'll learn:
- Setting up Pygame
- Setting up the screen with platforms
- Adding a player and it's movement
- Using images as sprites rather than rectangles
- Implement Side-scrolling
- Adding a basic enemy
- And using a gif image as an animated death.

## Advice for this tutorial
- Each section of code will have comments to help you understand parts of the code - read them.
- Although you could copy and paste code, it's adviced that you try to take the time to type it out - people learn code much better if they are to type it out for themselves.
- You are more than welcome to ask for help in this server - but see if you can figure it out first, it's more beneficial and reward that way
- If you don't know what a class is or how to use it, I would advice doing learning about that.

---

You will be needing some image resources that are in [this repository](https://github.com/Jamster3000/The-Coding-Corner-Tutorials/tree/main/Python/Pygame/Images)

---

> Start with the [basic setup](https://github.com/Jamster3000/The-Coding-Corner-Tutorials/blob/main/Python/Pygame/basic_setup_alternitive.py) file.

# Setting up Pygame
At the top we import the only things we require.
You will need to install pygame as it doesn't come preinstalled as a library with python.

## installing pygame
Run `pip install pygame` in a terminal to install it for python. Depending on how your system is set up you may require an virtual environment for this.


At the top of the code, it just sets up some simple things that are required.

- `pygame.init()` This just sets up pygame itself and prepares it, this will always be required at the start if you use pygame.

- **variables** that are in all UPPER CASE are called **constant** variables. There are no rules for this and at end of the day, running your code, the computer doesn't know the difference as to whether it's all UPPER CASE or lower case.

Constant variables help understand that the value of that variable will not change throughout the code. **For example**: WHITE variable will always stay as (255, 255, 255) as that colour will never be modified or changed throughout the code.

## setting up the window
First the screen is set up, all we do here is create the window and tell it how big we want it. We will need to use this variable later on to say where we want to draw sprites and objects.

> I have included a set_caption which will change the name of the window, but this isn't needed if you don't feel like being fancy.

## Game Map
There are many ways of representing and rendering the map of a level/game. In this instance I've use something simple and easy to understand.

Blank spaces/white spaces represent nothing, other than the background color.

**#** represents the platforms. There is a long platform for the player to stand on, and some above them to jump onto.

---

![image](https://github.com/Jamster3000/The-Coding-Corner-Tutorials/blob/main/Python/Pygame/tutorial-resources/game_map_visualization.gif)

Below the game_map There is a for loop which checks through each row in the game_map then each column, resulting in checking every character and blank space in the game_map

Where the current character is "#" it will append as a platform in the platforms variable. You can see a visualization of what it looks like in the above image.

---
> `camera_x` will be used later on in this tutorial when implementing the side-scrolling. For now, it will just be kept as 0


> You'll also notice that there is a clock but it doesn't tell the time. The clock allows you to change the frames and how fast or slow they go. Typically 60 FPS is what you'd go for.

## Main_game class
Although classes aren't strictly required, without them in a game it makes code repetitive and over-complicated - I highly would suggest using classes to keep things more organized and less chaotic.

Currently, the `Main_game` class only has one procedure.

---

The `draw_game` procedure is in charge of rendering/drawing everything onto the screen and updating it.

- `screen.fill` is used to fill the screen white first otherwise you would be able to see the older frames still on the screen.

- For every platform there is in the `platforms` list it renders a green square in the place you wanted it in the `game_map`

- Finally now it's added them to the scrren, call `pygame.display.update()` as this will update the screen to visually see the changes

# main procedure
This is where the game now comes together.

Like any class, you have to call it and prepare it before actually using the procedures and functions.

- All games require a while loop as it has to continuously render a frame on the screen.

- There is a for loop inside this, which is essential to be able to close the game at all. When you try to close the game it sends a event "QUIT" - In this for loop you're just checking if it ever gets the even "QUIT" if it does get that event response, it will stop everything cleanly

> `sys.exit()` is a clean and efficient way of exiting a python program. 

- The `game.draw_game()`  procedure is called which if you remember, it's in control of rendering everything.

- Finally it sets the clock.tick at the end, although this can be called anywhere, it's best to put it at the end of your while loop.

---

> Start with the [basic setup](https://github.com/Jamster3000/The-Coding-Corner-Tutorials/blob/main/Python/Pygame/player.py) file.

# Player
Now let's modify the basic setup we currently have to include a player.


As you can see, most of the code is the same - the only thing that has importantly changed is that we now have a **player class** (It would be wise to understand what a class is in python first before getting started).

## __init__
First we start with init, as soon as the **Player** class is called, the __init__ procedure is called automatically.
As you can see, we're just creating some basic variable settings for the player.

- **velocity** - This is the the movement of the player.
- **speed** - unlike the velocity, this is the actual speed of the player - this can be changed.
- **Gravity** - self explanitory, it's the gravity which is helps with bringing the player back down when they jump.
- **Jump_strength** - How strong they jump, in this case,  it's backwards, so lower the number stronger the jump is (e.g., -30 will make them jump higher)
- **on_ground** - This is important, without this, we wouldn't be able to stop the player from jumping endlessly

## handle_input
This procedure deals with the keyboard input.

- **pygame.keys.get_pressed()** - returns a list of the keyboard keys that are actively being pressed downwards.


## check_collision
Although this looks a little more complicated, breaking it down helps to better understand it.

it loops through all the platforms to detect if it collides with any of the platforms. As you can see there is a pygame method being used; **colliderect**, as it suggests, it will return a bool as to any of the platforms (that are being looped/iterated over) is colliding with the player (self.rect in this class is the player).

`if platform.colliderect(self.rect):` is the exact same as `if platform.colliderect(self.rect) == True:`

# Main_game
We are also going to add the scrolling into this too.

- **__init__** The Main_game class now has it's own __init__ where it sets the X camera to 0. In a game, a camera is something that follows the player (metaphorically speaking).

## handle_scrolling
This is a simple procedure that uses a little bit of maths
- Makes sure that the player is always in the middle no matter what
- Makes sure it doesn't continue scrolling past the start .

__                                                __

Finally in the main while loop

```python
player.update()
game.handle_scrolling(player)
game.draw_game(player)
``` 

- We call the player update method
- call the game's handle_scrolling method
- Call the game's draw_game method

---

> Start with the [basic setup](https://github.com/Jamster3000/The-Coding-Corner-Tutorials/blob/main/Python/Pygame/player_image.py) file.

## Replacing the blue rectangle with an image instead
Very simple and easy, only three lines to change to change the player into an image.

In the player __init__ procedure, we've added two lines
- pygame.image.load obviously loads the image into the game
- pygame.transform.scale - This increases/decreases the size to match the TILE_SIZE we have previously set.

> Don't get mixed up - though we are now using an image instead of a rectangle, that doesn't mean the player doesn't have a rectangle still. A rectangle is essential for efficient collision

```python
screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))
```

Finally, the third line, we are just blitting the image to the screen rather than a rectangle.


> Start with the [basic setup](https://github.com/Jamster3000/The-Coding-Corner-Tutorials/blob/main/Python/Pygame/player_direction.py) file.

# Player Direction
It's great now that we have a player to move around - but don't you think that it looks weird going left, yet still looking right? Well that's what the `player-left.png` image is for.

This next part will show you how to change the images between the arrow keys.

## Player class
```python
#load the left and right player image in
self.image_left = pygame.image.load("Images/player-left.png") 
self.image_right = pygame.image.load("Images/player-right.png") 
        
 self.image = pygame.transform.scale(self.image_right, (TILE_SIZE, TILE_SIZE))  # Scale the image to the correct size
```

- Load the left and right image in
- load and scale the right image as the player always starts the game looking to the right.

## handle_input
Obviously, here we need to change the player image based on the arrow key. when the left key is pressed set self.image to the left scaled image and vice versa for the right arrow key.

that should be all for the player direction.

---

> Start with the [basic setup](https://github.com/Jamster3000/The-Coding-Corner-Tutorials/blob/main/Python/Pygame/enemy.py) file.

# Enemy
Next is an enemy to make the game even slightly challenging. This is going to be a super simple enemy to allow you to expand and experiment with it later on.

# Enemey class
There is another class for the enemy, similar to the player except much much simpler.

- We create the rect and fill it red
- The draw procedure just blit's it onto screen.
- The update might be useful to you if you had any movement or the enemy changes from time to time.


We're using `E` in the map to represent where the enemies are placed on the map.

Currently the game_map's for loop was 
```python
for row_index, row in enumerate(game_map):
    for col_index, col in enumerate(row):
        if col == "#":
            platforms.append(pygame.Rect(col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE))
```

But now we add an elif statement to include the enemies in the map

```python
for row_index, row in enumerate(game_map):
    for col_index, col in enumerate(row):
        if col == "#":
            platforms.append(pygame.Rect(col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        elif col == "E":
            enemies.append(Enemy(col_index * TILE_SIZE, row_index * TILE_SIZE))  #creates an enemy where E is present in the map
```

## main_game
in main_game.draw_game
we have 
```python
for enemy in enemies:
    enemy.draw(self.camera_x)
```

Which is very similar to the drawing for platforms.

## collision
```python
#Check if the player has collided with any of the enemies
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                print("Player died!")
                pygame.quit()
                sys.exit() 
```

Finally, the collision with the player, for now, if the player touches the enemy, the game just quits.

