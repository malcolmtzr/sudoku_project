#Construct and implement GUI for Sudoku solver, using pygame.
import pygame
from sudoku_txtv1 import find_empty_cells, harmony, solve_sudoku
import time
pygame.init()

#Create classes for global grid, and single cell.


class Single_Cell:
    rows = 9                                                           #Class Variables present in all SIngle_Cell instances.
    columns = 9                                                        #Class Variables will be used as arguments for parameters: rows & columns in the Global_Grid Instance.
    def __init__(self, value, row, column, width, height):
        self.value = value
        self.row = row
        self.column = column
        self.width = width                                             #Both self.width & self.height attributes will be same as the self.width & self.height attributes in Global_Grid instance,
        self.height = height                                           #because it not realistic to determine the exact dimensions of each Single_Cell instance.
        self.selection = False
        self.temporary_value = 0

    def insert_temporary_value(self, value):                           #Method sets a temporary value in the selected cell if inserted value does not satisfy global constaints,
        self.temporary_value = value                                   #or, if user wants to put a value in the selected cell but does not want to commit the value in the selected cell (sketch).
    
    def insert_value(self, value):                                     #Method inserts a value in the selected cell.
        self.value = value

    def draw_single_cell(self, screen):                                #Method highlights the selected cell, takes its value - whether empty (0) or otherwise, and blits the number (image) onto the screen (surface).
        cell_measuremt = (self.height / 9)                             #Divide either self.width or self.height by 9 to get width or height (dimensions) of a Single_Cell instance, which is a square.         
        cell_x = (self.column * cell_measuremt)                        #Calculate x & y coordinates of the Single_Cell, coordinates are not indices but actual measurement values.
        cell_y = (self.row * cell_measuremt)
        gray = (128, 128, 128)
        some_blue = (0, 170, 204)
        white = (255, 255, 255)
        font = pygame.font.SysFont("Times", 32)                        #SysFont(name, size, bold=False, italic=False) -> Font. Set the Font and Font size to be used.
        if self.selection == True:                                                                      #self.selection == True when a single cell is selected. If so draw a Rectangle surface that higlight cell borders.
            pygame.draw.rect(screen, some_blue, (cell_x, cell_y, cell_measuremt, cell_measuremt), 4)    #rect(surface, color, rect, width=0, ... ) -> Rect. rect = (position: x & y and dimension: width & height) -> (x, y, w, h).
                                                                                                        #If width > 0, used for line thickness. The surface parameter is the surface to draw on.
        if self.value != 0:                                                               #Draws self.value onto a single cell, of which is not an empty cell. That is, self.value is a number already present in the board. 
            text = font.render(str(self.value), True, white)                              #render(text, antialias, color, background=None) -> Surface. Font.render() creates an image(Surface) of the text, & blit it onto another surface (screen).
            screen.blit(text, (cell_x +(cell_measuremt/2), cell_y +(cell_measuremt/2)))   #The antialias argument is a boolean: if true, characters will have smooth edges. blit(source, dest, area=None, special_flags=0) -> Rect. 
                                                                                          #Dest can be coordinates repping upper left corner of the source. So, add (cell_measuremt/2) to x & y to place self.value in exact middle of a single cell.
        elif self.value == 0 and self.temporary_value != 0:                             
            text = font.render(str(self.temporary_value), True, gray)                     #Draws self.temporary_value onto an empty cell (self.value == 0). So, self.temporary_value is a number that has yet to be committed to an empty cell,
            screen.blit(text, (cell_x +(cell_measuremt/2), cell_y +(cell_measuremt/2)))   #or what can be described as the number that is 'sketched' into an empty cell as the user's workings.

    def draw_outcome(self, screen, outcome):                            #Method draws an Aqua rectangle around the borders of a cell if the outcome of the inserted value is True, Fuchsia if False.
        aqua = (77, 255, 255)                                           #Method will be invoked when the board is running the algorithm and is checking the worked cells for their validity. Since algorithm will be running through
        fuchsia = (255, 0, 255)                                         #every cell that was initially empty, each cell must be filled with a Rect surface so that we can blit self.value onto the surface of each worked cell.
        black = (0, 0, 0)                                               #Rectangle surface of all worked cells must match the background of the main screen interface, which will be black.
        cell_measuremt = (self.height / 9)
        cell_x = (self.column * cell_measuremt)
        cell_y = (self.row * cell_measuremt)
        font = pygame.font.SysFont("Times", 32)
        pygame.draw.rect(screen, black, (cell_x, cell_y, cell_measuremt, cell_measuremt), 0)   #When width == 0, the Rectangle surface that's drawn will be filled; width > 0 is only used for line thickness; screen is the surface to draw on.
                                                                                               #This allows program to blit a number (image) into the cell, as cell would have a Rectangle surface within its borders. 
        text = font.render((str(self.value), True, white))                                     #Creates a surface (image) of the text (self.value), and then blit this surface onto another surface (screen).
        screen.blit(text, (cell_x + (cell_measuremt/2), cell_y + (cell_measuremt/2)))
        
        if outcome == True:                                                                    #outcome == True occurs when the value inserted into the empty cell returns True when it is checked to be valid with the harmony function.
            pygame.draw.rect(screen, aqua, (cell_x, cell_y, cell_measuremt, cell_measuremt), 4)
        else:                                                                                     #outcome == False occurs when the above circumstance returns False when it is checked to be invalid with the harmony function.
            pygame.draw.rect(screen, fuchsia, (cell_x, cell_y, cell_measuremt, cell_measuremt), 4)



