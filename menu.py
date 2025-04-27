import os 
import subprocess 
from tkinter import * 
from tkinter import messagebox 
import time 
 
w=Tk() 
canvas=Canvas(w,width=500,height=300) 
w.title("Welcome message") 
w.resizable(0,0) 
canvas.create_text(250,100,fill='orange',text="Welcome to Ball-Paddle game", 
                   font=('Bernard MT',20)) 
canvas.pack() 
 
ob=Tk() 
ob.title("Team-Project") 
lbl=Label(ob,text="Choose mode of play:",font=('Arial',20)).grid() 
 
def play1(): 
   messagebox.showinfo(title="Rules",message='''Move the paddle bar using left 
and right arrow keys. 
Prevent the ball from hitting bottom of the screen. 
Click on the gamescreen to get started''') 
    
   subprocess.call('paddle1.py',shell=True) 
    
def play2(): 
   messagebox.showinfo(title="Rules",message='''Keys to press 
Player1:E and X 
Player2: Up and Down arrow keys 
Prevent the ball from getting past your paddle.Click on gamescreen to get 
started''') 
   subprocess.call('pvp.py',shell=True) 
 
bt1=Button(ob,text="Player 1",command=play1,font=('Arial',16)).grid() 
 
bt2=Button(ob,text="Player 2",command=play2,font=('Arial',16)).grid() 
 
ob.mainloop()