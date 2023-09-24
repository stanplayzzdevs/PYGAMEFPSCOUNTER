import pygame

# initialize pygame
pygame.init()

# screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# load sprites
logo_sprite = pygame.image.load('sprites/logo.png')

# title bar
pygame.display.set_caption('OUR AMAZING PYGAME PROJECT')
pygame.display.set_icon(logo_sprite)

# variables
clock = pygame.time.Clock()

def Render_FPS(fps, color, pos):
    # add the font
    font = pygame.font.Font('fonts/Arial.ttf', 100)
    # create text
    text = font.render(fps, 1, (color))
    # function to draw the text onto the screen
    screen.blit(text, pos)

# main loop
running = True
while running:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background color
    screen.fill((50, 50, 50))

    # render fps to screen
    Render_FPS(str(int(clock.get_fps())), ("WHITE"), (0, 0))
    clock.tick()

    pygame.display.update()

pygame.quit()