import turtle 
import tkinter
import random

x = 0
y = 0

def menuScreen():
    window = tkinter.Tk()
    window.title("Aim Game")
    window.geometry ("800x800")
    window.configure(bg="teal")
    
    title = tkinter.Label(window, 
    text="AIM GAME", 
    font="Impact 60", 
    bg="Teal", 
    fg="brown")
    title.pack()

    playButton = tkinter.Button(window, 
    text="PLAY!", 
    width="100", 
    font="20", 
    bg="teal", 
    fg="white", 
    command=mainGame)
    playButton.pack()

    settingsButton = tkinter.Button(window, 
    text="Settings", 
    width="100", 
    font="20", 
    bg="teal", 
    fg="white")
    settingsButton.pack()

    exitButton = tkinter.Button(window, 
    text="Exit Game", 
    width="100", 
    font="20", 
    bg="teal", 
    fg="white", 
    command=window.destroy)
    exitButton.pack()


    window.mainloop()

def mainGame() :

    wn = turtle.Screen()
    wn.title ("Aim Game")
    wn.bgcolor ("grey")
    wn.setup (width=800, height= 800)

    loop = 0
     
    def move(x,y):
        x = random.randint (-500, 500)
        y = random.randint (-500, 500)
        dot.sety(y)
        dot.setx(x)

    dot = turtle.Turtle()
    dot.speed(0)
    dot.shape("circle")
    dot.color("black")
    dot.penup()
    while loop == 0:
        dot.onclick(move)

    wn.mainloop()


menuScreen()