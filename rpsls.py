import random
from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Rock Paper Scissor")

com_score, player_score, toggle = 0, 0, True

paper_l = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//paper_l.png")
paper_r = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//paper_r.png")
rock_l = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//rock_l.png")
rock_r = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//rock_r.png")
scissor_l = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//scissors_l.png")
scissor_r = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//scissors_r.png")
spock_l = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//spock_l.png")
spock_r = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//spock_r.png")
lizard_l = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//lizard_l.png")
lizard_r = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//lizard_r.png")
empty = PhotoImage(master=root, file="C://Users//Admin//Pictures//rock_paper_scissor_game//empty.png")

icon_list = (rock_l, paper_l, scissor_l, lizard_l, spock_l,
             rock_r, paper_r, scissor_r, lizard_r, spock_r,
             empty)

lbl = Label(root, text="Score : " + str(com_score) + " Score : " + str(player_score))
lbl.pack()

def create_btn(master, text=None, icon=None, row=0, col=0, state=None, relief='raised', command=None):
    btn = Button(master=master, text=text, relief=relief, state=state, command=command, bd=10, height=100, width=100)
    btn.grid(row=row, column=col)
    btn.configure(image=icon)
    return btn

def rock_paper_scissor(master, icon=icon_list):
    frm = Frame(master=master)
    frm.pack()

    rock_com = create_btn(frm, None, icon_list[0], 0, 0)
    paper_com = create_btn(frm, None, icon_list[1], 1, 0)
    scissor_com = create_btn(frm, None, icon_list[2], 2, 0)
    empty_com = create_btn(frm, None, icon_list[10], 1, 1, state=DISABLED, relief='flat')
    com_btn = create_btn(frm, None, icon_list[10], 1, 2)

    rock_player = create_btn(frm, None, icon_list[5], 0, 5,
                             command=lambda: play(icon_list[5], com_btn, player_btn, 'rock'))
    paper_player = create_btn(frm, None, icon_list[6], 1, 5,
                              command=lambda: play(icon_list[6], com_btn, player_btn, 'paper'))
    scissor_player = create_btn(frm, None, icon_list[7], 2, 5,
                                command=lambda: play(icon_list[7], com_btn, player_btn, 'scissor'))
    empty_player = create_btn(frm, None, icon_list[10], 1, 4, state=DISABLED, relief='flat')
    player_btn = create_btn(frm, None, icon_list[10], 1, 3)

    return frm

def rock_paper_scissor_lizard_spock(master):
    frm = Frame(master=master)
    frm.pack()

    rock_com = create_btn(frm, None, icon_list[0], 0, 0)
    paper_com = create_btn(frm, None, icon_list[1], 1, 0)
    scissor_com = create_btn(frm, None, icon_list[2], 2, 0)
    lizard_com = create_btn(frm, None, icon_list[3], 3, 0)
    spock_com = create_btn(frm, None, icon_list[4], 4, 0)
    empty_com = create_btn(frm, None, icon_list[10], 2, 1, state=DISABLED, relief='flat')
    com_btn = create_btn(frm, None, icon_list[10], 2, 2)

    rock_player = create_btn(frm, None, icon_list[5], 0, 5,
                             command=lambda: play(icon_list[5], com_btn, player_btn, 'rock', True))
    paper_player = create_btn(frm, None, icon_list[6], 1, 5,
                              command=lambda: play(icon_list[6], com_btn, player_btn, 'paper', True))
    scissor_player = create_btn(frm, None, icon_list[7], 2, 5,
                                command=lambda: play(icon_list[7], com_btn, player_btn, 'scissor', True))
    lizard_player = create_btn(frm, None, icon_list[8], 3, 5,
                               command=lambda: play(icon_list[8], com_btn, player_btn, 'lizard', True))
    spock_player = create_btn(frm, None, icon_list[9], 4, 5,
                              command=lambda: play(icon_list[9], com_btn, player_btn, 'spock', True))
    empty_player = create_btn(frm, None, icon_list[10], 2, 4, state=DISABLED, relief='flat')
    player_btn = create_btn(frm, None, icon_list[10], 2, 3)

    return frm

