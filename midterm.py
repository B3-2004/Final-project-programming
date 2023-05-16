import tkinter
from tkinter import *
import time
import random

root = tkinter.Tk()
root.title("Game")
h = 760
w = 1400
canvas = tkinter.Canvas(root, width=w, height=h, bg = 'white')
canvas.pack()

# the forest coordinates are x = 0-34 and y = 0-18
# forest = 0, pathways = 1, player = 5, npc = 20, buildings = 10, entrances >= 100
castle_entry = 0
village_entry = 0
house_entry = 0
ruins_entry = 0
deepforest_entry = 0

axe = True
castle_key = False
shovel = False
key = False
money = 0
timer = time.time()


# forest
forest = [[0 for i in range(int(h/40))] for j in range(int(w/40))]
for i in range(int(w/40)):
    for j in range(int(h/40)):
        canvas.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill = 'dark olive green')

# castle drawing
def castle_drawing(x, y):
    forest[x][y] = 10
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'grey')
c = [castle_drawing(26, 4), castle_drawing(27, 4), castle_drawing(29, 4), castle_drawing(30, 4),
     castle_drawing(26, 3), castle_drawing(27, 3), castle_drawing(28, 3), castle_drawing(29, 3),
     castle_drawing(30, 3), castle_drawing(26, 2), castle_drawing(30, 2), castle_drawing(28, 2)]

# village drawing
def village(x, y, color):
    forest[x][y] = 10
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = color)
v1 = [village(12, 5, 'goldenrod3'), village(12, 4, 'goldenrod3'), village(13, 5, 'goldenrod3'),village(13, 4, 'goldenrod3'),
      village(12, 3, 'orange4'), village(13, 3, 'orange4'), village(11, 4, 'orange4'), village(14, 4, 'orange4')]
v2 = [village(16, 6, 'goldenrod3'), village(16, 7, 'goldenrod3'), village(17, 6, 'goldenrod3'), village(17, 7, 'goldenrod3'),
      village(16, 5, 'orange4'), village(15, 6, 'orange4'), village(17, 5, 'orange4'), village(18, 6, 'orange4')]
v3 = [village(12, 8, 'goldenrod3'), village(11, 9, 'goldenrod3'), village(12, 9, 'goldenrod3'), village(13, 9, 'goldenrod3'),
      village(10, 9, 'orange4'), village(11, 8, 'orange4'), village(12, 7, 'orange4'), village(13, 8, 'orange4'), village(14, 9, 'orange4')]

# house drawing
def house(x, y, color):
    forest[x][y] = 10
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = color)
p = [house(31, 16, 'gray90'), house(29, 16, 'gray90'), house(31, 15, 'gray90'), house(29, 15, 'gray90'), house(30, 15, 'gray90'),
     house(28, 14, 'hotpink2'), house(29, 14, 'hotpink2'), house(30, 14, 'hotpink2'), house(31, 14, 'hotpink2'), house(32, 14, 'hotpink2'), house(29, 13, 'hotpink2'),
     house(30, 13, 'hotpink2'), house(31, 13, 'hotpink2'), house(30, 12, 'hotpink2')]

# ruins drawing
def wall(x, y):
    forest[x][y] = 10
    colour = random.choice(['grey80', 'grey60'])
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = colour)
w = [wall(2, 10), wall(2, 11), wall(3, 11), wall(4, 10), wall(5, 11), wall(2, 14), wall(3, 13),
     wall(5, 13), wall(5, 14), wall(6, 14), wall(7, 13), wall(7, 14), wall(8, 14), wall(9, 13),
     wall(9, 14), wall(10, 14), wall(3, 16), wall(3, 17), wall(4, 17), wall(5, 17), wall(6, 16),
     wall(6, 17), wall(8, 16), wall(9, 16)]


# pathways drawings
def path(x, y):
    forest[x][y] = 1
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'tan3')
path = [path(18, 16), path(19, 17), path(19, 16), path(10, 17), path(9, 17),
        path(20, 17), path(21, 17), path(22, 17), path(20, 16), path(21, 16), path(22, 16), path(20, 15), path(21, 15), path(23, 16), path(24, 16),
        path(24, 17), path(25, 17), path(26, 17), path(27, 16), path(28, 17), path(29, 17), path(30, 17), path(22, 15),
        path(21, 14), path(19, 14), path(23, 14), path(23, 13), path(20, 13), path(21, 13), path(20, 12), path(21, 12), path(19, 12), path(21, 11),
        path(22, 11), path(22, 10), path(23, 10), path(22, 9), path(22, 8), path(22, 6), path(23, 7), path(23, 8), path(24, 6), path(24, 7),
        path(24, 8), path(25, 6), path(26, 6), path(26, 7), path(27, 6), path(28, 6), path(28, 5), path(19, 11), path(18, 11), path(17, 11), path(17, 10),
        path(16, 10), path(17, 12), path(16, 12), path(16, 13), path(15, 13), path(14, 13), path(13, 13), path(13, 14), path(13, 15), path(14, 15),
        path(12, 15), path(12, 16), path(13, 17), path(11, 16), path(11, 17), path(8, 17), path(7, 17),
        path(12, 13), path(12, 12), path(11, 12), path(11, 11), path(10, 11), path(9, 11), path(8, 11), path(8, 10), path(7, 10), path(7, 9), path(6, 9),
        path(6, 8), path(5, 8), path(4, 8), path(4, 7), path(3, 7), path(2, 7), path(2, 6), path(2, 5), path(1, 6), path(1, 4), path(2, 3), path(2, 2),
        path(3, 3), path(3, 4), path(3, 5), path(4, 4), path(4, 4), path(4, 5), path(5, 2), path(5, 4), path(5, 5), path(6, 4), path(6, 5), path(6, 6),
        path(7, 6), path(7, 3), path(8, 6), path(8, 5), path(9, 7), path(9, 6), path(10, 7), path(10, 16), path(11, 6), path(10, 6), path(27, 17),
        path(24, 5), path(24, 4), path(23, 4), path(23, 3), path(22, 3), path(21, 3)]

# entering the buildings, red entrance
def entrance(x, y, ID):
    forest[x][y] = ID
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'red4')
e = [entrance(28, 4, 100), entrance(30, 16, 101), entrance(7, 17, 102), entrance(11, 6, 103), entrance(21, 2, 104)]

# NPCs
def npc_location(x, y):
    forest[x][y] = 20
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'black')
    canvas.create_rectangle(x*40+10, y*40+10, x*40+15, y*40+15, fill = 'white')
    canvas.create_rectangle(x*40+25, y*40+10, x*40+30, y*40+15, fill = 'white')
npc = [npc_location(18, 15)]

def NPC_text(text, x, y, bubble_width, bubble_height, bubble_padding, time):
    b = canvas.create_rectangle(x, y, x + bubble_width, y + bubble_height, fill="white", outline="")
    text_x = x + bubble_padding
    text_y = y + bubble_padding
    bt = canvas.create_text(text_x, text_y, anchor="nw", text=text, width=bubble_width - 2 * bubble_padding, font=("Arial", 12), fill="black")
    root.after(time, lambda: canvas.delete(b))
    root.after(time, lambda: canvas.delete(bt))

def bind_forest_keys():
    canvas.focus_set()
    canvas.bind('<Up>', move_up)
    canvas.bind('<Down>', move_down)
    canvas.bind('<Left>', move_left)
    canvas.bind('<Right>', move_right)
    canvas.bind('<space>', interacting)

