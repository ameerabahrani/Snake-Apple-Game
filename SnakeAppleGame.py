import pygame 
import sys
import random

pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Apple Game")

# Define colors
snake_color = (0, 255, 0)
apple_color = (255, 0, 0)
background_color = (0, 0, 0)
block_size = 20
snake = [(300, 200), (200, 200), (260, 200)]
snake_direction = 'RIGHT'

def move_snake(snake, direction, grow = False):
    head_x, head_y = snake[0]

    if direction == 'UP':
        new_head = (head_x, head_y - block_size)
    elif direction == 'DOWN':
        new_head = (head_x, head_y + block_size)
    elif direction == 'LEFT':
        new_head = (head_x - block_size, head_y)
    elif direction == 'RIGHT':
        new_head = (head_x + block_size, head_y)

    snake.insert(0, new_head)
    if not grow:
        snake.pop()

clock = pygame.time.Clock()

def draw_apple():
    apple_x = random.randint(0, (WIDTH - block_size) // block_size) * block_size
    apple_y = random.randint(0, (HEIGHT - block_size) // block_size) * block_size
    return (apple_x, apple_y)

apple_position = draw_apple()


# Main game loop
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'
    
    grow = (snake[0] == apple_position)
    move_snake(snake, snake_direction, grow)
    
    if grow:
        apple_position = draw_apple()

    # Collision with wall 
    head_x, head_y = snake[0]
    if(head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT):
        print("Game Over!")
        pygame.quit()
        sys.exit()
    
    if(snake[0] in snake[1:]):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    if grow:
        apple_position = draw_apple()

    screen.fill(background_color)

    for segment in snake: 
        pygame.draw.rect(screen, snake_color, (segment[0], segment[1], block_size, block_size))
    pygame.draw.rect(screen, apple_color, (apple_position[0], apple_position[1], block_size, block_size))

    

    pygame.display.update()
    clock.tick(10)  

    


