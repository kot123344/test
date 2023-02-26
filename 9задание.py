from tkinter import *
import random
def test():
    x=random.randint(1,3)
    can.delete("all")
    if x==1:
        x1 = random.randint(0,300)
        y1 = random.randint(0, 300)
        x2 = random.randint(0, 300)
        y2 = random.randint(0, 300)
        x3 = random.randint(0, 300)
        y3 = random.randint(0, 300)
        can.create_polygon(x1,y1,x2,y2,x3,y3)
    elif x==2 or x==3:
        y4=x4= 10000
        while x4>300 or y4>300:
           x1 = random.randint(0, 300)
           y1 = random.randint(0, 300)
           l4 = random.randint(0, 300)
           x4 = x1 + l4
           y4 = y1 + l4
        if x == 2:
            can.create_rectangle(x1,y1,x4,y4 ,fill='black')
        else:
            can.create_oval(x1,y1,x4,y4 ,fill='black')
root = Tk()
root.title("123")
root.geometry("300x500")
button = Button(root , text="generate" , font=5,command=test)
button.pack( side=BOTTOM,pady=70)
can=Canvas(root, width=300, height=300, bg='white')
can.pack()
root.mainloop()