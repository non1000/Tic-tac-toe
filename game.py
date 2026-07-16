from tkinter import *
window = Tk()
TURN = 0
record_x =[]
record_o =[]

board = Canvas(window, width=600, height=600, bg='white')

bg = PhotoImage(file= 'board.png')
x = PhotoImage(file='x.png')
o = PhotoImage(file='O.png')
win_x = PhotoImage(file='Win_screen_X.png')
win_o = PhotoImage(file='Win_screen_O.png')
draw = PhotoImage(file='draw.png')
gameover = PhotoImage(file= 'game_over.png')

board.create_image(305, 305, image = bg)
board.pack()

hitbox_1 = board.create_rectangle(0,0,209,204,fill='white', outline='white')
board.tag_bind(hitbox_1,'<Button-1>', lambda event: game(1))
hitbox_2 = board.create_rectangle(218,0,412,204,fill='white', outline='white')
board.tag_bind(hitbox_2,'<Button-1>', lambda event: game(2))
hitbox_3 = board.create_rectangle(423,0,600,204,fill='white', outline='white')
board.tag_bind(hitbox_3,'<Button-1>', lambda event: game(3))

hitbox_4 = board.create_rectangle(0,214,209,400,fill='white', outline='white')
board.tag_bind(hitbox_4,'<Button-1>', lambda event: game(4))
hitbox_5 = board.create_rectangle(218,214,412,400,fill='white', outline='white')
board.tag_bind(hitbox_5,'<Button-1>', lambda event: game(5))
hitbox_6 = board.create_rectangle(422,214,600,400,fill='white', outline='white')
board.tag_bind(hitbox_6,'<Button-1>', lambda event: game(6))

hitbox_7 = board.create_rectangle(0,412,209,600,fill='white', outline='white')
board.tag_bind(hitbox_7,'<Button-1>', lambda event: game(7))
hitbox_8 = board.create_rectangle(218,412,412,600,fill='white', outline='white')
board.tag_bind(hitbox_8,'<Button-1>', lambda event: game(8))
hitbox_9 = board.create_rectangle(422,412,600,600,fill='white', outline='white')
board.tag_bind(hitbox_9,'<Button-1>', lambda event: game(9))

hitbox_centres = {
    1: (110,110), 2: (310,110), 3: (510,110),
    4: (110,310), 5: (310,310), 6: (510,310),
    7: (110,510), 8: (310,510), 9: (510,510),
}

def game(hitbox):
    global TURN
    shape = x if TURN % 2 == 0 else o
    x_coord,y_coord = hitbox_centres[hitbox]
    board.create_image(x_coord,y_coord, image= shape)
    TURN += 1
    
    if shape == x:
        record_x.append((x_coord,y_coord))
    else:
        record_o.append((x_coord,y_coord))
    
    def victory_screen():
        if shape == x:
            congrats = win_x
        else:
            congrats = win_o
        popup = Toplevel(window)
        winner =Label(popup, width=1234, height= 559, image= congrats)
        winner.pack()
        board.create_image(305, 305, image = gameover)
    
#For X
#horizontal
    if (110,110) in record_x and (310,110) in record_x and (510,110) in record_x :
        victory_screen()
    if (110,310) in record_x and (310,310) in record_x and (510,310) in record_x :
        victory_screen()
    if (110,510) in record_x and (310,510) in record_x and (510,510) in record_x :
        victory_screen()
#vertical
    if (110,110) in record_x and (110,310) in record_x and (110,510) in record_x :
        victory_screen()
    if (310,110) in record_x and (310,310) in record_x and (310,510) in record_x :
        victory_screen()
    if (510,110) in record_x and (510,310) in record_x and (510,510) in record_x :
        victory_screen()
#diagonal
    if (110,110) in record_x and (310,310) in record_x and (510,510) in record_x :
        victory_screen()
    if (510,110) in record_x and (310,310) in record_x and (110,510) in record_x :
        victory_screen()
#For O
#horizontal
    if (110,110) in record_o and (310,110) in record_o and (510,110) in record_o :
        victory_screen()
    if (110,310) in record_o and (310,310) in record_o and (510,310) in record_o :
        victory_screen()
    if (110,510) in record_o and (310,510) in record_o and (510,510) in record_o :
        victory_screen()
#vertical
    if (110,110) in record_o and (110,310) in record_o and (110,510) in record_o :
        victory_screen()
    if (310,110) in record_o and (310,310) in record_o and (310,510) in record_o :
        victory_screen()
    if (510,110) in record_o and (510,310) in record_o and (510,510) in record_o :
        victory_screen()
#diagonal
    if (110,110) in record_o and (310,310) in record_o and (510,510) in record_o :
        victory_screen()
    if (510,110) in record_o and (310,310) in record_o and (110,510) in record_o :
        victory_screen()

#draw
    if TURN == 9:
        popup = Toplevel(window)
        nowin = Label(popup, width=1234, height= 559, image= draw)
        nowin.pack()
        board.create_image(305, 305, image = gameover)  
        
window.mainloop()