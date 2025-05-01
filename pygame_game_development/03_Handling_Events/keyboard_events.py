import pygame
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move the Rectangle")
rect_x, rect_y = 400, 300
rect_width, rect_height = 50, 50
rect_speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()
pygame.quit()