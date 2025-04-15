import pygame

"""CONSTANTS"""
screen_width = 900
screen_height = 600
cell_size = 50
cell_margin = 5
key_width = 30
key_height = 40
key_width_margin = 5
key_height_margin = 5

def drawHUD():
    fps = clock.get_fps()
    fps_counter = font.render(f"FPS: {clock.get_fps():.2f}",True,"black")

    screen.blit(fps_counter,(30,50))

pygame.init()
pygame.display.set_caption("Wordle")
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

font = pygame.font.Font(None,30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit

    grid_x_pos = (screen_width // 2) - (cell_size*2.5) - (cell_margin*2.5)
    grid_y_pos = 30
    key_x_pos = (screen_width // 2) - (key_width*5) - (key_width_margin*5)
    key_y_pos = 400

    screen.fill("white")
    drawHUD()

    # draw grid
    for row in range(6):
        for column in range(5):
            pygame.draw.rect(screen,"darkgray",pygame.Rect(grid_x_pos,grid_y_pos,cell_size,cell_size),2)
            grid_x_pos += cell_size + cell_margin
        grid_x_pos = (screen_width // 2) - (cell_size*2.5) - (cell_margin*2.5)
        grid_y_pos += cell_size + cell_margin
    
    # draw keyboard layout
    for column in range(10):
        pygame.draw.rect(screen,"lightgray",pygame.Rect(key_x_pos,key_y_pos,key_width,key_height))
        key_x_pos += key_width + key_width_margin
    key_x_pos = (screen_width // 2) - (key_width*5) - (key_width_margin*5) + key_width // 2 + key_width_margin // 2
    key_y_pos += key_height + key_height_margin
    for column in range(9):
        pygame.draw.rect(screen,"lightgray",pygame.Rect(key_x_pos,key_y_pos,key_width,key_height))
        key_x_pos += key_width + key_width_margin
    key_x_pos = (screen_width // 2) - (key_width*5) - (key_width_margin*5)
    key_y_pos += key_height + key_height_margin
    pygame.draw.rect(screen,"lightgray",pygame.Rect(key_x_pos,key_y_pos,key_width+18,key_height))
    key_x_pos += key_width + key_width_margin+18
    for column in range(7):
        pygame.draw.rect(screen,"lightgray",pygame.Rect(key_x_pos,key_y_pos,key_width,key_height))
        key_x_pos += key_width + key_width_margin
    pygame.draw.rect(screen,"lightgray",pygame.Rect(key_x_pos,key_y_pos,key_width+18,key_height))        
    
    
    pygame.display.update()
    clock.tick(60)
