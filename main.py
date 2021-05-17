'''
05/17/2021

Pygame - Intro 

Pygame
- A set of python modules designed for writing video games

Coordinates in Pygame window
- The top left corner of the screen is (0,0) and the bottom right is (width, height)
- Positive x-direction is to the right and Negative x-direction is to the left.
- Positive y-direction is downward and negative y-direction is upward.

Important pygame functions
1. Import the Pygame library
import pygame

2. Initalize the Pygame
pygame.init()

3. Create a pygame window with sizes(Width, Height)
variable1 = pygame.display.set_mode((Width, Height))

4. Accepting key inputs from user 
pygame.key.get_pressed("KEYNAME")

5. Setup delay time (## in ms, (1s = 1000 ms))
pygame.time.delay(##)

6. Update frame
pygame.display.update()

7. Terminate the pygame at the end
pygame.quit()
'''

# 1. Import the pygame library
import pygame

# 2. Intalize pygame
pygame.init()

# 3. Make a pygame window(w,h) 
window = pygame.display.set_mode((500, 500))

# 4. Setup a caption (Game Name) on window to "First Game"

pygame.display.set_caption("First Pygame")

# 5. Set variables and values (starting coordinates)
# Assign 50 to 'x'
# Assign 10 to 'y'
x = 50
y = 10
# 6. Create an object (width and height) and speed
# Assign 10 to 'width'
# Assign 15 to 'height'
# Assign 5 to 'speed'
width = 10
height = 15
speed = 5
# 7. Create a control variable
# Assign True to 'run'
run = True

# 8. Launching a game with the control variable
while(run):
  # 9. Setup delay time to 100ms
  pygame.time.delay(100)

  # 10. Function the button
  for event in pygame.event.get():
    if(event.type == pygame.QUIT):
      # 11. Terminate Game when the button is pressed
      run = False
  # 12. Activite keys
  keys = pygame.key.get_pressed() 
  # 13. Left arrow key pressed, then decrease value of x
  if keys[pygame.K_LEFT]:
    x -= speed
  # 14. Right arrow key pressed, then increase value of x
  if keys[pygame.K_RIGHT]:
    x += speed
  # 15. Up arrow key pressed, then decrease value of y
  if keys[pygame.K_UP]:
    y -= speed
  # 16. Down arrow key pressed, then increase value of y
  if keys[pygame.K_DOWN]:
    y += speed

  # 19. As the object move, the background update
  window.fill((0,0,0))
  # 17. Setup a rectangle as a moving game
  pygame.draw.rect(window, (50, 150, 23), (x, y, width, height))
  # 18. Update the game 
  pygame.display.update()

# 11. Quit out of the game
pygame.quit()