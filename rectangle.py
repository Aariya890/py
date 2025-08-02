import pygame

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drawing a Rectangle")


RED = (255, 0, 0)
BLUE = (0, 0, 255)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((255, 255, 255)) 
    
    pygame.draw.rect(screen, RED, (100, 100, 200, 150))
    pygame.draw.rect(screen, BLUE, (400, 200, 150, 100), 5) 
    pygame.display.flip()


pygame.quit()