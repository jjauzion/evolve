import pygame

print("hello")

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("my Window")
image = pygame.image.load("/Users/jjauzion/Desktop/big_brother.jpg").convert_alpha()
#screen.blit(image, (x, y))
pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1000, 500))
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            pygame.draw.rect(screen, (0, 0, 0), (x, y, 3, 3))
        elif event.type == pygame.KEYUP and event.key == pygame.K_f:
            loop = False
    pygame.display.flip()
pygame.quit()
