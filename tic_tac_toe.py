from tkinter import *
from tkinter import messagebox
from threading import Timer
import random
from subprocess import call 

# test = open('tic_tac_toe.py', 'r')
# data = test.read().strip()



# print(data)


root = Tk()


root.title('Tic-Tac-Toe')
player_turn= BooleanVar()
player_turn.set(True)
turn = IntVar()
x_counter = IntVar()
o_counter = IntVar()
tie_counter = IntVar()
game_over = BooleanVar()
game_over.set(False)


def clicked(btn):
    if btn["text"] == " ":
        if player_turn.get() == True:
            player_turn.set(False)
            btn['text'] = 'X'
            btn['fg'] = 'magenta'
            turn.set(turn.get() + 1)
            win()
        else:
            player_turn.set(True)
            btn['text'] = 'O'
            btn['fg'] = 'blue' 
            turn.set(turn.get() + 1)
            win()
        unclicked_buttons.remove(btn)
           
'''Once a button is clicked and the text inside the button is blank, the code checks whose turn it is based off of the turn variable
and then puts either an X or O into the text for the button once everything is complete the code changes the player's turn.'''





def win():
    if turn.get() == 9:
        tie_counter.set(tie_counter.get() + 1)
        canvas.itemconfig(ties, text = str(tie_counter.get()))
        messagebox.showinfo('WinDialog', 'Tie ... Press SPACE to clear!')
        game_over.set(True)

    for combo in rows + cols + diags:
        if combo[0]['text'] in 'XO' and combo[0]['text'] == combo[1]['text'] and combo[1]['text'] == combo[2]['text']:
            messagebox.showinfo('WinDialog', combo[0]['text']+ ' wins ... Press SPACE to clear!')
            if combo[0]['text'] == 'X':
                x_counter.set(x_counter.get() + 1)
                canvas.itemconfig(x_counter_text, text = str(x_counter.get()))
                game_over.set(True) 
            if combo[0]['text'] == 'O':
                o_counter.set(o_counter.get() + 1)
                canvas.itemconfig(o_counter_text, text = str(o_counter.get()))
                game_over.set(True)
    
    if game_over.get() == True:
        unclicked_buttons.clear()
        unclicked_buttons.extend(buttons)
        for btn in buttons:
            btn.configure(state='disabled')

def player_mode():
    call(['python', 'tic_tac_toe.py'])
     
'''Checks to make sure the text inside a button are all three x or all three o then makes a window stating who won. 
If the play turns out to be a tie then the tie variable is then added one.  also disables the buttons when someone wins. It also
dissables the buttons so no one can make another play until the game is reset.'''




canvas = Canvas(root, width=500, height=500, background='black')
canvas.grid(row=0, column=0, rowspan=20, columnspan=20)
canvas.create_text(260, 50, text="TIC-TAC-TOE", font = ("Comic Sans MS", 40), fill = 'white')
canvas.create_text(100, 425, text= "PLAYER 1", font= ("Comic Sans MS", 20), fill= 'white')
canvas.create_text(400, 425, text= "PLAYER 2", font= ("Comic Sans MS", 20), fill = 'white')
canvas.create_text(250, 425, text= "TIE", font= ("Comic Sans MS", 20), fill = 'white')
canvas.create_text(100, 400, text="X", font= ("Comic Sans MS", 30), fill = 'white')
canvas.create_text(400, 400, text="O", font= ("Comic Sans MS", 30), fill = 'white')
x_counter_text = canvas.create_text(100, 450, text= str(x_counter.get()), font= ("Comic Sans MS", 20), fill = 'magenta')
o_counter_text = canvas.create_text(400, 450, text= str(o_counter.get()),  font= ("Comic Sans MS", 20), fill= 'blue')
ties = canvas.create_text(250, 450, text= str(tie_counter.get()), font= ("Comic Sans MS", 20), fill = 'white')

'''Makes names that hold the accumulators that keep track of the score for each player and the amount of ties.
Also has the basic layout of the window witht the background and other text.'''




btn1 = Button(root,text=" ", highlightbackground='black', width=6,height=3,font=('Comic Sans MS','20'),command=lambda: clicked(buttons[0]))
btn1.grid(column=9, row=7)
btn2 = Button(root, text=" ",  highlightbackground='black', width=6,height=3,font=('Comic Sans MS','20'),command=lambda: clicked(buttons[1]))
btn2.grid(column=10, row=7)
btn3 = Button(root, text=" ",  highlightbackground='black',width=6,height=3,font=('Comic Sans MS','20'),command=lambda: clicked(buttons[2]))
btn3.grid(column=11, row=7)
btn4 = Button(root, text=" ",  highlightbackground='black',width=6,height=3,font=('Comic Sans MS','20'),command=lambda: clicked(buttons[3]))
btn4.grid(column=9, row=8)
btn5 = Button(root, text=" ",  highlightbackground='black',width=6,height=3,font=('Comic Sans MS','20'),command=lambda: clicked(buttons[4]))
btn5.grid(column=10, row=8)
btn6 = Button(root, text=" ", highlightbackground='black', width=6,height=3,font=('Comic Sans MS','20'),command=lambda: clicked(buttons[5]))
btn6.grid(column=11, row=8)
btn7 = Button(root, text=" ",  highlightbackground='black',width=6,height=3,font=('Comic Sans MS','20'),command=lambda: clicked(buttons[6]))
btn7.grid(column=9, row=9)
btn8 = Button(root, text=" ", highlightbackground='black', width=6,height=3,font=('Comic Sans MS','20'),command=lambda: clicked(buttons[7]))
btn8.grid(column=10, row=9)
btn9 = Button(root, text=" ",  highlightbackground='black',width=6,height=3,font=('Comic Sans MS','20'),command=lambda: clicked(buttons[8]))
btn9.grid(column=11, row=9)




buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
unclicked_buttons = buttons[::]

rows = ((btn1, btn2, btn3), (btn4, btn5, btn6), (btn7, btn8, btn9))
cols = tuple(zip(*rows))
diags = ((btn1, btn5, btn9), (btn3, btn5, btn7))

''' Creates 9 buttons that are placed on the canvas like a tic tac toe board and are linked to the above funtions. 
The text is blank because it changes based on whose turn it is. Also sorts the buttons based on rows colums and diagnols
to check who has won later.'''




def clear_boxes(event):
    game_over.set(False)
    for btn in buttons:
        btn['text'] = ' '
        btn.configure(state='normal')
    turn.set(0)
    unclicked_buttons.clear()
    unclicked_buttons.extend(buttons)
    
'''Clears the whole board and and enables the buttons to be pressed again'''



canvas.bind('<space>', clear_boxes)
canvas.focus_set()

root.mainloop()