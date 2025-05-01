import pygame
import random
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
paddle_width = 15
paddle_height = 100
ball_radius = 10
left_paddle_y = 250
right_paddle_y = 250
ball_x = 400
ball_y = 300
ball_speed_x = random.choice([5, -5])
ball_speed_y = random.choice([5, -5])
paddle_speed = 10
left_score = 0
right_score = 0
font = pygame.font.SysFont("Arial", 32)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < 600 - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < 600 - paddle_height:
        right_paddle_y += paddle_speed
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    if ball_y <= 0 or ball_y >= 600 - ball_radius:
        ball_speed_y *= -1
    if (ball_x <= paddle_width and left_paddle_y <= ball_y <= left_paddle_y + paddle_height) or        (ball_x >= 800 - paddle_width - ball_radius and right_paddle_y <= ball_y <= right_paddle_y + paddle_height):
        ball_speed_x *= -1
    if ball_x < 0:
        right_score += 1
        ball_x = 400
        ball_y = 300
        ball_speed_x *= random.choice([1, -1])
        ball_speed_y *= random.choice([1, -1])
    elif ball_x > 800:
        left_score += 1
        ball_x = 400
        ball_y = 300
        ball_speed_x *= random.choice([1, -1])
        ball_speed_y *= random.choice([1, -1])
    score_text = font.render(f"{left_score} - {right_score}", True, WHITE)
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (0, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (785, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)
    window.blit(score_text, (350, 10))
    pygame.display.update()
pygame.quit()