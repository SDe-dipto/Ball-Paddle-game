from tkinter import *
import time as t
import random

count1 = 0
count2 = 0

def score1():
    canvas.itemconfig(cscore1, text='Player1 Score: ' + str(count1))

def score2():
    canvas.itemconfig(cscore2, text='Player2 Score: ' + str(count2))

class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.circle = canvas.create_oval(10, 10, 30, 30, fill=color)

        self.canvas.move(self.circle, 220, 210)
        self.x = 3
        self.y = 3
        self.height = self.canvas.winfo_height()
        self.width = self.canvas.winfo_width()
        self.hitside = False

    def reset(self):
        self.canvas.delete(self.circle)
        self.__init__(canvas, paddle1, paddle2, 'green')

    def hitpaddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.p)
        if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                self.y += self.paddle1.y
                return True
        return False

    def hitpaddle2(self, pos):
        paddle_pos = self.canvas.coords(self.paddle2.p)
        if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                self.y += self.paddle2.y
                return True
        return False

    def draw(self, v):
        self.canvas.move(self.circle, self.x, self.y)
        pos = self.canvas.coords(self.circle)

        if pos[0] <= 0:
            self.x = v
            self.hitside = True
            global count2
            count2 += 1
            score2()

        if pos[1] <= 0:
            self.y = v
            canvas.itemconfig(self.circle, fill="green")

        if pos[2] >= self.width:
            self.x = -v
            self.hitside = True
            global count1
            count1 += 1
            score1()

        if pos[3] >= self.height:
            self.y = -v
            canvas.itemconfig(self.circle, fill="yellow")

        if self.hitpaddle1(pos) == True:
            self.x = 3
            canvas.itemconfig(self.circle, fill="brown")

        if self.hitpaddle2(pos) == True:
            self.x = -3
            canvas.itemconfig(self.circle, fill="pink")

class Paddle:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.p = canvas.create_rectangle(10, 10, 20, 110, fill=color)
        self.y = 0
        self.cht = self.canvas.winfo_height()

        if self.paddle == 'paddle1':
            self.canvas.bind_all('<KeyPress-e>', self.up)
            self.canvas.bind_all('<KeyPress-x>', self.down)

        if self.paddle == 'paddle2':
            self.canvas.bind_all('<KeyPress-Up>', self.up)
            self.canvas.bind_all('<KeyPress-Down>', self.down)

    def move(self, x, y):
        self.canvas.move(self.p, x, y)

    def draw(self):
        self.canvas.move(self.p, 0, self.y)
        self.pospad = self.canvas.coords(self.p)

        if self.pospad[1] <= 0:
            self.y = 0
        if self.pospad[3] >= self.cht:
            self.y = 0

    def up(self, event):
        if self.pospad[1] >= 0:
            self.y = -6

    def down(self, event):
        if self.pospad[3] <= self.cht:
            self.y = 6

tk = Tk()
canvas = Canvas(tk, width=600, height=600)
tk.title("Air Hockey")
tk.resizable(0, 0)
canvas.pack()
tk.update()

paddle1 = Paddle(canvas, 'paddle1', "red")
paddle1.move(60, 220)

paddle2 = Paddle(canvas, 'paddle2', "blue")
paddle2.move(520, 220)

ball = Ball(canvas, paddle1, paddle2, "green")

cscore1 = canvas.create_text(100, 20, font=('Footlight MT', 10))
cscore2 = canvas.create_text(400, 20, font=('Footlight MT', 10))

score1()
score2()

def startgame(event):
    i = 3
    while True:
        i += 0.005
        if ball.hitside == True:
            t.sleep(1)
            ball.reset()
            break  # Exit the loop after reset

        if ball.hitside == False:
            ball.draw(i)
            paddle1.draw()
            paddle2.draw()
            tk.update_idletasks()
            tk.update()
            t.sleep(0.01)

canvas.bind_all('<Button-1>', startgame)

tk.mainloop()