# main character
x, y = 20, 17
canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey10')
forest[x][y] = 5

def close_bubble():
    global b_instructions, bt_instructions, bt2_instructions, bt3_instructions
    canvas.delete(b)
    canvas.delete(bt)
    canvas.delete(bt2)
    canvas.delete(bt3)
    
    canvas.delete(b_instructions)
    canvas.delete(bt_instructions)
    canvas.delete(bt2_instructions)
    canvas.delete(bt3_instructions)
    
    canvas.delete('ok_button') 
    canvas.delete('instructions_button') 

def instructions():
    global b_instructions, bt_instructions, bt2_instructions, bt3_instructions
    def close_instructions():
        canvas.delete(b_instructions)
        canvas.delete(bt_instructions)

    b_instructions = canvas.create_rectangle(500, 230, 900, 530, fill="white")
    bt_instructions = canvas.create_text(700, 280, text="Arrow keys to move", font=("Arial", 30), fill="black", justify="center")
    bt2_instructions = canvas.create_text(700, 350, text="Space to interact, Talk with People, Cut, Dig, Open and search", font=("Arial", 20), width=300, fill="black", justify="center")
    bt3_instructions = canvas.create_text(700, 420, text="Press M, to show your acquired money", font=("Arial", 20), width=300, fill="black", justify="center")
 
b_instructions, bt_instructions, bt2_instructions, bt3_instructions = 0,0,0,0 
b = canvas.create_rectangle(500, 230, 900, 530, fill="white")
bt = canvas.create_text(700, 280, text="The Enchanting Forest", font=("Arial", 30), fill="black", justify="center")
bt2 = canvas.create_text(700, 350, text="The goal of the game is to enter the pink house", font=("Arial", 20), width=400, fill="black", justify="center")
bt3 = canvas.create_text(700, 420, text="Do what you must. Good luck!", font=("Arial", 20), width=200, fill="black", justify="center")
ok_button = Button(root, text="OK", command=close_bubble)
ok_button_id = canvas.create_window(650, 480, window=ok_button, tags='ok_button')
instructions_button = Button(root, text="Instructions", command=instructions)
instructions_button_id = canvas.create_window(750, 480, window=instructions_button, tags='instructions_button')

def money_f(event):
    global money
    m = canvas.create_rectangle(10, 10, 80, 50, fill="white")
    mt = canvas.create_text(45, 30, text=f"{money}$", font=("Arial", 20), fill="black")
    root.after(1500, lambda: canvas.delete(m))
    root.after(1500, lambda: canvas.delete(mt))

#the blinking, interaction with surroundings(space bar) - NPC
def interacting(event):
    global x, y
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if forest[i][j] == 20:
                print("NPC at", i, j)
                if i == 18 and j == 15:
                    NPC_text("Hi! I'm Baptiste. I live in the white and pink house over there", i*40+45, j*40-50, 150, 60, 10, 2500)
                    root.after(2500, lambda: NPC_text("The goal of the game is to enter my home", i*40+5, j*40-100, 150, 40, 8, 2500))
                    root.after(5000, lambda: NPC_text("Good luck!", i*40+5, j*40-75, 100, 30, 8, 2000))
    canvas.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='red')
    root.after(50, lambda: canvas.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10'))
    
def show(x, y):
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'grey10')
    forest[x][y] = 5

def show2(x, y):
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'tan3')
    forest[x][y] = 1

def re_spawn(x, y):
    global castle_entry, village_entry, house_entry, ruins_entry, deepforest_entry
    
    if castle_entry == 1:
        x, y = 28, 5
        forest[x][y] = 5
        castle_entry = 0
        
    if village_entry == 1:
        x, y = 10, 6
        forest[x][y] = 5
        village_entry = 0
    
    if house_entry == 1:
        x, y = 30, 17
        forest[x][y] = 5
        house_entry = 0
    
    if ruins_entry == 1:
        x, y = 8, 17
        forest[x][y] = 5
        ruins_entry = 0
    
    if deepforest_entry == 1:
        x, y = 21, 3
        forest[x][y] = 5
        deepforest_entry = 0
    
    return x, y

# these are to move, add a square in front, make the current dissapear, using the show and show2 functions

def move_up(event):
    global x, y
    x, y = re_spawn(x, y)
    if forest[x][y] == 5:
        if forest[x][y-1] >= 100:
            check_entrance(x, y-1)
        if forest[x][y-1] == 1:
            show(x, y-1)
            show2(x, y)
            x, y = x, y-1

def move_down(event):
    global x, y
    x, y = re_spawn(x, y)
    if forest[x][y] == 5:
        if (forest[x][y+1] == 1 or forest[x][y+1] >= 100):
            check_entrance(x, y+1)
            show(x, y+1)
            show2(x, y)
            x, y = x, y+1
    
def move_left(event):
    global x, y
    x, y = re_spawn(x, y)
    if forest[x][y] == 5:
        if (forest[x-1][y] == 1 or forest[x-1][y] >= 100):
            check_entrance(x-1, y)
            show(x-1, y)
            show2(x, y)
            x, y = x-1, y
    
def move_right(event):
    global x, y
    x, y = re_spawn(x, y)
    if forest[x][y] == 5:
        if (forest[x+1][y] == 1 or forest[x+1][y] >= 100):
            check_entrance(x+1, y)
            show(x+1, y)
            show2(x, y)
            x, y = x+1, y

def check_entrance(x, y):
    global castle_entry, village_entry, house_entry, ruins_entry, deepforest_entry, timer
    print("Checking entrance at", x, y,', number:', forest[x][y])
    if forest[x][y] == 100:
        print("Entering building at", x, y)
        castle_entry = 1
        castle_entrance()
        bind_forest_keys()
        return True
    if forest[x][y] == 103:
        print("Entering building at", x, y)
        village_entry = 1 
        village_entrance()
        bind_forest_keys()
        return True
    if forest[x][y] == 101 and key == True:
        print("Entering building at", x, y)
        house_entry = 1 
        house_entrance()
        bind_forest_keys()
        return True
    if forest[x][y] == 101 and key == False:
        NPC_text("The door is locked", 1060, 640, 130, 30, 10, 2500)
    if forest[x][y] == 102:
        print("Entering building at", x, y)
        ruins_entry = 1 
        ruins_entrance()
        bind_forest_keys()
        return True
    if forest[x][y] == 104:
        print("Entering building at", x, y)
        deepforest_entry = 1 
        deepforest_entrance()
        bind_forest_keys()
        return True
    return False
    

#===============================================================================================================================================
#===============================================================================================================================================

