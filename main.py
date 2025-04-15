import pygame

"""CONSTANTS"""
screen_width = 900
screen_height = 600
cell_size = 50
cell_margin = 5

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

    screen.fill("white")
    drawHUD()

    for row in range(6):
        for column in range(5):
            pygame.draw.rect(screen,"darkgray",pygame.Rect(grid_x_pos,grid_y_pos,cell_size,cell_size),2)
            grid_x_pos += cell_size + cell_margin
        grid_x_pos = (screen_width // 2) - (cell_size*2.5) - (cell_margin*2.5)
        grid_y_pos += cell_size + cell_margin
    

    pygame.display.update()
    clock.tick(60)
