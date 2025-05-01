import pygame
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Animation")
x, y = 0, 300
width, height = 50, 50
speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += speed
    if x > 800:
        x = -width
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()