import pygame
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mouse Click Example")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(f"Mouse clicked at: ({mouse_x}, {mouse_y})")
pygame.quit()