class Global_Grid:                                                      #A Global_Grid instance will hold all Single_Cell instances.

    sudoku_board = [                                                    #Adjust board manually if user wants to change the board/difficulty.
    [5, 0, 0, 1, 8, 0, 0, 7, 0],                                        #sudoku_board object represents the starting grid of filled cells.
    [0, 0, 7, 2, 9, 0, 5, 4, 3],
    [0, 0, 0, 0, 0, 4, 0, 0, 1],
    [0, 5, 0, 6, 0, 0, 9, 8, 0],
    [7, 0, 0, 9, 0, 0, 3, 0, 4],
    [0, 9, 6, 3, 0, 8, 2, 1, 5],
    [0, 0, 5, 8, 0, 0, 0, 0, 6],
    [1, 4, 0, 0, 6, 0, 0, 0, 2],
    [0, 3, 0, 0, 2, 7, 1, 0, 0]]

    def __init__(self, rows, columns, width, height, screen):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.screen = screen
        self.selection = None
        self.singlecells = [Single_Cell(self.sudoku_board[row][column], row, column, width, height)     
                            for row in range(rows) for column in range(columns)]
                                                                                    #self.singlecells is a list of Single_Cell instances, which is a list of all the cells from the sudoku board.
    white = (255, 255, 255)
    gray = (128, 128, 128)                                              #pygame.draw.line(surface, color, start_pos, end_pos, width) -> Rect. start_pos & end_pos receive (x, y) coordinates (as Tuples or List).
    def draw_grid(self, screen):                                        #Draw grid lines. Major grid lines are white, minor grid lines are gray.
        cell_width = (self.width / 9)                                   #Divide width into 9 equal cells.
        for n in range(self.column + 1):                                #There are 10 vertical and horizontal lines dividing cells equally, so self.column + 1 includes very last vertical & horizontal line to iterator: [0,1,2,3,4,5,6,7,8,9].
            if n % 3 == 0:                                              #Apply same logic in make_board() function from sudoku_txtv1.py to modulo operations. Thicker lines are n = 0, 3, 6, 9. Thin lines are the remaining n values.
                line_width = 3                                          #Default line width = 1.  Width < 1 = nothing will be drawn.
            else:
                line_width = 1
            if line_width == 3:                                                                                      #First vertical and horizontal line: cellwidth*0, last vertical and horizontal line: cellwidth*9.
                pygame.draw.line(screen, white, ((cell_width * n), 0), ((cell_width * n), self.height), line_width)  #Draws vertical major grid lines, starting from y = 0.
                pygame.draw.line(screen, white, (0, (cell_width * n)), (self.width, (cell_width * n)), line_width)   #Draws horizontal major grid lines, starting from x = 0.
            elif line_width == 1:
                pygame.draw.line(screen, gray, ((cell_width * n), 0), ((cell_width * n), self.height), line_width)   #Draws vertical minor grid lines, starting from y = 0.
                pygame.draw.line(screen, gray, (0, (cell_width * n)), (self.width, (cell_width * n)), line_width)    #Draws horizontal minor grid lines, starting from x = 0.

    def reset_and_select(self, row, column):
        for x in range(self.rows):                                      #Method assigns (row, column) coordinates to self.selection.
            for y in range(self.columns):

                self.singlecells[x][y].selection = False                #Reset all self.selection in self.singlecells list to False. So that when a Single_Cell instance is
                                                                        #selected again, only this Single_Cell instance will have self.selection == True.
        self.singlecells[row][column].selection = True                  #Then assign the coordinates of this selected Single_Cell instance to self.selection.
        self.selection = (row, column)

    def clear_cell(self):                                               #Method enables an empty and unworked cell to remain clear of any number. If self.value is 0, it means cell is empty and should not display any number including 0.
        (row, column) = self.selection                                  #Unpack coordinates, and set self.tempory_value = 0 in order to not meet all the conditionals of the draw_single_cell method of the Single_Cell instance,
        if self.singlecells[row][column].value == 0:                    #so that draw_single_cell method does not blit self.temporary_value = 0 onto the surface of the empty and unworked cell and it remains clear of any number.
            self.singlecells[row][column].insert_temporary_value(0)

    def sketch_cell(self, value):                                       #Method allows user to sketch a draft number into an empty cell, by giving the cell a temporary value.
        (row, column) = self.selection
        self.singlecells[row][column].insert_temporary_value(value)

    def







