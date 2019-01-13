import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("my Window")
image = pygame.image.load("resources/troll.jpeg").convert_alpha()
#screen.blit(image, (x, y))
pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1000, 500))
loop = True
draw = False
while loop:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            draw = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_f:
            loop = False
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
    if draw:
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 30, 30)
    pygame.display.flip()
pygame.quit()