def castle_entrance():
    global x, y, castle_key, money
    castle_window = tkinter.Toplevel(root)
    castle_window.title("Castle")
    h = 760
    w = 1400
    castle = tkinter.Canvas(castle_window, width=w, height=h, bg='white')
    castle.pack()
    exited_castle = False
    
    # gold = 15, floor = 1, walls = 10, door = 20, door key = 25

    castle_grid = [[2 for i in range(int(h/40))] for j in range(int(w/40))]
    for i in range(int(w / 40)):
        for j in range(int(h / 40)):
            castle.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='darkolivegreen')
    
    def c_walls(x, y):
        castle.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey30')
        castle_grid[x][y] = 10
    c = [c_walls(15, 15), c_walls(14, 15), c_walls(13, 15), c_walls(12, 15), c_walls(11,15), c_walls(10, 15), c_walls(9, 16),
         c_walls(8, 17), c_walls(7, 17), c_walls(6, 17), c_walls(5, 17), c_walls(4, 17), c_walls(3, 16), c_walls(2, 15), c_walls(2, 14),
         c_walls(2, 13), c_walls(3, 12), c_walls(4, 11), c_walls(4, 10), c_walls(4, 9), c_walls(4, 8), c_walls(3, 7), c_walls(2, 6),
         c_walls(2, 5), c_walls(2, 4), c_walls(3, 3), c_walls(4, 2), c_walls(5, 2), c_walls(6, 2), c_walls(7, 2), c_walls(8, 2),
         c_walls(9, 3), c_walls(10, 4), c_walls(11, 4), c_walls(12, 4), c_walls(13,4), c_walls(14, 4), c_walls(15, 4), c_walls(16, 4),
         c_walls(17, 4), c_walls(18, 4), c_walls(19, 4), c_walls(20, 4), c_walls(21, 4), c_walls(22, 4), c_walls(23, 4), c_walls(24, 4),
         c_walls(25, 3), c_walls(26, 2), c_walls(27, 2), c_walls(28, 2), c_walls(29, 2), c_walls(30, 2), c_walls(31, 3), c_walls(32, 4),
         c_walls(32, 5), c_walls(32, 6), c_walls(31, 7), c_walls(30, 8), c_walls(30, 9), c_walls(30, 10), c_walls(30, 11), c_walls(31, 12),
         c_walls(32, 13), c_walls(32, 14), c_walls(32, 15), c_walls(31, 16), c_walls(30, 17), c_walls(29, 17), c_walls(28, 17), c_walls(27, 17),
         c_walls(26, 17), c_walls(25, 16), c_walls(24, 15), c_walls(23, 15), c_walls(22, 15), c_walls(21, 15), c_walls(20, 15), c_walls(19, 15),
         c_walls(9, 11), c_walls(10, 12), c_walls(11, 12), c_walls(12, 12), c_walls(13, 12), c_walls(14, 12), c_walls(15, 12), c_walls(16, 12),
         c_walls(17, 12), c_walls(18, 12), c_walls(19, 12), c_walls(20, 12), c_walls(21, 12), c_walls(22, 12), c_walls(23, 12), c_walls(24, 12),
         c_walls(25, 11), c_walls(25, 10), c_walls(25, 9), c_walls(25, 8), c_walls(24, 7), c_walls(23, 7), c_walls(22, 7), c_walls(21, 7),
         c_walls(20, 7), c_walls(19, 7), c_walls(18, 7), c_walls(17, 7), c_walls(16, 7), c_walls(15, 7), c_walls(14, 7), c_walls(13, 7),
         c_walls(12, 7), c_walls(11, 7), c_walls(10, 7), c_walls(9, 8), c_walls(9, 9), c_walls(9, 10)]
    
    def floor(x, y):
        castle.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey')
        castle_grid[x][y] = 1
    for i in range(18):
        for j in range(34):
            if (i == 5 and 2 < j < 32) or (i == 6 and 2 < j < 32) or (i == 13 and 2 < j < 32) or (i == 14 and 2 < j < 32):
                floor(j, i)
            if (j==5 and 2<i<17) or (j==6 and 2<i<17) or (j==7 and 2<i<17) or (j==8 and 2<i<17) or (j==26 and 2<i<17)or (j==27 and 2<i<17) or (j==28 and 2<i<17) or (j==29 and 2<i<17):
                floor(j, i)
    f = [floor(4, 3), floor(4, 4), floor(3, 4), floor(4, 7), floor(9, 4), floor(9, 7), floor(4, 12), floor(4, 15), floor(4, 16),
         floor(3, 15), floor(9, 12), floor(9, 15), floor(30, 3), floor(30, 4), floor(30, 7), floor(31, 4), floor(25, 4), floor(25, 7),
         floor(25, 12), floor(25, 15), floor(30, 12), floor(30, 15), floor(30, 16), floor(31, 15), floor(16, 18), floor(16, 17), floor(16, 16),
         floor(16, 15), floor(17, 15), floor(17, 16), floor(17, 17), floor(18, 15), floor(18, 16), floor(18, 17), floor(18, 18)]
    
    c2 = [c_walls(10, 5), c_walls(10, 6), c_walls(8, 8), c_walls(7, 8), c_walls(6, 8)]
    
    def gold(x, y):
        castle.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='goldenrod')
        castle_grid[x][y] = 15
            
    g = [gold(3, 6), gold(3, 5), gold(3, 4), gold(4, 3), gold(5, 3), gold(5, 4), gold(5, 5), gold(5, 6), gold(6, 4), gold(6, 5),
         gold(7, 4), gold(7, 5), gold(7, 6), gold(9, 4), gold(9, 5), gold(9, 6), gold(9, 7), gold(6, 3), gold(7, 3), gold(8, 3),
         gold(8, 4), gold(8, 5), gold(8, 7), gold(4, 7), gold(7, 7), gold(4, 4), gold(4, 5), gold(31, 4), gold(31, 6), gold(30, 3),
         gold(29, 3), gold(26, 16), gold(27, 16), gold(25, 12), gold(4, 16) ]
    
    def special(x, y, colour, number):
        castle.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill=colour)
        castle_grid[x][y] = number
    s = [special(5, 8, 'saddle brown', 20), special(13, 4, 'grey20', 25)]
    
    #character
    x, y = 17, 16
    castle.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey10')
    castle_grid[x][y] = 5
    
    #exit
    castle.create_rectangle(17*40, 18*40, 17*40+40, 18*40+40, fill='red4')
    castle_grid[17][18] = 100
    
    
    b = castle.create_rectangle(500, 330, 900, 430, fill="white")
    bt = castle.create_text(700, 380, text="You've entered the castle", font=("Arial", 30), fill="black", justify="center")
    castle_window.after(1500, lambda: castle.delete(b))
    castle_window.after(1500, lambda: castle.delete(bt))
    
    def money_f(event):
        global money
        m = castle.create_rectangle(10, 10, 80, 50, fill="white")
        mt = castle.create_text(45, 30, text=f"{money}$", font=("Arial", 20), fill="black")
        castle_window.after(1500, lambda: castle.delete(m))
        castle_window.after(1500, lambda: castle.delete(mt))
    
    def NPC_text(text, x, y, bubble_width, bubble_height, bubble_padding, time):
        b = castle.create_rectangle(x, y, x + bubble_width, y + bubble_height, fill="white", outline="")
        text_x = x + bubble_padding
        text_y = y + bubble_padding
        bt = castle.create_text(text_x, text_y, anchor="nw", text=text, width=bubble_width - 2 * bubble_padding, font=("Arial", 12), fill="black")
        castle_window.after(time, lambda: castle.delete(b))
        castle_window.after(time, lambda: castle.delete(bt))
    
    def interacting(event):
        global x, y, castle_key, money
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if castle_grid[i][j] == 20 and castle_key == True:
                    castle.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='grey')
                    castle_grid[i][j] = 1
                if castle_grid[i][j] == 20 and castle_key == False:
                    NPC_text("the door is locked", i*40-20, j*40-20, 120, 30, 8, 1000)
                if castle_grid[i][j] == 25:
                    castle_key = True
                    NPC_text("you found a small key", i*40-20, j*40-20, 145, 30, 8, 1000)
                if castle_grid[i][j] == 15:
                    money += 2
                    castle.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='grey')
                    castle_grid[i][j] = 1
                    
        castle.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='red')
        castle_window.after(50, lambda: castle.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10'))
    
    def show_castle(x, y):
        castle.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10')
        castle_grid[x][y] = 5

    def show2_castle(x, y):
        castle.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey')
        castle_grid[x][y] = 1
    
    def exiting(x, y):
        nonlocal exited_castle
        print("Checking exit at", x, y,', number:', castle_grid[x][y])
        if castle_grid[x][y] == 100:
            print("Exiting building at", x, y)
            castle.unbind_all('<Up>')
            castle.unbind_all('<Down>')
            castle.unbind_all('<Left>')
            castle.unbind_all('<Right>')
            exited_castle = True
            castle_window.destroy()
            bind_forest_keys()
            return True
        return False

    def move_up_castle(event):
        global x, y
        if castle_grid[x][y] == 5:
            if (castle_grid[x][y-1] == 1 or castle_grid[x][y-1] >= 100):
                exited = exiting(x, y-1)
                if exited: return
                show_castle(x, y-1)
                show2_castle(x, y)
                x, y = x, y-1

    def move_down_castle(event):
        global x, y
        if castle_grid[x][y] == 5:
            if (castle_grid[x][y+1] == 1 or castle_grid[x][y+1] >= 100):
                exited = exiting(x, y+1)
                if exited: return
                show_castle(x, y+1)
                show2_castle(x, y)
                x, y = x, y+1

    def move_left_castle(event):
        global x, y
        if castle_grid[x][y] == 5:
            if (castle_grid[x-1][y] == 1 or castle_grid[x-1][y] >= 100):
                exited = exiting(x-1, y)
                if exited: return
                show_castle(x-1, y)
                show2_castle(x, y)
                x, y = x-1, y

    def move_right_castle(event):
        global x, y
        if castle_grid[x][y] == 5:
            if (castle_grid[x+1][y] == 1 or castle_grid[x+1][y] >= 100):
                exited = exiting(x+1, y)
                if exited: return
                show_castle(x+1, y)
                show2_castle(x, y)
                x, y = x+1, y

    

    castle.focus_set()
    castle.bind_all('<Up>', move_up_castle)
    castle.bind_all('<Down>', move_down_castle)
    castle.bind_all('<Left>', move_left_castle)
    castle.bind_all('<Right>', move_right_castle)
    castle.bind_all('<space>', interacting)
    castle.bind_all('<m>', money_f)
        
    castle_window.mainloop()

    return exited_castle

#===============================================================================================================================================
#===============================================================================================================================================

def village_entrance():
    global x, y, money, axe
    import random
    village_window = tkinter.Toplevel(root)
    village_window.title("village")
    h = 760
    w = 1400
    village = tkinter.Canvas(village_window, width=w, height=h, bg='white')
    village.pack()
    exited_village = False

    village_grid = [[1 for i in range(int(h/40))] for j in range(int(w/40))]
    for i in range(int(w / 40)):
        for j in range(int(h / 40)):
            village.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='dark olive green')
    
    def houses(x, y):
        village.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='tan4')
        village_grid[x][y] = 10
    h = [houses(1, 16), houses(2, 16), houses(3, 16), houses(1, 15), houses(2, 15), houses(1, 14), houses(2, 14), houses(1, 13),
         houses(2, 13), houses(1, 12), houses(2, 12), houses(3, 12), houses(10, 16), houses(10, 15), houses(10, 14), houses(10, 13),
         houses(11, 16), houses(11, 15), houses(11, 14), houses(11, 13), houses(12, 16), houses(12, 15), houses(12, 14), houses(12, 13),
         houses(10, 10), houses(10, 9), houses(10, 8), houses(10, 7), houses(11, 10), houses(11, 9), houses(11, 8), houses(11, 7),
         houses(12, 10), houses(12, 9), houses(12, 8), houses(12, 7), houses(9,9), houses(9,8), houses(13, 9), houses(13, 8), houses(2, 6),
         houses(2, 5), houses(2, 4), houses(2, 3), houses(2, 2), houses(3, 6), houses(3, 5), houses(3, 4), houses(3, 3), houses(3, 2),
         houses(4, 6), houses(4, 5), houses(4, 4), houses(4, 3), houses(4, 2), houses(5, 3), houses(5, 2), houses(6, 3), houses(6, 2),
         houses(7, 3), houses(7, 2), houses(8, 3), houses(8, 2), houses(9, 3), houses(9, 2), houses(10, 3), houses(10, 2), houses(28, 17),
         houses(28, 16), houses(29, 17), houses(29, 16), houses(30, 17), houses(30, 16), houses(31, 17), houses(31, 16), houses(32, 17),
         houses(32, 16), houses(33, 17), houses(33, 16), houses(33, 15), houses(33, 14), houses(33, 13), houses(33, 13), houses(33, 12),
         houses(33, 11), houses(32, 11), houses(32, 12), houses(31, 11), houses(31, 12), houses(30, 12), houses(30, 11), houses(29, 11),
         houses(29, 12), houses(29, 13), houses(29, 14), houses(28, 11), houses(28, 12), houses(28, 13), houses(28, 14), houses(30, 8),
         houses(30, 7), houses(31, 8), houses(31, 7), houses(32, 8), houses(32, 7), houses(23, 12), houses(24, 12), houses(16, 2), houses(16, 3),
         houses(29, 2), houses(29, 3), houses(33, 2), houses(33, 3)]
    for x in range(18, 25):
        for y in range(7, 12):
            houses(x, y)
    for x in range(16, 34):
        for y in range(1, 2):
            houses(x, y)
        for y in range(4, 5):
            houses(x, y)
    
    def more(x, y, colour):
        village.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill=colour)
        village_grid[x][y] = 10
    m = [more(3, 15, 'tan3'), more(3, 14, 'tan3'), more(3, 13, 'tan3'), more(5, 4, 'tan3'), more(6, 4, 'tan3'), more(7, 4, 'tan3'),
         more(8, 4, 'tan3'), more(9, 4, 'tan3'), more(10, 4, 'tan3'), more(18, 7, 'tan3'), more(18, 8, 'tan3'), more(18, 9, 'tan3'),
         more(18, 10, 'tan3'), more(18, 11, 'tan3'), more(30, 2, 'steelblue'), more(30, 3, 'steelblue'), more(31, 2, 'steelblue'),
         more(31, 3, 'steelblue'), more(32, 2, 'steelblue'), more(32, 3, 'steelblue')]
    for x in range(17, 29):
        for y in range(2, 4):
            more(x, y, 'yellow green')
    
    def baskets(x, y):
        village.create_oval(x*40, y*40, x*40+40, y*40+40, fill='red3')
        village_grid[x][y] = 15
    b = [baskets(32, 15), baskets(32, 14), baskets(21, 12), baskets(20, 12), baskets(19, 12), baskets(9, 16), baskets(9, 15),
         baskets(4, 15), baskets(4, 14), baskets(4, 13), baskets(13, 10), baskets(14, 9), baskets(5, 4), baskets(6, 4), baskets(5, 5)]
    
    #character
    x, y = 17, 16
    village.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey10')
    village_grid[x][y] = 5
    
    #exit
    village.create_rectangle(17*40, 18*40, 17*40+40, 18*40+40, fill='red4')
    village_grid[17][18] = 100
    
    
    b = village.create_rectangle(500, 330, 900, 430, fill="white")
    bt = village.create_text(700, 380, text="You've entered the village", font=("Arial", 30), fill="black", justify="center")
    village_window.after(1500, lambda: village.delete(b))
    village_window.after(1500, lambda: village.delete(bt))
    
    def money_f(event):
        global money
        m = village.create_rectangle(10, 10, 80, 50, fill="white")
        mt = village.create_text(45, 30, text=f"{money}$", font=("Arial", 20), fill="black")
        village_window.after(1500, lambda: village.delete(m))
        village_window.after(1500, lambda: village.delete(mt))
    
    def show_village(x, y):
        village.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10')
        village_grid[x][y] = 5

    def show2_village(x, y):
        village.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='dark olive green')
        village_grid[x][y] = 1
    
    def npc_location(x, y):
        village_grid[x][y] = 20
        village.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'black')
        village.create_rectangle(x*40+10, y*40+10, x*40+15, y*40+15, fill = 'white')
        village.create_rectangle(x*40+25, y*40+10, x*40+30, y*40+15, fill = 'white')
    npc = [npc_location(30, 13), npc_location(31, 5), npc_location(26, 7), npc_location(23, 13),
           npc_location(15, 1), npc_location(9, 5), npc_location(8, 13), npc_location(4, 16)]

    def NPC_text(text, x, y, bubble_width, bubble_height, bubble_padding, time):
        b = village.create_rectangle(x, y, x + bubble_width, y + bubble_height, fill="white", outline="")
        text_x = x + bubble_padding
        text_y = y + bubble_padding
        bt = village.create_text(text_x, text_y, anchor="nw", text=text, width=bubble_width - 2 * bubble_padding, font=("Arial", 12), fill="black")
        village_window.after(time, lambda: village.delete(b))
        village_window.after(time, lambda: village.delete(bt))
    
    def interacting(event):
        global x, y, money, axe
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if village_grid[i][j] == 15:
                    village.create_oval(i*40, j*40, i*40+40, j*40+40, fill='grey30')
                    money+=1
                    village_grid[i][j] = 10
                    print(money)
                if village_grid[i][j] == 20:
                    print("NPC at", i, j)
                    if i == 23 and j == 13:
                        NPC_text("Hello traveler, welcome to the Great village of the Forest.", i*40+45, j*40-10, 150, 60, 10, 2500)
                        village_window.after(2600, lambda: NPC_text("If you need anything just ask the villagers", i*40+5, j*40-80, 150, 50, 10, 2500))
                    if i == 26 and j == 7:
                        NPC_text("Good morning traveller, I'm John.", i*40+45, j*40-10, 150, 50, 10, 2500)
                        village_window.after(2700, lambda: NPC_text("You look new. I hope you have a nice stay!", i*40+5, j*40-80, 150, 50, 10, 3000))
                    if i == 31 and j == 5:
                        NPC_text("Howdy, traveler! I see you've stumbled upon my humble farm.", i*40-5, j*40-70, 150, 60, 10, 3000)
                        village_window.after(3100, lambda: NPC_text(" Hard work and a touch of nature's magic make these crops thrive.", i*40-45, j*40-145, 150, 60, 10, 3000))
                        village_window.after(6300, lambda: NPC_text("If you're looking for fresh vegetables, I'm your guy", i*40-45, j*40-145, 150, 60, 10, 3000))
                    if i == 15 and j == 1:
                        NPC_text("Please don't talk to me i'm having a bad day", i*40+45, j*40-10, 150, 50, 10, 2500)
                    if i == 9 and j == 5:
                        NPC_text("Hey, stranger! What brings you to our village? You should come to my shop!", i*40-15, j*40-75, 150, 70, 10, 3500)
                    if i == 8 and j == 13:
                        NPC_text("Goodbye.", i*40+45, j*40-10, 70, 30, 7, 1000)
                    if i == 4 and j == 16:
                        NPC_text("Welcome to the best shop of the village!", i*40-130, j*40-55, 140, 50, 10, 2500)
                    if i == 30 and j == 13 and money < 80:
                        NPC_text("If you want an axe, it will cost you 80$.", i*40-5, j*40-55, 130, 40, 8, 2600)
                        village_window.after(2700, lambda: NPC_text(f"You only have {money}$", i*40-45, j*40-140, 130, 40, 8, 3000))
                    if i == 30 and j == 13 and money >= 80:
                        NPC_text("Nice! You have enough money for an axe.", i*40-5, j*40-55, 130, 50, 8, 2600)
                        village_window.after(2700, lambda: NPC_text("Here you go.", i*40-45, j*40-140, 100, 30, 8, 3000))
                        axe = True
                        
        village.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='red')
        village_window.after(50, lambda: village.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10'))
    
    def exiting(x, y):
        nonlocal exited_village
        print("Checking exit at", x, y,', number:', village_grid[x][y])
        if village_grid[x][y] == 100:
            print("Exiting building at", x, y)
            village.unbind_all('<Up>')
            village.unbind_all('<Down>')
            village.unbind_all('<Left>')
            village.unbind_all('<Right>')
            exited_village = True
            village_window.destroy()
            bind_forest_keys()
            return True
        return False

    def move_up_village(event):
        global x, y
        if village_grid[x][y] == 5:
            if (village_grid[x][y-1] == 1 or village_grid[x][y-1] >= 100):
                exited = exiting(x, y-1)
                if exited: return
                show_village(x, y-1)
                show2_village(x, y)
                x, y = x, y-1

    def move_down_village(event):
        global x, y
        if village_grid[x][y] == 5:
            if (village_grid[x][y+1] == 1 or village_grid[x][y+1] >= 100):
                exited = exiting(x, y+1)
                if exited: return
                show_village(x, y+1)
                show2_village(x, y)
                x, y = x, y+1

    def move_left_village(event):
        global x, y
        if village_grid[x][y] == 5:
            if (village_grid[x-1][y] == 1 or village_grid[x-1][y] >= 100):
                exited = exiting(x-1, y)
                if exited: return
                show_village(x-1, y)
                show2_village(x, y)
                x, y = x-1, y

    def move_right_village(event):
        global x, y
        if village_grid[x][y] == 5:
            if (village_grid[x+1][y] == 1 or village_grid[x+1][y] >= 100):
                exited = exiting(x+1, y)
                if exited: return
                show_village(x+1, y)
                show2_village(x, y)
                x, y = x+1, y
    

    village.focus_set()
    village.bind_all('<Up>', move_up_village)
    village.bind_all('<Down>', move_down_village)
    village.bind_all('<Left>', move_left_village)
    village.bind_all('<Right>', move_right_village)
    village.bind_all('<space>', interacting)
    village.bind_all('<m>', money_f)
        
    village_window.mainloop()

    return exited_village

#===============================================================================================================================================
#===============================================================================================================================================

def house_entrance():
    global x, y, key, money, timer
    house_window = tkinter.Tk()
    house_window.title("house")
    h = 760
    w = 1400
    house = tkinter.Canvas(house_window, width=w, height=h, bg='white')
    house.pack()
    exited_house = False

    house_grid = [[1 for i in range(int(h/40))] for j in range(int(w/40))]
    for i in range(int(w / 40)):
        for j in range(int(h / 40)):
            house.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='mistyrose3')
    
    
    b = house.create_rectangle(480, 330, 920, 430, fill="white")
    bt = house.create_text(700, 380, text="You've entered the pink house", font=("Arial", 30), fill="black", justify="center")
    house_window.after(1500, lambda: house.delete(b))
    house_window.after(1500, lambda: house.delete(bt))
    
    def money_f(event):
        global money
        m = house.create_rectangle(10, 10, 80, 50, fill="white")
        mt = house.create_text(45, 30, text=f"{money}$", font=("Arial", 20), fill="black")
        house_window.after(1500, lambda: house.delete(m))
        house_window.after(1500, lambda: house.delete(mt))
    
    #character
    x, y = 17, 16
    house.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey10')
    house_grid[x][y] = 5
    
    #exit
    house.create_rectangle(17*40, 18*40, 17*40+40, 18*40+40, fill='red4')
    house_grid[17][18] = 100
    
    def show_house(x, y):
        house.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10')
        house_grid[x][y] = 5

    def show2_house(x, y):
        house.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='mistyrose2')
        house_grid[x][y] = 1
    
    def npc_location(x, y):
        house_grid[x][y] = 20
        house.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'black')
        house.create_rectangle(x*40+10, y*40+10, x*40+15, y*40+15, fill = 'white')
        house.create_rectangle(x*40+25, y*40+10, x*40+30, y*40+15, fill = 'white')
    npc = [npc_location(17, 3)]

    def NPC_text(text, x, y, bubble_width, bubble_height, bubble_padding, time):
        b = house.create_rectangle(x, y, x + bubble_width, y + bubble_height, fill="white", outline="")
        text_x = x + bubble_padding
        text_y = y + bubble_padding
        bt = house.create_text(text_x, text_y, anchor="nw", text=text, width=bubble_width - 2 * bubble_padding, font=("Arial", 15), fill="black")
        house_window.after(time, lambda: house.delete(b))
        house_window.after(time, lambda: house.delete(bt))
    
    def interacting(event):
        global x, y, money, timer
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if house_grid[i][j] == 20:
                    if i == 17 and j == 3:
                        timer = int(time.time() - timer)
                        NPC_text("Congratulations", i*40-45, j*40-55, 130, 40, 12, 2500)
                        house_window.after(2500, lambda: NPC_text("You've just finished the Game", i*40-120, j*40-140, 230, 40, 12, 2500))
                        house_window.after(5000, lambda: NPC_text(f"You acquired {int(((money)/85)*100)}% of the gold available", i*40-120, j*40-140, 230, 55, 12, 2500))
                        house_window.after(7500, lambda: NPC_text(f"You took {timer}s to finish the game", i*40-120, j*40-140, 230, 55, 12, 2500))
                        house_window.after(10000, lambda: NPC_text(f"Your Final Score is {int(money*(300/timer))} points", i*40-120, j*40-140, 230, 55, 12, 2500))
                        
        house.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='red')
        house_window.after(50, lambda: house.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10'))
    
    
    def exiting(x, y):
        nonlocal exited_house
        print("Checking exit at", x, y,', number:', house_grid[x][y])
        if house_grid[x][y] == 100:
            print("Exiting building at", x, y)
            house.unbind_all('<Up>')
            house.unbind_all('<Down>')
            house.unbind_all('<Left>')
            house.unbind_all('<Right>')
            exited_house = True
            house_window.destroy()
            bind_forest_keys()
            return True
        return False

    def move_up_house(event):
        global x, y
        if house_grid[x][y] == 5:
            if (house_grid[x][y-1] == 1 or house_grid[x][y-1] >= 100):
                exited = exiting(x, y-1)
                if exited: return
                show_house(x, y-1)
                show2_house(x, y)
                x, y = x, y-1

    def move_down_house(event):
        global x, y
        if house_grid[x][y] == 5:
            if (house_grid[x][y+1] == 1 or house_grid[x][y+1] >= 100):
                exited = exiting(x, y+1)
                if exited: return
                show_house(x, y+1)
                show2_house(x, y)
                x, y = x, y+1

    def move_left_house(event):
        global x, y
        if house_grid[x][y] == 5:
            if (house_grid[x-1][y] == 1 or house_grid[x-1][y] >= 100):
                exited = exiting(x-1, y)
                if exited: return
                show_house(x-1, y)
                show2_house(x, y)
                x, y = x-1, y

    def move_right_house(event):
        global x, y
        if house_grid[x][y] == 5:
            if (house_grid[x+1][y] == 1 or house_grid[x+1][y] >= 100):
                exited = exiting(x+1, y)
                if exited: return
                show_house(x+1, y)
                show2_house(x, y)
                x, y = x+1, y
    

    house.focus_set()
    house.bind_all('<Up>', move_up_house)
    house.bind_all('<Down>', move_down_house)
    house.bind_all('<Left>', move_left_house)
    house.bind_all('<Right>', move_right_house)
    house.bind_all('<space>', interacting)
    house.bind_all('<m>', money_f)
        
    house_window.mainloop()

    return exited_house

#===============================================================================================================================================
#===============================================================================================================================================

def ruins_entrance():
    global x, y, shovel, key, money
    ruins_window = tkinter.Tk()
    ruins_window.title("ruins")
    h = 760
    w = 1400
    ruins = tkinter.Canvas(ruins_window, width=w, height=h, bg='white')
    ruins.pack()
    exited_ruins = False
    
    # walls = 10, floor = 1, floordig1 = 2, floordig2 = 3, key = 20

    ruins_grid = [[1 for i in range(int(h/40))] for j in range(int(w/40))]
    for i in range(int(w / 40)):
        for j in range(int(h / 40)):
            ruins.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='dark olive green')
    
    def walls(x, y):
        colour = random.choice(['grey80', 'grey60'])
        ruins.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill=colour, width=1)
        ruins_grid[x][y] = 10
    w = [walls(1, 9), walls(1, 10), walls(2, 10), walls(4, 17), walls(5, 17), walls(6, 17), walls(5, 16), walls(5, 14), walls(5, 15),
         walls(5, 14), walls(5, 13), walls(5, 12), walls(5, 11), walls(5, 10), walls(4, 10), walls(6, 10), walls(7, 10), walls(8, 10),
         walls(7, 11), walls(7, 12), walls(7, 13), walls(10, 15), walls(10, 16), walls(10, 17), walls(11, 16), walls(11, 17), walls(12, 17),
         walls(13, 13), walls(13, 14), walls(13, 15), walls(13, 16), walls(13, 17), walls(14, 17), walls(15, 9), walls(16, 9), walls(16, 10),
         walls(17, 10), walls(18, 10), walls(19, 10), walls(20, 10), walls(18, 11), walls(19, 11), walls(19, 12), walls(19, 13), walls(19, 14),
         walls(19, 15), walls(20, 15), walls(22, 17), walls(23, 17), walls(24, 17), walls(24, 16), walls(23, 16), walls(23, 15), walls(23, 14),
         walls(23, 13), walls(23, 12), walls(23, 11), walls(27, 17), walls(28, 17), walls(29, 17), walls(30, 17), walls(31, 17), walls(32, 17),
         walls(33, 17), walls(29, 16), walls(29, 15), walls(29, 14), walls(29, 13), walls(29, 12), walls(29, 11), walls(29, 10), walls(28, 10),
         walls(30, 10), walls(31, 10), walls(32, 10), walls(33, 10), walls(31, 11), walls(31, 12), walls(31, 13), walls(31, 14), walls(31, 15),
         walls(31, 16), walls(32, 16), walls(2, 1), walls(2, 2), walls(2, 3), walls(3, 1), walls(3, 2), walls(4, 1), walls(5,1), walls(6, 1),
         walls(7,1), walls(8,1), walls(9,1), walls(10,1), walls(11,1), walls(12,1), walls(13,1), walls(14,1), walls(15,1), walls(16,1), walls(6, 2),
         walls(7, 2), walls(8, 2), walls(7, 3), walls(7, 4), walls(7, 5), walls(7, 6), walls(13, 2), walls(14, 2), walls(15, 2), walls(14, 3),
         walls(14, 4), walls(14, 5), walls(14, 6), walls(14, 7), walls(13, 7), walls(17, 7), walls(18, 7), walls(18, 6), walls(19, 5), walls(19, 1),
         walls(20,1), walls(21, 1), walls(22, 1), walls(23, 1), walls(24, 1), walls(25, 1), walls(26, 1), walls(27, 1), walls(28, 1), walls(21, 2),
         walls(22, 2), walls(21, 3), walls(21, 4), walls(21, 5), walls(21, 6), walls(21, 7), walls(21, 8), walls(25, 2), walls(26, 2), walls(27, 2),
         walls(26, 3), walls(26, 4), walls(26, 5), walls(26,6), walls(26,7), walls(26,8)]
    
    b = ruins.create_rectangle(500, 330, 900, 430, fill="white")
    bt = ruins.create_text(700, 380, text="You've entered the ruins", font=("Arial", 30), fill="black", justify="center")
    ruins_window.after(1500, lambda: ruins.delete(b))
    ruins_window.after(1500, lambda: ruins.delete(bt))
    
    #character
    x, y = 17, 16
    ruins.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey10')
    ruins_grid[x][y] = 5
    
    #exit
    ruins.create_rectangle(17*40, 18*40, 17*40+40, 18*40+40, fill='red4')
    ruins_grid[17][18] = 100
    
    def money_f(event):
        global money
        m = ruins.create_rectangle(10, 10, 80, 50, fill="white")
        mt = ruins.create_text(45, 30, text=f"{money}$", font=("Arial", 20), fill="black")
        ruins_window.after(1500, lambda: ruins.delete(m))
        ruins_window.after(1500, lambda: ruins.delete(mt))
        
    def NPC_text(text, x, y, bubble_width, bubble_height, bubble_padding, time):
        b = ruins.create_rectangle(x, y, x + bubble_width, y + bubble_height, fill="white", outline="")
        text_x = x + bubble_padding
        text_y = y + bubble_padding
        bt = ruins.create_text(text_x, text_y, anchor="nw", text=text, width=bubble_width - 2 * bubble_padding, font=("Arial", 12), fill="black")
        ruins_window.after(time, lambda: ruins.delete(b))
        ruins_window.after(time, lambda: ruins.delete(bt))
    
    def interacting(event):
        global x, y, key, shovel
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if shovel == True and ruins_grid[i][j] == 2 and (ruins_grid[i][j] != 100 and ruins_grid[i][j] != 10 and ruins_grid[i][j] != 20):
                    ruins.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='darkolivegreen3')
                    ruins_grid[i][j] = 3
                if shovel == True and ruins_grid[i][j] == 1 and (ruins_grid[i][j] != 100 and ruins_grid[i][j] != 10 and ruins_grid[i][j] != 20):
                    ruins.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='darkolivegreen4')
                    ruins_grid[i][j] = 2
                if i == 6 and j == 11 and key == False and ruins_grid[i][j] == 3:
                    ruins_grid[i][j] = 20
                    ruins.create_rectangle(6*40, 11*40, 6*40+40, 11*40+40, fill='gold')
                    ruins.create_rectangle(245, 452, 258, 468, fill='black')
                    ruins.create_rectangle(247, 457, 275, 461, fill='black')
                    ruins.create_rectangle(272, 457, 275, 469, fill='black')
                    ruins.create_rectangle(265, 457, 268, 467, fill='black')
                    ruins.create_rectangle(248, 455, 255, 465, fill='gold')
                    NPC_text("Press Y", i*40-20, j*40-50, 100, 30, 8, 1500)
                
        ruins_grid[x][y] = 5        
        ruins.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='red')
        ruins_window.after(50, lambda: ruins.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10'))
        
    def key_acquisition(event):
        global x, y, shovel, key
        print('key found')
        if 5 <= x <= 7 and 10 <= y <= 12 and key == False:
            ruins.create_rectangle(6*40, 11*40, 6*40+40, 11*40+40, fill='darkolivegreen3')
            ruins_grid[6][11] = 1
            key = True
            NPC_text("You have acquired the final House Key", 6*40+45, 11*40-50, 140, 40, 8, 2500)
    
    def show_ruins(x, y):
        ruins.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10')
        ruins_grid[x][y] = 5

    def show2_ruins(x, y, colour):
        ruins.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill=colour)
        ruins_grid[x][y] = 1
    
    def exiting(x, y):
        nonlocal exited_ruins
        print("Checking exit at", x, y,', number:', ruins_grid[x][y])
        if ruins_grid[x][y] == 100:
            print("Exiting building at", x, y)
            ruins.unbind_all('<Up>')
            ruins.unbind_all('<Down>')
            ruins.unbind_all('<Left>')
            ruins.unbind_all('<Right>')
            exited_ruins = True
            ruins_window.destroy()
            bind_forest_keys()
            return True
        return False

    def colouring(x, y):
        if ruins_grid[x][y] == 1:
            return 'darkolivegreen'
        if ruins_grid[x][y] == 2:
            return 'darkolivegreen4'
        if ruins_grid[x][y] == 3:
            return 'darkolivegreen3'
            

    def move_up_ruins(event):
        global x, y
        colour = colouring(x, y-1)
        if ruins_grid[x][y] == 5:
            if (ruins_grid[x][y-1] <= 3 or ruins_grid[x][y-1] >= 100):
                exited = exiting(x, y-1)
                if exited: return
                show_ruins(x, y-1)
                show2_ruins(x, y, colour)
                x, y = x, y-1

    def move_down_ruins(event):
        global x, y
        colour = colouring(x, y+1)
        if ruins_grid[x][y] == 5:
            if (ruins_grid[x][y+1] <= 3 or ruins_grid[x][y+1] >= 100):
                exited = exiting(x, y+1)
                if exited: return
                show_ruins(x, y+1)
                show2_ruins(x, y, colour)
                x, y = x, y+1

    def move_left_ruins(event):
        global x, y
        colour = colouring(x-1, y)
        if ruins_grid[x][y] == 5:
            if (ruins_grid[x-1][y] <= 3 or ruins_grid[x-1][y] >= 100):
                exited = exiting(x-1, y)
                if exited: return
                show_ruins(x-1, y)
                show2_ruins(x, y, colour)
                x, y = x-1, y

    def move_right_ruins(event):
        global x, y
        colour = colouring(x+1, y)
        if ruins_grid[x][y] == 5:
            if (ruins_grid[x+1][y] <= 3 or ruins_grid[x+1][y] >= 100):
                exited = exiting(x+1, y)
                if exited: return
                show_ruins(x+1, y)
                show2_ruins(x, y, colour)
                x, y = x+1, y
    

    ruins.focus_set()
    ruins.bind_all('<Up>', move_up_ruins)
    ruins.bind_all('<Down>', move_down_ruins)
    ruins.bind_all('<Left>', move_left_ruins)
    ruins.bind_all('<Right>', move_right_ruins)
    ruins.bind_all('<space>', interacting)
    ruins.bind_all('<y>', key_acquisition)
    ruins.bind_all('<m>', money_f)

    ruins_window.mainloop()


