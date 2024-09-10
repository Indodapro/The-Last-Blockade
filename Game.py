print('Program started')

import pygame, time, os, sys

print('Modules imported')

pygame.init()
pygame.font.init()
pygame.display.set_caption('The Last Blockade')

print('Pygame initiated')

#3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#3, 3, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#3, 3, 4, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#3, 3, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0,
#3, 3, 4, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 2, 5, 5, 5, 5, 5, 2, 0, 0,
#3, 3, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 2, 0, 0,
#3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 2, 0, 0,
#3, 3, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 2, 0, 0,
#3, 3, 4, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 2, 5, 5, 5, 5, 5, 2, 0, 0,
#3, 3, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0,
#3, 3, 4, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#3, 3, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#3, 3, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#3, 3, 4, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#3, 3, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#3, 3, 4, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#3, 3, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

# Set the width and height of the screen (width, height)
Size = (1920, 1080)
Center_X= Size[0] // 2
Center_Y = Size[1] // 2
screen = pygame.display.set_mode((Size), pygame.RESIZABLE)

print('Screen set')

import os 
import sys 
script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 
print(script_directory)

print('Script path found')

map_path = str(script_directory) + '/Map.dat'

# Load map data from a file
def load_map(filename):
    with open(filename, 'r') as file:
        map_data = []
        for line in file:
            # Remove any leading/trailing whitespace and ignore empty lines
            stripped_line = line.strip()
            if stripped_line:   # Only process non-empty lines
                map_data.append(list(map(int, stripped_line.split(','))))
        return map_data

def save_map(map_data, filename):
    with open(filename, 'w') as file:
        for row in map_data:
            line = ','.join(str(cell) for cell in row)
            file.write(line + '\n')

# Load the map
map = load_map( map_path)
print('Map loaded')

# Define grid parameters
Block_Size = 50

# Initialize cube position and direction
X, Y = 100, 100  # Initial position
last_X, last_Y = X, Y  # Store the last valid position
speed = 0.1
direction = 'up'  # Initial direction

# Center position of the character on the screen
char_x, char_y = Size[0] // 2 - Block_Size // 2, Size[1] // 2 - Block_Size // 2

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
BROWN = (150, 75, 0)
LIGHT_BROWN = (196, 164, 132)
YELLOW = (255, 255, 0)

cover = pygame.image.load(str(script_directory) + '/Cover.jpeg').convert()
cover = pygame.transform.scale(cover, (Size[1] / 2, Size[1] / 2))

clock = pygame.time.Clock()

# Create a Button Class
class Button:
    def __init__(self, text, pos, font, bg='black'):
        self.x, self.y = pos
        self.font = pygame.font.Font(font, 40)
        self.change_text(text, bg)

    def change_text(self, text, bg='black'):
        self.text = self.font.render(text, True, pygame.Color('white'))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(x, y):
                return True
        return False

def draw_text(text, text_col, size, x, y):
  Font = pygame.font.SysFont('arialblack', size)
  txt = Font.render(text, True, text_col)
  screen.blit(txt, (x, y))

def remove_decimal(number):
    # Convert the number to a string, split at the decimal point, and keep the integer part
    integer_part = str(number).split('.')[0]
    # Convert the result back to an integer to ensure no decimals remain
    return int(integer_part)

def get_value(x, y):
    return map[x][y]

def edit_value(x, y, n):
    x = remove_decimal(x)
    y = remove_decimal(y)
    # Can't find it but somewhere these get flipped so this reverses it, shit but whatever
    map[y][x] = n

def block_place(x, y, dir, block):
    if dir == 'up':
        edit_value(x, y - 1, block)
    if dir == 'down':
        edit_value(x, y + 1, block)
    if dir == 'left':
        edit_value(x - 1, y, block)
    if dir == 'right':
        edit_value(x + 1, y, block)

