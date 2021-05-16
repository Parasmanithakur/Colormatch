import tkinter #library for the gui
from PIL import Image, ImageTk #library for image import
import random

score=0

root =tkinter.Tk() #root is the window name 
root.geometry('400x400')
root.title('Colour Match')
ScoreLine = tkinter.Label(root,text=str(score))
ScoreLine.pack()
def scorechange(score):
  ScoreLine.configure(text=str(score))
color =['black.png','green.png','blue.png',
 'red.png','yellow.png','orange.png']
colorName=['black','green','blue',
 'red','yellow','orange']
Ncolorname=colorName[random.randint(0,5)]

NameLabel=tkinter.Label(root, text=Ncolorname)
NameLabel.pack(expand=True)
Ncolorpic=color[random.randint(0,5)]
ColourImage =ImageTk.PhotoImage(Image.open(Ncolorpic))
ImageLabel =tkinter.Label(root,image=ColourImage)


ImageLabel.pack(expand=True)
i=0
def Image_colour_yes():
    global score
    global Ncolorname
    global Ncolorpic
    if(Ncolorname in str(Ncolorpic)):
      score+=1
    
    scorechange(score)
    Ncolorpic=color[random.randint(0,5)]
    ColourImage = ImageTk.PhotoImage(Image.open(Ncolorpic))
    # update image
    Ncolorname=colorName[random.randint(0,5)]
    ImageLabel.configure(image=ColourImage)
    NameLabel.configure(text=Ncolorname)
    # keep a reference
    ImageLabel.image = ColourImage
    
  
def Image_colour_no():
    global score
    global Ncolorname
    global Ncolorpic
    if(Ncolorname not in str(Ncolorpic)):
      score+=1
    
    scorechange(score)
    Ncolorpic=color[random.randint(0,5)]
    ColourImage = ImageTk.PhotoImage(Image.open(Ncolorpic))
    # update image
    Ncolorname=colorName[random.randint(0,5)]
    ImageLabel.configure(image=ColourImage)
    NameLabel.configure(text=Ncolorname)
    # keep a reference
    ImageLabel.image = ColourImage
    
  

button = tkinter.Button(root, text='Yes', fg='blue', command=Image_colour_yes)
button1 = tkinter.Button(root, text='No', fg='blue', command=Image_colour_no)
# pack a widget in the parent widget
button.pack( expand=True)
button1.pack( expand=True)
root.mainloop()    