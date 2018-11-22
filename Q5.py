# Line towards your cursor with infinite length
# Right Click or Left Click to change position
# By: Ali


import pygame

# --- constants ---

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# --- functions ---

def calculate(player_x, player_y, mouse_x, mouse_y):
    dx = player_x - mouse_x + 0.1
    dy = player_y - mouse_y

    reversed_sign_x = 1 if dx < 0 else -1
    #reversed_sign_y = 1 if dy < 0 else -1

    slope = dy/dx

    x_new = reversed_sign_x * DISPLAY_WIDTH
    y_new = player_y + slope * (x_new - player_x)

    return x_new, y_new

# --- main ---

# - init -

pygame.init()
SCREEN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# - objects -

player_x = DISPLAY_WIDTH // 2
player_y = DISPLAY_HEIGHT // 2

mouse_x = player_x
mouse_y = player_y

x_new, y_new = calculate(player_x, player_y, mouse_x, mouse_y)

# - mainloop -

clock = pygame.time.Clock()
running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player_x, player_y = event.pos
        elif event.type == pygame.MOUSEMOTION:
            x_new, y_new = calculate(player_x, player_y, event.pos[0], event.pos[1])

    # - updates -

    # empty

    # - draws -

    SCREEN.fill(BLACK)
    pygame.draw.line(SCREEN, GREEN, (player_x, player_y), (x_new, y_new), 2)
    pygame.display.flip()

    # - FPS -

    clock.tick(25)

# - end -

pygame.quit()