def draw_character(screen, x, y, direction):

    # Draw the main body (cube)
    pygame.draw.rect(screen, RED, (x, y, Block_Size, Block_Size))

    # Position of eyes based on the direction
    if direction == 'up':
        left_eye = (x + 15, y + 10)
        right_eye = (x + 35, y + 10)
    elif direction == 'down':
        left_eye = (x + 15, y + 40)
        right_eye = (x + 35, y + 40)
    elif direction == 'left':
        left_eye = (x + 10, y + 15)
        right_eye = (x + 10, y + 35)
    elif direction == 'right':
        left_eye = (x + 40, y + 15)
        right_eye = (x + 40, y + 35)

    # Draw the eyes
    pygame.draw.circle(screen, YELLOW, left_eye, 5)
    pygame.draw.circle(screen, YELLOW, right_eye, 5)

Home_screen = True
Menu = 'home'

# Create Home_screen Buttons
font = None
play_button = Button('Play', (20, 200), font)
options_button = Button('Options', (20, 300), font)
quit_button = Button('Quit', (20, 400), font)
fulscreen_button = Button('Toggle Fulscreen', (20, 200), font)
volume_button = Button('Volume', (20, 300), font)
back_button = Button('Back', (20, 400), font)

while  Home_screen == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Game Closed')
            pygame.quit()
            exit()
        if Menu == 'home':
            if play_button.click(event):
                Home_screen = False
            if options_button.click(event):
                Menu = 'options'
            if quit_button.click(event):
                print('Game closing...')
                pygame.quit()
                exit()
        if Menu == 'options':
            if fulscreen_button.click(event):
                pygame.display.toggle_fullscreen()
                print('Fullscreen mode toggled')
            if back_button.click(event):
                Menu = 'home'

    screen.fill(BLACK)

    if Menu == 'home':
        screen.blit(cover, (Size[0] / 4, Size[1] / 4))

    if Menu == 'home':
        play_button.show(screen)
        options_button.show(screen)
        quit_button.show(screen)
    if Menu == 'options':
        fulscreen_button.show(screen)
        volume_button.show(screen)
        back_button.show(screen)
        
    if Menu == 'home':
        draw_text('The Last Blockade', WHITE, 50, 20, 10)
    if Menu == 'options':
        draw_text('Options', WHITE, 50, 20, 10)

    pygame.display.update()

    pygame.display.flip()

    clock.tick(60)

# Create Pause Buttons
font = None
play_button = Button('Play', (20, 200), font)
options_button = Button('Options', (20, 300), font)
quit_button = Button('Quit', (20, 400), font)
fulscreen_button = Button('Toggle Fulscreen', (20, 200), font)
volume_button = Button('Volume', (20, 300), font)
back_button = Button('Back', (20, 400), font)

Run = True
Pause = False