def main_window():
    #Construct a visible screen interface:
    screenwidth = 800
    screenheight = 920
    screen = pygame.display.set_mode([screenwidth, screenheight])       #set_mode(size=(0, 0), flags=0, depth=0, display=0) -> set screen size.
    background = pygame.Surface(screen.get_size())                      #Surface((width, height), flags=0, depth=0, masks=None) -> create background surface. #get_size() -> (width, height)
    background.fill((0, 0, 0))                                          #fill(color, rect=None, special_flags=0) -> Rect color = (r, g, b)
    background.convert()                                                #change the pixel format of an image; convert(Surface=None) -> Surface
    screen.blit(background, (0,0))                                      #background surface is not visible on its own. blit background surface to the screen.
                                                                        #blit(source, dest, area=None, special_flags=0) -> Rect. Upper left corner of 'background' is on position (0, 0) on the screen.
    
    mainloop = True                                                     #mainloop represents pygame window.
    #construct pygame events handler:
#    while mainloop == True:                                             #If pygame window is still running:
#        for event in pygame.event.get():                                #get events from the queue, get(eventtype=None) -> Event List
#            if event.type == pygame.QUIT:                               #if event.type is a QUIT event, uninitialize all pygame modules, 
#                mainloop = False                                        #pygame window closed by user.
#            elif event.type == pygame.KEYDOWN:                          #else & if event.type is a KEYDOWN event, i.e, a key is pressed, set function of pressed keys, using pygame key constants.
#                if event.key == pygame.K_1:                             #every KEYDOWN event has a key and a mod. Refer to pygame.key documentation for list of constants and their representations.
#                    key = 1
#                if event.key == pygame.K_2:
#                    key = 2
#                if event.key == pygame.K_3:
#                    key = 3
#                if event.key == pygame.K_4:
#                    key = 4
#                if event.key == pygame.K_5:
#                    key = 5
#                if event.key == pygame.K_6:
#                    key = 6
#                if event.key == pygame.K_7:
#                    key = 7
#                if event.key == pygame.K_8:
#                    key = 8
#                if event.key == pygame.K_9:
#                    key = 9
                #needs 2 more keys: enter(return) and delete (to reset all empty cells) - see pygame.key for documentation.
                #needs event.type == pygame.MOUSEBUTTONDOWN - refer to pygame.mouse for documentation.





main_window() #test function