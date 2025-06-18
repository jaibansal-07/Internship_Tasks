import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake and food
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = (BLOCK_SIZE, 0)
food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
        random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, BLOCK_SIZE):
                snake_direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -BLOCK_SIZE):
                snake_direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and snake_direction != (BLOCK_SIZE, 0):
                snake_direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-BLOCK_SIZE, 0):
                snake_direction = (BLOCK_SIZE, 0)

    # Move snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    
    # Check collisions
    if (new_head in snake or
        new_head[0] < 0 or new_head[1] < 0 or
        new_head[0] >= WIDTH or new_head[1] >= HEIGHT):
        print("Game Over!")
        running = False

    snake.insert(0, new_head)

    # Check if food is eaten
    if new_head == food:
        food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()