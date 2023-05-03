import tkinter

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
def wall(x, y, color):
    forest[x][y] = 10
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = color)
w = [wall(2, 10, 'lightslateblue'), wall(2, 11, 'slateblue'), wall(3, 11, 'lightslateblue'), wall(4, 10, 'lightslateblue'), wall(5, 11, 'slateblue'), wall(2, 14, 'slateblue'), wall(3, 13, 'lightslateblue'),
     wall(5, 13, 'slateblue'), wall(5, 14, 'lightslateblue'), wall(6, 14, 'slateblue'), wall(7, 13, 'slateblue'), wall(7, 14, 'lightslateblue'), wall(8, 14, 'lightslateblue'), wall(9, 13, 'slateblue'),
     wall(9, 14, 'slateblue'), wall(10, 14, 'lightslateblue'), wall(3, 16, 'slateblue'), wall(3, 17, 'lightslateblue'), wall(4, 17, 'slateblue'), wall(5, 17, 'slateblue'), wall(6, 16, 'lightslateblue'),
     wall(6, 17, 'lightslateblue'), wall(8, 16, 'slateblue'), wall(9, 16, 'lightslateblue')]


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
        path(7, 6), path(7, 3), path(8, 6), path(8, 5), path(9, 7), path(9, 6), path(10, 7), path(10, 16), path(11, 6), path(10, 6), path(27, 17)]

# entering the buildings, red entrance
def entrance(x, y, ID):
    forest[x][y] = ID
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'red4')
e = [entrance(28, 4, 100), entrance(30, 16, 101), entrance(7, 17, 102), entrance(11, 6, 103)]

# NPCs
def npc_location(x, y):
    forest[x][y] = 20
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'black')
npc = [npc_location(18, 15), canvas.create_rectangle(730, 610, 735, 615, fill = 'white'), canvas.create_rectangle(745, 610, 750, 615, fill = 'white')]

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

#the blinking, interaction with surroundings(space bar)
def interacting(event):
    global x, y
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if forest[i][j] == 20:
                print("NPC at", i, j)
                if i == 18 and j == 15:
                    NPC_text("Hi! I'm Alfred. I live in the white and pink house over there", i*40+45, j*40-50, 150, 60, 10, 2500)
                    root.after(2500, lambda: NPC_text("If you're a traveller, I've heard of a magic key in the village. You should check it out!", i*40+5, j*40-100, 150, 70, 10, 4000))
                    root.after(6700, lambda: NPC_text("Good luck!", i*40+5, j*40-75, 100, 30, 10, 2000))
    canvas.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='red')
    root.after(50, lambda: canvas.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10'))
    
def show(x, y):
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'grey10')
    forest[x][y] = 5

def show2(x, y):
    canvas.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill = 'tan3')
    forest[x][y] = 1

def re_spawn(x, y):
    global castle_entry, village_entry, house_entry, ruins_entry
    
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
    
    return x, y

# these are to move, add a square in front, make the current dissapear

def move_up(event):
    global x, y
    x, y = re_spawn(x, y)
    if forest[x][y] == 5:
        if (forest[x][y-1] == 1 or forest[x][y-1] >= 100):
            check_entrance(x, y-1)
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
    global castle_entry, village_entry, house_entry, ruins_entry
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
    if forest[x][y] == 101:
        print("Entering building at", x, y)
        house_entry = 1 
        house_entrance()
        bind_forest_keys()
        return True
    if forest[x][y] == 102:
        print("Entering building at", x, y)
        ruins_entry = 1 
        ruins_entrance()
        bind_forest_keys()
        return True
    return False
    

#===============================================================================================================================================
#===============================================================================================================================================

def castle_entrance():
    global x, y
    castle_window = tkinter.Toplevel(root)
    castle_window.title("Castle")
    h = 760
    w = 1400
    castle = tkinter.Canvas(castle_window, width=w, height=h, bg='white')
    castle.pack()
    exited_castle = False

    castle_grid = [[1 for i in range(int(h/40))] for j in range(int(w/40))]
    for i in range(int(w / 40)):
        for j in range(int(h / 40)):
            castle.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='grey')
    
    #character
    x, y = 17, 16
    castle.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey10')
    castle_grid[x][y] = 5
    
    #exit
    castle.create_rectangle(17*40, 18*40, 17*40+40, 18*40+40, fill='red4')
    castle_grid[17][18] = 100
    
    def show_castle(x, y):
        castle.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10')
        castle_grid[x][y] = 5

    def show2_castle(x, y):
        castle.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey45')
        castle_grid[x][y] = 1
    
    def check_exit_status():
        if not exited_castle:
            castle_window.after(100, check_exit_status)
        else:
            castle_window.destroy()
            bind_forest_keys()
    
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
        
    check_exit_status()
    castle_window.mainloop()

    return exited_castle

