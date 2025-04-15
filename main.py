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
    fps_counter = font.render(f"FPS: {clock.get_fps():.2f}",True,"black")
    screen.blit(fps_counter,(30,50))

def draw_keyboard(key_color):
        key_y_pos = 400
        row_offset = [0,key_width // 2 + key_width_margin // 2,0]
        for row_index, row in enumerate(keyboard):
            key_x_pos = (screen_width // 2) - (key_width*5) - (key_width_margin*5) + row_offset[row_index]
            for key in row:
                width = key_width
                use_font = font
                if key in ("ENTER","DELETE"):
                    width += 18
                    use_font = special_font
                pygame.draw.rect(screen, key_color[key], pygame.Rect(key_x_pos, key_y_pos, width, key_height))
                label = use_font.render(key, True, "black")
                label_rect = label.get_rect(center=(key_x_pos + width // 2, key_y_pos + key_height // 2))
                screen.blit(label, label_rect)
                key_x_pos += width + key_width_margin
            key_y_pos += key_height + key_height_margin

pygame.init()
pygame.display.set_caption("Wordle")
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

font = pygame.font.Font(None,30)
special_font = pygame.font.Font(None,15)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
    
    screen.fill("white")
    drawHUD()

    # make list for letters
    grid_data = [
        [{"letter": "","color":"white"} for _ in range(5)]
        for _ in range(6)
    ]

    grid_x_pos = (screen_width // 2) - (cell_size*2.5) - (cell_margin*2.5)
    grid_y_pos = 30

    # draw grid
    for row in range(6):
        for column in range(5):
            pygame.draw.rect(screen,"darkgray",pygame.Rect(grid_x_pos,grid_y_pos,cell_size,cell_size),2)
            grid_x_pos += cell_size + cell_margin
        grid_x_pos = (screen_width // 2) - (cell_size*2.5) - (cell_margin*2.5)
        grid_y_pos += cell_size + cell_margin
    
    # make keyboard list
    keyboard = [list("QWERTYUIOP"),
                list("ASDFGHJKL"),
                ["ENTER"]+list("ZXCVBNM")+["DELETE"]]
    key_color = {key:"lightgray" for row in keyboard for key in row}
    
    key_x_pos = (screen_width // 2) - (key_width*5) - (key_width_margin*5)
    key_y_pos = 400

    draw_keyboard(key_color)       
    

    pygame.display.update()
    clock.tick(60)