#===============================================================================================================================================
#===============================================================================================================================================

def deepforest_entrance():
    global x, y, axe, shovel, money
    deepforest_window = tkinter.Toplevel(root)
    deepforest_window.title("deepforest")
    h = 760
    w = 1400
    deepforest = tkinter.Canvas(deepforest_window, width=w, height=h, bg='white')
    deepforest.pack()
    exited_deepforest = False
    
    deepforest_grid = [[2 for i in range(int(h/40))] for j in range(int(w/40))]
    for i in range(int(w / 40)):
        for j in range(int(h / 40)):
            deepforest.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='darkolivegreen')
    
    # initial starting pathway
    def path(x, y):
        deepforest.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='tan3')
        deepforest_grid[x][y] = 1
    p = [path(16, 18), path(18, 18), path(16, 17), path(17, 17), path(18, 17)]
    
    #character
    x, y = 17, 16
    deepforest.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey10')
    deepforest_grid[x][y] = 5
    
    #exit
    deepforest.create_rectangle(17*40, 18*40, 17*40+40, 18*40+40, fill='red4')
    deepforest_grid[17][18] = 100
    
    
    b = deepforest.create_rectangle(480, 330, 920, 430, fill="white")
    bt = deepforest.create_text(700, 380, text="You've entered the deep forest", font=("Arial", 30), fill="black", justify="center")
    deepforest_window.after(2500, lambda: deepforest.delete(b))
    deepforest_window.after(2500, lambda: deepforest.delete(bt))
    
    def money_f(event):
        global money
        m = deepforest.create_rectangle(10, 10, 80, 50, fill="white")
        mt = deepforest.create_text(45, 30, text=f"{money}$", font=("Arial", 20), fill="black")
        deepforest_window.after(1500, lambda: deepforest.delete(m))
        deepforest_window.after(1500, lambda: deepforest.delete(mt))
    
    def show_deepforest(x, y):
        deepforest.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10')
        deepforest_grid[x][y] = 5

    def show2_deepforest(x, y):
        deepforest.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='tan3')
        deepforest_grid[x][y] = 1
    
    def exiting(x, y):
        nonlocal exited_deepforest
        print("Checking exit at", x, y,', number:', deepforest_grid[x][y])
        if deepforest_grid[x][y] == 100:
            print("Exiting building at", x, y)
            deepforest.unbind_all('<Up>')
            deepforest.unbind_all('<Down>')
            deepforest.unbind_all('<Left>')
            deepforest.unbind_all('<Right>')
            exited_deepforest = True
            deepforest_window.destroy()
            bind_forest_keys()
            return True
        return False
    
    
    def interacting(event):
        global x, y, axe, shovel
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if axe == True and (deepforest_grid[i][j] != 100 and deepforest_grid[i][j] != 20):
                    deepforest.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='tan3')
                    deepforest_grid[i][j] = 1
                if i == 5 and j == 5 and shovel == False:
                    deepforest_grid[i][j] = 20
                    deepforest.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='gold')
                    deepforest.create_rectangle(217, 210, 223, 235, fill='saddle brown')
                    deepforest.create_rectangle(212, 205, 228, 217, fill='grey')
                    NPC_text("Press P", i*40-20, j*40-130, 100, 30, 8, 1500)
        
        deepforest_grid[x][y] = 5            
        deepforest.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='red')
        deepforest_window.after(50, lambda: deepforest.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey10'))
    
    def NPC_text(text, x, y, bubble_width, bubble_height, bubble_padding, time):
        b = deepforest.create_rectangle(x, y, x + bubble_width, y + bubble_height, fill="white", outline="")
        text_x = x + bubble_padding
        text_y = y + bubble_padding
        bt = deepforest.create_text(text_x, text_y, anchor="nw", text=text, width=bubble_width - 2 * bubble_padding, font=("Arial", 12), fill="black")
        deepforest_window.after(time, lambda: deepforest.delete(b))
        deepforest_window.after(time, lambda: deepforest.delete(bt))
    
    def shovel_acquisition(event):
        global x, y, shovel
        if 4 <= x <= 6 and 4 <= y <= 6 and shovel == False:
            deepforest.create_rectangle(5*40, 5*40, 5*40+40, 5*40+40, fill='tan3')
            deepforest_grid[5][5] = 1
            shovel = True
            NPC_text("You have acquired a shovel", 5*40+45, 5*40-50, 140, 40, 8, 2500)

    def move_up_deepforest(event):
        global x, y
        if deepforest_grid[x][y] == 5:
            if (deepforest_grid[x][y-1] == 1 or deepforest_grid[x][y-1] >= 100):
                exited = exiting(x, y-1)
                if exited: return
                show_deepforest(x, y-1)
                show2_deepforest(x, y)
                x, y = x, y-1

    def move_down_deepforest(event):
        global x, y
        if deepforest_grid[x][y] == 5:
            if (deepforest_grid[x][y+1] == 1 or deepforest_grid[x][y+1] >= 100):
                exited = exiting(x, y+1)
                if exited: return
                show_deepforest(x, y+1)
                show2_deepforest(x, y)
                x, y = x, y+1

    def move_left_deepforest(event):
        global x, y
        if deepforest_grid[x][y] == 5:
            if (deepforest_grid[x-1][y] == 1 or deepforest_grid[x-1][y] >= 100):
                exited = exiting(x-1, y)
                if exited: return
                show_deepforest(x-1, y)
                show2_deepforest(x, y)
                x, y = x-1, y

    def move_right_deepforest(event):
        global x, y
        if deepforest_grid[x][y] == 5:
            if (deepforest_grid[x+1][y] == 1 or deepforest_grid[x+1][y] >= 100):
                exited = exiting(x+1, y)
                if exited: return
                show_deepforest(x+1, y)
                show2_deepforest(x, y)
                x, y = x+1, y
    

    deepforest.focus_set()
    deepforest.bind_all('<Up>', move_up_deepforest)
    deepforest.bind_all('<Down>', move_down_deepforest)
    deepforest.bind_all('<Left>', move_left_deepforest)
    deepforest.bind_all('<Right>', move_right_deepforest)
    deepforest.bind_all('<space>', interacting)
    deepforest.bind_all('<p>', shovel_acquisition)
    deepforest.bind_all('<m>', money_f)
        
    deepforest_window.mainloop()

    return exited_deepforest


#===============================================================================================================================================
#===============================================================================================================================================


def quit_game(event):
    print('You quit the Game')
    return root.destroy()

bind_forest_keys()
canvas.bind('<Escape>', quit_game)
canvas.bind('<m>', money_f)
