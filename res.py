from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.state("zoomed")

root.title(".")
root.resizable(width=0, height=0)
frame1 = LabelFrame(root, padx=20, pady=20)
frame1.grid(row=0, column=0, sticky="nw")
frame1.propagate(0)
frame2 = LabelFrame(root, text="Your Order:", padx=20, pady=20, width=20,font=("Arial", 12, "bold"),bg="white")
frame2.grid(row=0, column=2,sticky="nw",)
frame2.propagate(0)
frame3 = LabelFrame(root, padx=20, pady=20, width=20)
frame3.grid(row=0, column=1,sticky="nw",)
frame3.propagate(0)
frame4 = LabelFrame(root, padx=20, pady=20, width=20)
frame4.grid(row=1, column=0,sticky="nw",)
frame4.propagate(0)
li={}
main={"Chicken Burger":10,"Beef Burger":21,"Cheese Pizza":7,
      "Veggie Pizza":1,"Meat Pizza":16,"Cappuccino":9,"Hot Coffee":17,"Cold coffee":10,
      "BBQ Pasta":13,"Chicken Cheese Pasta":7,"Beef Pasta":3,"Chicken Sandwich":20,
     "Grilled Sandwich":23,"Sprite":31,"Pepsi":25}
global main
total=0
global li
def can(e):
    for widgets in frame2.winfo_children():
        widgets.destroy()

    
        
def click(event):
    teext = event.widget.cget("text")
    label = Label(frame2, text=teext,bg="white",font=("Arial", 9, "bold")).grid(column=2)
    a=teext.split("-")
    temp=int(a[-1])
    if(a[0] not in li):
        li[a[0]]=[1]
        li[a[0]].append(temp)
    else:
        for key,value in li.items():
            if(a[0]==key):
                li[key][0]+=1
                li[key][-1]+=temp

def popup(e):
    top= Toplevel(root)
    top.geometry("1000x700")
    top.title("Child Window")
    def click2(event):
        teext = event.widget.cget("text")        
        temp=teext.split("-")
        string= E1.get()
        for key,value in main.items():
                 if(temp[-1]==key):
                    main[key]+=int(string)
        E1.delete(0, END)
    E1 = Entry(top, bd =5)
    E1.grid(row=1,column=2)
    s = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Chicken Burger"), font="lucida 12 bold")
    s.bind("<Button-1>", click2)
    s.grid(row=2, column=1)
    

    s1 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Beef Burger"), font="lucida 12 bold")
    s1.bind("<Button-1>", click2)
    s1.grid(row=3, column=1)
    

    s2 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Cheese Pizza"), font="lucida 12 bold")
    s2.bind("<Button-1>", click2)
    s2.grid(row=4, column=1)
    

    s3 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Meat Pizza"), font="lucida 12 bold")
    s3.bind("<Button-1>", click2)
    s3.grid(row=5, column=1)
    

    s4 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Cappuccino"), font="lucida 12 bold")
    s4.bind("<Button-1>", click2)
    s4.grid(row=6, column=1)
    

    s5 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Hot Coffee"), font="lucida 12 bold")
    s5.bind("<Button-1>", click2)
    s5.grid(row=2, column=2)

    s6 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Cold coffee"), font="lucida 12 bold")
    s6.bind("<Button-1>", click2)
    s6.grid(row=3, column=2)
    

    s7 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("BBQ Pasta"), font="lucida 12 bold")
    s7.bind("<Button-1>", click2)
    s7.grid(row=4, column=2)
    
    
    s8 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Chicken Cheese Pasta"), font="lucida 12 bold")
    s8.bind("<Button-1>", click2)
    s8.grid(row=5, column=2)


    s9 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Beef Pasta"), font="lucida 12 bold")
    s9.bind("<Button-1>", click2)
    s9.grid(row=2, column=3)


    s10 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Chicken Sandwich"), font="lucida 12 bold")
    s10.bind("<Button-1>", click2)
    s10.grid(row=3, column=3)


    s11 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Grilled Sandwich"), font="lucida 12 bold")
    s11.bind("<Button-1>", click2)
    s11.grid(row=4, column=3)

    

    s12 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Sprite"), font="lucida 12 bold")
    s12.bind("<Button-1>", click2)
    s12.grid(row=4, column=3)


    
    s13 = Button(top, bg="gray", height=1, width=20, text="ADD-"+str("Pepsi"), font="lucida 12 bold")
    s13.bind("<Button-1>", click2)
    s13.grid(row=5, column=3)

    
def con(e):
    total=0
    for widgets in frame2.winfo_children():
         widgets.destroy()
    for key,value in li.items():
        label = Label(frame2, text=str(value[0])+" X "+str(key)+"-"+str(value[-1]),font=("Arial", 9, "bold"),bg="white").grid(column=2)
        total+=value[-1]
        for key2,value2 in main.items():
            if(key==key2):
                main[key2]-=value[0]
    label = Label(frame2, text=".............",bg="white").grid(column=2)
    label = Label(frame2, text="Total: "+str(total),font=("Arial", 9, "bold"),bg="gray").grid(column=2)
    li.clear()