def play(image, dest1, dest2, player, rpsls=False):
    x = {"rock": icon_list[0], "paper": icon_list[1], "scissor": icon_list[2]}
    if rpsls:
        x.update({"lizard": icon_list[3], "spock": icon_list[4]})

    com = random.choice(list(x.keys()))
    dest1.configure(image=x.get(com))
    dest2.configure(image=image)

    global com_score, player_score

    if com == player:
        messagebox.showinfo(None, "Draw !")
    elif com == "scissor" and player == "paper":
        com_score += 1
        messagebox.showinfo(message="Scissors cuts Paper \n Com wins !")
    elif com == "scissor" and player == "lizard":
        com_score += 1
        messagebox.showinfo(message="Scissors decapitates Lizard  \n Com wins ! ")
    elif com == "rock" and player == "lizard":
        com_score += 1
        messagebox.showinfo(message="Rock crushes Lizard  \n Com wins !")
    elif com == "rock" and player == "scissor":
        com_score += 1
        messagebox.showinfo(message="Rock crushes Scissors  \n Com wins !")
    elif com == "paper" and player == "rock":
        com_score += 1
        messagebox.showinfo(message="Paper covers Rock \n Com wins ! ")
    elif com == "paper" and player == "spock":
        com_score += 1
        messagebox.showinfo(message="Paper disproves spock  \n Com wins !")
    elif com == "lizard" and player == "paper":
        com_score += 1
        messagebox.showinfo(message="Lizard eats paper  \n Com wins !")
    elif com == "lizard" and player == "spock":
        com_score += 1
        messagebox.showinfo(message="Lizard poisons Spock  \n Com wins !")
    elif com == "spock" and player == "scissor":
        com_score += 1
        messagebox.showinfo(message="Spock smashes Scissors  \n Com wins !")
    elif com == "spock" and player == "rock":
        com_score += 1
        messagebox.showinfo(message="Spock vaporizes Rock  \n Com wins !")

    elif player == "scissor" and com == "paper":
        player_score += 1
        messagebox.showinfo(message="Scissors cuts Paper \n player wins !")
    elif player == "scissor" and com == "lizard":
        player_score += 1
        messagebox.showinfo(message="Scissors decapitates Lizard  \n player wins ! ")
    elif player == "rock" and com == "lizard":
        player_score += 1
        messagebox.showinfo(message="Rock crushes Lizard  \n player wins !")
    elif player == "rock" and com == "scissor":
        player_score += 1
        messagebox.showinfo(message="Rock crushes Scissors  \n player wins !")
    elif player == "paper" and com == "rock":
        player_score += 1
        messagebox.showinfo(message="Paper covers Rock \n player wins ! ")
    elif player == "paper" and com == "spock":
        player_score += 1
        messagebox.showinfo(message="Paper disproves spock  \n player wins !")
    elif player == "lizard" and com == "paper":
        player_score += 1
        messagebox.showinfo(message="Lizard eats paper  \n player wins !")
    elif player == "lizard" and com == "spock":
        player_score += 1
        messagebox.showinfo(message="Lizard poisons Spock  \n player wins !")
    elif player == "spock" and com == "scissor":
        player_score += 1
        messagebox.showinfo(message="Spock smashes Scissors  \n player wins !")
    elif player == "spock" and com == "rock":
        player_score += 1
        messagebox.showinfo(message="Spock vaporizes Rock  \n player wins !")

    lbl.configure(text="Score : " + str(com_score) + " Score : " + str(player_score))
    pass

a = rock_paper_scissor(root)

def change_game(event=None):
    global a, toggle, com_score, player_score
    a.destroy()
    if toggle:
        toggle = False
        com_score, player_score = 0, 0
        root.title("Rock Paper Scissor Lizard Spock")
        lbl.configure(text="Score : " + str(com_score) + " Score : " + str(player_score))
        a = rock_paper_scissor_lizard_spock(root)
    else:
        toggle = True
        com_score, player_score = 0, 0
        root.title("Rock Paper Scissor ")
        lbl.configure(text="Score : " + str(com_score) + " Score : " + str(player_score))
        a = rock_paper_scissor(root)

root.bind_all("<Home>", func=change_game)

menubar = Menu(root)

game = Menu(menubar, tearoff=0)
game.add_command(label="rock paper scissor", accelerator="Home", command=change_game)
game.add_command(label="rock paper scissor lizard spock", accelerator="Home", command=change_game)

exit_m = Menu(menubar, tearoff=0)
exit_m.add_command(label="exit", command=root.destroy)

menubar.add_cascade(label='Game', menu=game)
menubar.add_cascade(label="Exit", menu=exit_m)

root.config(menu=menubar)

root.mainloop()
