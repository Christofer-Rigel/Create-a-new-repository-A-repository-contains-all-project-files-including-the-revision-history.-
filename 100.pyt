import pygame

# Initialize Pygame
pygame.init()

# Set up the window
win_width, win_height = 500, 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Move the Square")

# Square properties
x, y = 250, 250   # Starting position
size = 50         # Size of the square
vel = 5           # Speed of movement

# Game loop
run = True
clock = pygame.time.Clock()

while run:
    # 1. Check for events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 2. Handle Arrow Key Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    # 3. Draw everything
    win.fill((0, 0, 0)) # Clear screen with black
    pygame.draw.rect(win, (255, 0, 0), (x, y, size, size)) # Draw red square
    pygame.display.update() # Refresh the screen

    clock.tick(60) # Limits the game to 60 frames per second

pygame.quit()