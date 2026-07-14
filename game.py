from tkinter import *
window = Tk()
TURN = 0

board = Canvas(window, width=600, height=600, bg='white')
bg = PhotoImage(file= 'board.png')
x = PhotoImage(file='x.png')
o = PhotoImage(file='O.png')

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
    1: (100,100), 2: (300,100), 3: (500,100),
    4: (100,300), 5: (300,300), 6: (500,300),
    7: (100,500), 8: (300,500), 9: (500,500),
}

def game(cell):
    global TURN
    shape = x if TURN % 2 == 0 else o
    x_coord,y_coord = hitbox_centres[cell]
    board.create_image(x_coord,y_coord, image= shape)
    TURN += 1  
    
window.mainloop()