#===============================================================================================================================================
#===============================================================================================================================================

def village_entrance():
    global x, y
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
            village.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='orange4')
    
    #character
    x, y = 17, 16
    village.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey10')
    village_grid[x][y] = 5
    
    #exit
    village.create_rectangle(17*40, 18*40, 17*40+40, 18*40+40, fill='red4')
    village_grid[17][18] = 100
    
    def show_village(x, y):
        village.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10')
        village_grid[x][y] = 5

    def show2_village(x, y):
        village.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='orange3')
        village_grid[x][y] = 1
    
    def check_exit_status():
        if not exited_village:
            village_window.after(100, check_exit_status)
        else:
            village_window.destroy()
            bind_forest_keys()
    
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
        
    check_exit_status()
    village_window.mainloop()

    return exited_village

#===============================================================================================================================================
#===============================================================================================================================================

def house_entrance():
    global x, y
    house_window = tkinter.Toplevel(root)
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
    
    def check_exit_status():
        if not exited_house:
            house_window.after(100, check_exit_status)
        else:
            house_window.destroy()
            bind_forest_keys()
    
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
        
    check_exit_status()
    house_window.mainloop()

    return exited_house



#===============================================================================================================================================
#===============================================================================================================================================

def ruins_entrance():
    global x, y
    ruins_window = tkinter.Toplevel(root)
    ruins_window.title("ruins")
    h = 760
    w = 1400
    ruins = tkinter.Canvas(ruins_window, width=w, height=h, bg='white')
    ruins.pack()
    exited_ruins = False

    ruins_grid = [[1 for i in range(int(h/40))] for j in range(int(w/40))]
    for i in range(int(w / 40)):
        for j in range(int(h / 40)):
            ruins.create_rectangle(i*40, j*40, i*40+40, j*40+40, fill='dark olive green')
    
    #character
    x, y = 17, 16
    ruins.create_rectangle(x*40, y*40, x*40+40, y*40+40, fill='grey10')
    ruins_grid[x][y] = 5
    
    #exit
    ruins.create_rectangle(17*40, 18*40, 17*40+40, 18*40+40, fill='red4')
    ruins_grid[17][18] = 100
    
    def show_ruins(x, y):
        ruins.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='grey10')
        ruins_grid[x][y] = 5

    def show2_ruins(x, y):
        ruins.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, fill='darkolivegreen4')
        ruins_grid[x][y] = 1
    
    def check_exit_status():
        if not exited_ruins:
            ruins_window.after(100, check_exit_status)
        else:
            ruins_window.destroy()
            bind_forest_keys()
    
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
            return True
        return False

    def move_up_ruins(event):
        global x, y
        if ruins_grid[x][y] == 5:
            if (ruins_grid[x][y-1] == 1 or ruins_grid[x][y-1] >= 100):
                exited = exiting(x, y-1)
                if exited: return
                show_ruins(x, y-1)
                show2_ruins(x, y)
                x, y = x, y-1

    def move_down_ruins(event):
        global x, y
        if ruins_grid[x][y] == 5:
            if (ruins_grid[x][y+1] == 1 or ruins_grid[x][y+1] >= 100):
                exited = exiting(x, y+1)
                if exited: return
                show_ruins(x, y+1)
                show2_ruins(x, y)
                x, y = x, y+1

    def move_left_ruins(event):
        global x, y
        if ruins_grid[x][y] == 5:
            if (ruins_grid[x-1][y] == 1 or ruins_grid[x-1][y] >= 100):
                exited = exiting(x-1, y)
                if exited: return
                show_ruins(x-1, y)
                show2_ruins(x, y)
                x, y = x-1, y

    def move_right_ruins(event):
        global x, y
        if ruins_grid[x][y] == 5:
            if (ruins_grid[x+1][y] == 1 or ruins_grid[x+1][y] >= 100):
                exited = exiting(x+1, y)
                if exited: return
                show_ruins(x+1, y)
                show2_ruins(x, y)
                x, y = x+1, y
    

    ruins.focus_set()
    ruins.bind_all('<Up>', move_up_ruins)
    ruins.bind_all('<Down>', move_down_ruins)
    ruins.bind_all('<Left>', move_left_ruins)
    ruins.bind_all('<Right>', move_right_ruins)
        
    check_exit_status()
    ruins_window.mainloop()

    return exited_ruins



#===============================================================================================================================================
#===============================================================================================================================================

def quit_game(event):
    print('You quit the Game')
    return root.destroy()

bind_forest_keys()
canvas.bind('<Escape>', quit_game)
