from tkinter import * 
from tkinter import messagebox 
import random 
import time 
import os 
import sys 
import subprocess 
 
 
a=Tk() 
canvas=Canvas(a,width=500,height=500) 
a.title("Ball-Paddle") 
a.resizable(0,0) 
canvas.pack() 
a.update() 
 
count=0 
 
def score(): 
    canvas.itemconfig(cscore,text='Score:'+str(count)) 
 
 
 
class Ball: 
    def __init__(self,canvas,paddle,color): 
 
        self.canvas=canvas 
        self.paddle=paddle 
        self.circ=canvas.create_oval(10,10,27,27,fill=color) 
        self.canvas.move(self.circ,220,220) 
 
        startx=[-5,-4,-3,-2,-1,1,2,3,4,5] 
        self.x=random.choice(startx) 
        self.y=-3 
 self.cht=self.canvas.winfo_height() 
        self.cwd=self.canvas.winfo_width() 
        self.hitbottom=False 
 
    def hit_paddle(self,pos): 
        paddle_pos=self.canvas.coords(self.paddle.pad) 
 
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]: 
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]: 
 
                self.x+=self.paddle.x 
 
                return True 
        return False 
 
    def draw(self,v): 
        self.canvas.move(self.circ,self.x,self.y) 
        pos=self.canvas.coords(self.circ) 
 
        if pos[0]<=0: 
            canvas.itemconfig(self.circ,fill='blue') 
            self.x=3 
        if pos[2]>=self.cwd: 
            self.x=-3 
            canvas.itemconfig(self.circ,fill='yellow') 
        if pos[1]<=0: 
            self.y=v 
            canvas.itemconfig(self.circ,fill='orange') 
        if pos[3]>=self.cht: 
            self.hitbottom=True 
        if self.hit_paddle(pos)==True: 
            self.y=-v 
            canvas.itemconfig(self.circ,fill='red') 
            global count 
            count+=1 
            score() 
 
 
class Paddle: 
    def __init__(self,canvas,color): 
        self.canvas=canvas 
        self.pad=canvas.create_rectangle(100,100,180,110,fill=color) 
        self.canvas.move(self.pad,200,300) 
        self.x=0 
        self.cwd=self.canvas.winfo_width() 
        self.start=False 
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left) 
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right) 
        self.canvas.bind_all('<KeyRelease>',self.stop) 
        self.canvas.bind_all('<Button-1>',self.st) 
 
    def draw(self): 
        self.canvas.move(self.pad,self.x,0) 
        self.pos=self.canvas.coords(self.pad) 
        if self.pos[0]<=0: 
            self.x=0 
        if self.pos[2]>=self.cwd: 
            self.x=0 
 
    def turn_left(self,event): 
        if self.pos[0]>=0: 
            self.x=-5 
 
    def turn_right(self,event): 
        if self.pos[2]<=self.cwd: 
            self.x=5 
 
    def st(self,event): 
        self.start=True 
 
     
    def stop(self,event): 
        self.x=0 
 
def msgprompt(): 
    r=messagebox.askyesno('Replay','Do you want a replay?') 
    if r: 
        a.destroy() 
        subprocess.call(sys.executable + ' "' + 
                        os.path.realpath(__file__) + '"') 
    else: 
         a.destroy() 
 
 
 
 
paddle=Paddle(canvas,'blue') 
ball=Ball(canvas,paddle,'green') 
gmover=canvas.create_text(250,270,state='hidden', 
                          fill='purple',font=('Algerian',20)) 
cscore=canvas.create_text(250,20,font=('Footlight MT',16)) 
 
score() 
i=3 
 
while 1: 
    if ball.hitbottom==False and paddle.start==True: 
        ball.draw(i) 
        paddle.draw() 
    if ball.hitbottom==True: 
        time.sleep(1) 
        myimage=PhotoImage(file='D:\\download.gif') 
        canvas.create_image(120,0,anchor=NW,image=myimage) 
         
        canvas.itemconfig(gmover,state='normal',text='Game over\n' 
                          +'Score:'+str(count)) 
         
        break 
 
     
    i+=0.008 
    a.update_idletasks() 
    a.update() 
    time.sleep(0.01)
    
msgprompt()
a.mainloop()