def printt(e):
    pass

for key,value in main.items():
    label = Label(frame3, text=str(key)+" Left: "+str(value),font=("Arial", 12, "bold")).grid(column=3)


x = Label(frame1, text="\nPlace your orders Here\n", font=("Arial", 20, "bold")).grid(row=0, column=5)
b = Label(frame1, text="Burger", bg="black", fg="white", font=("Arial", 17, "bold"))
b.grid(row=1, column=0)
b1 = Button(frame1, text="Chicken Burger-250", height=1, width=20, font="lucida 12 bold")
b1.bind("<Button-1>", click)
b1.grid(row=2, column=0)

b2 = Button(frame1, text="Beef Burger-290", height=1, width=20, font="lucida 12 bold")
b2.bind("<Button-1>", click)
b2.grid(row=3, column=0)

pizza0 = Label(frame1, text="Pizza", bg="black", fg="white", font=("Arial", 17, "bold")).grid(row=1, column=5)
b3 = Button(frame1, height=1, width=20, text="Cheese Pizza-300", font="lucida 12 bold")
b3.bind("<Button-1>", click)
b3.grid(row=2, column=5)
b4 = Button(frame1, height=1, width=20, text="Veggie Pizza-270", font="lucida 12 bold")
b4.bind("<Button-1>", click)
b4.grid(row=3, column=5)
b5 = Button(frame1, height=1, width=20, text="Meat Pizza-340", font="lucida 12 bold")
b5.bind("<Button-1>", click)
b5.grid(row=4, column=5)
pizza = Label(frame1, text="Coffee", bg="black", fg="white", font=("Arial", 17, "bold")).grid(row=1, column=6)

b7 = Button(frame1, height=1, width=20, text="Cappuccino-100", font="lucida 12 bold")
b7.bind("<Button-1>", click)
b7.grid(row=2, column=6)
b8 = Button(frame1, height=1, width=20, text="Hot Coffee-60", font="lucida 12 bold")
b8.bind("<Button-1>", click)
b8.grid(row=3, column=6)
b9 = Button(frame1, height=1, width=20, text="Cold coffee-75", font="lucida 12 bold")
b9.bind("<Button-1>", click)
b9.grid(row=4, column=6)
x = Label(frame1, text="\n", font=("Arial", 20, "bold")).grid(row=5, column=5)
pizza1 = Label(frame1, text="Pasta", bg="black", fg="white", font=("Arial", 17, "bold")).grid(row=6, column=0)

b10 = Button(frame1, height=1, width=20, text="BBQ Pasta-280", font="lucida 12 bold")
b10.bind("<Button-1>", click)
b10.grid(row=7, column=0)
b11 = Button(frame1, height=1, width=20, text="Chicken Cheese Pasta-320", font="lucida 12 bold")
b11.bind("<Button-1>", click)
b11.grid(row=8, column=0)
ba = Button(frame1, height=1, width=20, text="Beef Pasta-340", font="lucida 12 bold")
ba.bind("<Button-1>", click)
ba.grid(row=9, column=0)
pizza2 = Label(frame1, text="Sandwich", bg="black", fg="white", font=("Arial", 17, "bold")).grid(row=6, column=5)

bb = Button(frame1, height=1, width=20, text="Chicken Sandwich-150", font="lucida 12 bold")
bb.bind("<Button-1>", click)
bb.grid(row=7, column=5)
bc = Button(frame1, height=1, width=20, text="Grilled Sandwich-180", font="lucida 12 bold")
bc.bind("<Button-1>", click)
bc.grid(row=8, column=5)
pizza3 = Label(frame1, text="Cold Drinks", bg="black", fg="white", font=("Arial", 17, "bold")).grid(row=6, column=6)
bd = Button(frame1, height=1, width=20, text="Sprite-40", font="lucida 12 bold")
bd.bind("<Button-1>", click)
bd.grid(row=7, column=6)
be = Button(frame1, height=1, width=20, text="Pepsi-40", font="lucida 12 bold")
be.bind("<Button-1>", click)
be.grid(row=8, column=6)
x = Label(frame1, text="\n", font=("Arial", 20, "bold")).grid(row=11, column=5)
bes = Button(frame1, bg="gray", height=1, width=20, text="Confirm Order", font="lucida 12 bold")
bes.bind("<Button-1>", con)
bes.grid(row=12, column=6)
bee = Button(frame1, bg="gray", height=1, width=20, text="Cancel Order", font="lucida 12 bold")
bee.bind("<Button-1>", can)
bee.grid(row=13, column=6)
pizza = Label(frame1, text="-------").grid(row=14, column=6)
prin = Button(frame1, bg="gray", height=1, width=16, text="Print Bill", font="lucida 12 bold")
prin.bind("<Button-1>", printt)
prin.grid(row=15, column=6)

update = Button(frame4, bg="gray", height=1, width=20, text="UPDATE INFO", font="lucida 15 bold")
update.bind("<Button-1>", popup)
update.grid(row=1,column=1)
root.mainloop()
