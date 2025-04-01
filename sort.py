from tkinter import *
import turtle
from time import perf_counter as clock
import time




arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

posarr = [100,150,-150,25,-25,75,-100,-50,50,0,-75,125,-125,175,-175,-200]
screen = turtle.Screen()
screen.bgcolor("#222")

turtle.penup()
turtle.setpos(-200,200)
turtle.pencolor("green")
turtle.write("Bubble sorting ", True, align="center", font=("Courier",18,"bold"))
turtle.ht()


bar1 = turtle.Turtle()
bar1.shape('square')
bar1.shapesize(arr[0],1)
bar1.penup()
bar1.setpos(posarr[0],-150)
bar1.color("green")

bar2 = turtle.Turtle()
bar2.shape('square')
bar2.shapesize(arr[1],1)
bar2.penup()
bar2.setpos(posarr[1],-140)
bar2.color("green")


bar3 = turtle.Turtle()
bar3.shape('square')
bar3.shapesize(arr[2],1)
bar3.penup()
bar3.setpos(posarr[2],-130)
bar3.color("green")

bar4 = turtle.Turtle()
bar4.shape('square')
bar4.shapesize(arr[3],1)
bar4.penup()
bar4.setpos(posarr[3],-120)
bar4.color("green")

bar5 = turtle.Turtle()
bar5.shape('square')
bar5.shapesize(arr[4],1)
bar5.penup()
bar5.setpos(posarr[4],-110)
bar5.color("green")

bar6 = turtle.Turtle() 
bar6.shape('square')
bar6.shapesize(arr[5],1)
bar6.penup()
bar6.setpos(posarr[5],-100)
bar6.color("green")

bar7 = turtle.Turtle() 
bar7.shape('square')
bar7.shapesize(arr[6],1)
bar7.penup()
bar7.setpos(posarr[6],-90)
bar7.color("green")

bar8 = turtle.Turtle() 
bar8.shape('square')
bar8.shapesize(arr[7],1)
bar8.penup()
bar8.setpos(posarr[7],-80)
bar8.color("green")

bar9 = turtle.Turtle() 
bar9.shape('square')
bar9.shapesize(arr[8],1)
bar9.penup()
bar9.setpos(posarr[8],-70)
bar9.color("green")


bar10 = turtle.Turtle() 
bar10.shape('square')
bar10.shapesize(arr[9],1)
bar10.penup()
bar10.setpos(posarr[9],-60)
bar10.color("green")

bar11 = turtle.Turtle()
bar11.shape('square')
bar11.shapesize(arr[10],1)
bar11.penup()
bar11.setpos(posarr[10],-50)
bar11.color("green")

bar12 = turtle.Turtle() 
bar12.shape('square')
bar12.shapesize(arr[11],1)
bar12.penup()
bar12.setpos(posarr[11],-40)
bar12.color("green")

bar13 = turtle.Turtle() 
bar13.shape('square')
bar13.shapesize(arr[12],1)
bar13.penup()
bar13.setpos(posarr[12],-30)
bar13.color("green")

bar14 = turtle.Turtle() 
bar14.shape('square')
bar14.shapesize(arr[13],1)
bar14.penup()
bar14.setpos(posarr[13],-20)
bar14.color("green")

bar15 = turtle.Turtle() 
bar15.shape('square')
bar15.shapesize(arr[14],1)
bar15.penup()
bar15.setpos(posarr[14],-10)
bar15.color("green")


bar16 = turtle.Turtle() 
bar16.shape('square')
bar16.shapesize(arr[15],1)
bar16.penup()
bar16.setpos(posarr[15],0)
bar16.color("green")
msg1 = "Hello"


# turtle.write((300,300), True)

a = clock()
for o in range(len(posarr)):
    for a in range(len(posarr)-1):
        temp = posarr[a]+ posarr[a+1]
        if posarr[a] > posarr[a+1]:
            posarr[a] = temp - posarr[a]
            posarr[a+1] = temp - posarr[a+1]
        bar1.setpos(posarr[0],-150)
        bar2.setpos(posarr[1],-140)
        bar3.setpos(posarr[2],-130)
        bar4.setpos(posarr[3],-120)
        bar5.setpos(posarr[4],-110)
        bar6.setpos(posarr[5],-100)
        bar7.setpos(posarr[6],-90)
        bar8.setpos(posarr[7],-80)
        bar9.setpos(posarr[8],-70)
        bar10.setpos(posarr[9], -60)
        bar11.setpos(posarr[10], -50)
        bar12.setpos(posarr[11], -40)
        bar13.setpos(posarr[12], -30)
        bar14.setpos(posarr[13], -20)
        bar15.setpos(posarr[14], -10)
        bar16.setpos(posarr[15], 0)
b = clock()

bar1.color("white")
bar2.color("white")
bar3.color("white")
bar4.color("white")
bar5.color("white")
bar6.color("white")
bar7.color("white")
bar8.color("white")
bar9.color("white")
bar10.color("white")
bar11.color("white")
bar12.color("white")
bar13.color("white")
bar14.color("white")
bar15.color("white")
bar16.color("white")

print("done: %.2f sec." % (b-a))
screen.mainloop()