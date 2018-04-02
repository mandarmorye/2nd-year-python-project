from tkinter import *
from PIL import ImageTk, Image
from os import *
import random
import time
import tkinter.messagebox
root=Tk()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def scoreCard(): #display the score page
    global label21 
    label21=Label(root,text="Your SCORE",font="Times 25",width=100,bg="SkyBlue4",padx=10,pady=10)
    label21.pack()

    label22=Label(root,text="CORRECT : "+str(check)+" /5",font="Times 25",width=100,bg="SkyBlue3",padx=10,pady=10) 
    label22.pack()
    labelcheck=Label(root,text="\n".join(checklist),font="Times 13",width=100,bg="SkyBlue3",padx=5,pady=5)
    labelcheck.pack()
    
    label23=Label(root,text="INCORRECT : "+str(uncheck)+" /5",font="Times 25",width=100,bg="SkyBlue2",padx=10,pady=10) 
    label23.pack()
    labeluncheck=Label(root,text="\n".join(unchecklist),font="Times 13",width=100,bg="SkyBlue2",padx=5,pady=5) 
    labeluncheck.pack()

    def scoreErase() : #remove content of score page 
        labelcheck.pack_forget()
        labeluncheck.pack_forget()
        label21.pack_forget()
        label22.pack_forget()
        label23.pack_forget()
        but.pack_forget()
        mainMenu() # return to mainmenu

    but=Button(root,text=" MAIN MENU ",cursor="circle",font="Times 15",fg="white",bg="firebrick1",width=50,padx=30,pady=30,command=scoreErase)
    but.pack()
    mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def game() :
    Newbut.pack_forget()
    Instbut.pack_forget()
    Exitbut.pack_forget()

    global flag
    if flag!=0:
        global labelinst
        labelinst.pack_forget()

    def evalute(event):
        global check
        global uncheck
        global i
        global checklist
        global unchecklist

        data=e.get()
        if str(data.lower()) in ansDict.keys() :
            if ansDict[str(data.lower())] == imageDict[str(list[i])]:
                check+=1
                checklist.append(str(data.lower()))
            else :
                uncheck+=1
                unchecklist.append(str(data.lower()))
        else :
            uncheck+=1
            unchecklist.append(str(data.lower()))

        global label
        label.pack_forget()
        labelnum2.pack_forget()
        label1.pack_forget()
        e.pack_forget()
        labelextra1.pack_forget()

        # image window (even number of image)(i is even)
        i+=1
        if(i>4) :
            scoreCard()
        else :
            global labelnum1
            labelnum1=Label(root,text=str(i+1),font="Times 15",width=5,bg="olive drab",padx=10,pady=10)
            labelnum1.pack(anchor=W)

            global newlabel
            image=Image.open(str(list[i]))
            image=image.resize((250, 250), Image.ANTIALIAS)
            photo=ImageTk.PhotoImage(image)

            newlabel=Label(root,image=photo,width=20,bg="saddle brown",padx=10,pady=10)
            newlabel.pack(fill=BOTH, expand=1)

            global label2
            label2=Label(root,text="ENTER YOUR ANSWER : ",font="Times 13",width=100,bg="olive drab",padx=10,pady=10)
            label2.pack()

            global e1
            e1=Entry(root)
            e1.bind("<Return>",fk)
            e1.pack()

            global labelextra2
            labelextra2=Label(root,width=100,bg="saddle brown")
            labelextra2.pack()
            mainloop()

    def fk(event) :
        global e1
        global label2
        global newlabel
        global labelnum
        global labelextra2
        global check
        global uncheck
        global checklist
        global unchecklist
        global i
        newlabel.pack_forget()
        label2.pack_forget()
        labelnum1.pack_forget()
        e1.pack_forget()
        labelextra2.pack_forget()
        data=e1.get()
        if str(data.lower()) in ansDict.keys() :
            if ansDict[str(data.lower())] == imageDict[str(list[i])] :
                check+=1
                checklist.append(str(data.lower()))
            else :
                uncheck+=1
                unchecklist.append(str(data.lower()))
        else :
            uncheck+=1
            unchecklist.append(str(data.lower()))

        i+=1
        game()
        
    # image window (even number of image)(i is even)
    global i
    global label
    if(i>4) :
        scoreCard()
    else :
        global labelnum2
        labelnum2=Label(root,text=str(i+1),width=5,font="Times 15",bg="thistle4",padx=10,pady=10)
        labelnum2.pack(anchor=W)

        image=Image.open(str(list[i]))
        image=image.resize((250, 250), Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(image)

        label=Label(root,image=photo,width=20,bg="firebrick1",padx=10,pady=10)
        label.pack(fill=BOTH, expand=1)
        
        label1=Label(root,text="ENTER YOUR ANSWER : ",font="Times 13",width=100,bg="thistle4",padx=10,pady=10)
        label1.pack()

        global e
        e=Entry(root)
        e.bind("<Return>",evalute)
        e.pack()

        labelextra1=Label(root,width=100,bg="thistle4")
        labelextra1.pack()
        mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def instruct(): #display instruction page
    Newbut.pack_forget()
    Instbut.pack_forget()
    Exitbut.pack_forget()

    global labelinst
    global flag
    flag+=1

    image=Image.open("instruction.png")
    image=image.resize((400, 400), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)

    labelinst=Label(root,image=photo,bg="black",width=40,padx=10,pady=10)
    labelinst.pack(fill=BOTH, expand=1)

    def backErase() : #remove instruction content
        global labelinst
        labelinst.pack_forget()
        backbut.pack_forget()
        mainMenu() #return to mainmenu

    backbut=Button(root,text=" BACK ",cursor="circle",fg="white",bg="firebrick1",padx=20,command=backErase)
    backbut.pack()
    mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def exitGame(): #popup window
    Newbut.pack_forget()
    Instbut.pack_forget()
    Exitbut.pack_forget()
    
    ans=tkinter.messagebox.askquestion("VERIFICATION","DO you want to EXIT?")
    if ans=="yes" :
        root.destroy()
    else :
        mainMenu()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#mainmenu window
def mainMenu() :
    global list
    list=['bentley.png','bugatti.png','buick.png','cadillac.png','chevrolet.png','chrysler.png','citroen.png','dodge.png','ferrari.png','honda.png','indian motorcycle.png','infiniti.png','jaguar.png','jeep.png','lamborghini.png','mahindra.png','maserati.png','mazda.png','mercury.png','mitsubishi.png','opel.png','peugeot.png','pontiac.png','renault.png','rolls royce.png','royal enfield.png','skoda.png','suzuki.png','tesla.png','toyota.png','volkswagen.png']
    random.shuffle(list)

    global i
    global check
    global uncheck
    global checklist
    global unchecklist
    global flag
    i=0
    check=0
    uncheck=0
    checklist=[]
    unchecklist=[]
    flag=0

    startbut.pack_forget()
    canvas.pack_forget()

    global Newbut
    Newbut=Button(root,text=" NEW GAME ",font="Times 15",cursor="circle",fg="white",bg="purple1",width=50,padx=30,pady=30,command=game)
    Newbut.pack()

    global Instbut
    Instbut=Button(root,text=" INSTRUCTION ",font="Times 15",cursor="circle",fg="white",bg="purple2",width=50,padx=30,pady=30,command=instruct)
    Instbut.pack()

    global Exitbut
    Exitbut=Button(root,text=" EXIT ",font="Times 15",cursor="circle",fg="white",bg="purple3",width=50,padx=30,pady=30,command=exitGame)
    Exitbut.pack()

    mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#initial window
canvas = Canvas(root, width=500, height=200, bg = 'coral')
canvas.create_text(50,100,fill="red4",font="Times 40 italic bold",text="LOGO\n   QUIZ")
canvas.pack()

for i in range(0,40):
    canvas.move(1,5,0)
    root.update()
    time.sleep(0.1)

startbut=Button(root,text=" START ",cursor="circle",font="Times 15",fg="saddle brown",bg="gold",width=50,padx=30,pady=30,command=mainMenu)
startbut.pack()

global ansDict
ansDict={'bentley':1,'bugatti':2,'buick':3,'cadillac':4,'chevrolet':5,'chrysler':6,'citroen':7,'dodge':8,'ferrari':9,'honda':10,'indian motorcycle':11,'infiniti':12,'jaguar':13,'jeep':14,'lamborghini':15,'mahindra':16,'maserati':17,'mazda':18,'mercury':19,'mitsubishi':20,'opel':21,'peugeot':22,'pontiac':23,'renault':24,'rolls royce':25,'royal enfield':26,'skoda':27,'suzuki':28,'tesla':29,'toyota':30,'volkswagen':31}

global imageDict
imageDict={'bentley.png':1,'bugatti.png':2,'buick.png':3,'cadillac.png':4,'chevrolet.png':5,'chrysler.png':6,'citroen.png':7,'dodge.png':8,'ferrari.png':9,'honda.png':10,'indian motorcycle.png':11,'infiniti.png':12,'jaguar.png':13,'jeep.png':14,'lamborghini.png':15,'mahindra.png':16,'maserati.png':17,'mazda.png':18,'mercury.png':19,'mitsubishi.png':20,'opel.png':21,'peugeot.png':22,'pontiac.png':23,'renault.png':24,'rolls royce.png':25,'royal enfield.png':26,'skoda.png':27,'suzuki.png':28,'tesla.png':29,'toyota.png':30,'volkswagen.png':31}

root.configure(background="black")
root.geometry("500x500")
root.mainloop()