# -------- Main Program Loop -----------
while Run == True:

    if Pause == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
                save_map(map, map_path)
                print('Game Closed')
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('Unpaused')
                    Pause = False
                    time.sleep(0.2)

        # Draw the button background
        pygame.draw.rect(screen, BLUE, (Size[0] / 4, 0, Size[0] / 2, Size[1]))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(30)

    if Pause == False:

        # Store the last valid position
        last_X, last_Y = X, Y

        col_index = Y // Block_Size
        row_index = X // Block_Size

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
                save_map(map, map_path)
                print('Game Closed')
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('Paused')
                    Pause = True
                    time.sleep(0.2)

        # Get the mouse position
        Mouse_X, Mouse_Y = pygame.mouse.get_pos()

        # Calculate differences from the center
        dx = Mouse_X - Center_X
        dy = Mouse_Y - Center_Y

        if abs(dx) > abs(dy):   # |dx| > |dy| means it's in left or right Direction
            if dx > 0:
                direction = 'right'
            else:
                direction = 'left'
        else:   # |dy| >= |dx| means it's in top or bottom Direction
            if dy > 0:
                direction = 'down'
            else:
                direction = 'up'

        # --- Game logic should go here
        check = True
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w] and keys[pygame.K_a]:
        #     check = False
        # if keys[pygame.K_w] and keys[pygame.K_s]:
        #     check = False
        # if keys[pygame.K_w] and keys[pygame.K_d]:
        #     check = False
        # if keys[pygame.K_a] and keys[pygame.K_w]:
        #     check = False
        # if keys[pygame.K_a] and keys[pygame.K_s]:
        #     check = False
        # if keys[pygame.K_a] and keys[pygame.K_d]:
        #     check = False
        # if keys[pygame.K_s] and keys[pygame.K_w]:
        #     check = False
        # if keys[pygame.K_s] and keys[pygame.K_a]:
        #     check = False
        # if keys[pygame.K_s] and keys[pygame.K_d]:
        #     check = False
        # if keys[pygame.K_d] and keys[pygame.K_w]:
        #     check = False
        # if keys[pygame.K_d] and keys[pygame.K_a]:
        #     check = False
        # if keys[pygame.K_d] and keys[pygame.K_s]:
        #     check = False
        

        if keys[pygame.K_e]:    #Place block
            block_place(X // Block_Size, Y // Block_Size, direction, 2)
            time.sleep(0.1)
        if keys[pygame.K_r]:    #Place block
            block_place(X // Block_Size, Y // Block_Size, direction, 3)
            time.sleep(0.1)
        elif keys[pygame.K_w]:    # Move up
                if check == True:
                    direction = 'up'
                    next_col_index = (Y - 50) // Block_Size
                    if next_col_index >= 0:
                        Y -= 50
                    time.sleep(speed)
        elif keys[pygame.K_a]:    # Move left
                if check == True:
                    direction = 'left'
                    next_row_index = (X - 50) // Block_Size
                    if next_row_index >= 0:
                        X -= 50
                    time.sleep(speed)
        elif keys[pygame.K_s]:    # Move down
                if check == True:
                    direction = 'down'
                    next_col_index = (Y + 50) // Block_Size
                    if next_col_index < len(map):
                        Y += 50
                    time.sleep(speed)
        elif keys[pygame.K_d]:    # Move right
                if check == True:
                    keys = ''
                    direction = 'right'
                    next_row_index = (X + 50) // Block_Size
                    if next_row_index < len(map[0]):
                        X += 50
                    time.sleep(speed)

        # Check if the new position is inside a block (collision detection)
        row_index = Y // Block_Size
        col_index = X // Block_Size
        if get_value(row_index, col_index) == 0:
            # Revert to the last valid position if collision is detected
            X, Y = last_X, last_Y
        if get_value(row_index, col_index) == 1:
            # Revert to the last valid position if collision is detected
            X, Y = last_X, last_Y
        if get_value(row_index, col_index) == 2:
            # Revert to the last valid position if collision is detected
            X, Y = last_X, last_Y
        if get_value(row_index, col_index) == 4:
            # Revert to the last valid position if collision is detected
            X, Y = last_X, last_Y

        # --- Screen-clearing code goes here
        screen.fill(WHITE)

        # --- Drawing code should go here
        # Offset the map based on the character's position
        offset_x = char_x - X
        offset_y = char_y - Y

        # Draw the grid
        for row_index, row in enumerate(map):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    pygame.draw.rect(
                        screen,
                        BLACK,
                        (col_index * Block_Size + offset_x, row_index * Block_Size + offset_y, Block_Size, Block_Size)
                    )
                if cell == 2:
                    pygame.draw.rect(
                        screen,
                        GREY,
                        (col_index * Block_Size + offset_x, row_index * Block_Size + offset_y, Block_Size, Block_Size)
                    )
                if cell == 3:
                    pygame.draw.rect(
                        screen,
                        GREEN,
                        (col_index * Block_Size + offset_x, row_index * Block_Size + offset_y, Block_Size, Block_Size)
                    )
                if cell == 4:
                    pygame.draw.rect(
                        screen,
                        BROWN,
                        (col_index * Block_Size + offset_x, row_index * Block_Size + offset_y, Block_Size, Block_Size)
                    )
                if cell == 5:
                    pygame.draw.rect(
                        screen,
                        BLUE,
                        (col_index * Block_Size + offset_x, row_index * Block_Size + offset_y, Block_Size, Block_Size)
                    )
                if cell == 6:
                    pygame.draw.rect(
                        screen,
                        LIGHT_BROWN,
                        (col_index * Block_Size + offset_x, row_index * Block_Size + offset_y, Block_Size, Block_Size)
                    )

        # Draw the character
        draw_character(screen, char_x, char_y, direction)

        draw_text(str(X // 50) + ' , ' + str(Y // 50), BLACK, 20, 10, 10)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(30)

# Close the window and quit.
pygame.quit()
exit()
