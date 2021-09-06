import tkinter
from PIL import Image, ImageTk
import random


root = tkinter.Tk()
root.geometry('300x410') #creation of the app window
root.title('FramesandPackets Dice Roll')
root.configure(background='ghost white')

#HEADER LABEL
Header_Label = tkinter.Label(root, text="\nFramesandPackets Dice Roll",
                            fg = "black",
                            bg = "ghost white",
                            font = "Helvetica 12 bold")
Header_Label.pack()

#images of Dice
dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png'] #images being pulled from project dir
dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))  #creating 1:6 chance of each side of dice to be chosen

# add image on load of app
ImageLabel = tkinter.Label(root, image=dice_image)
ImageLabel.image = dice_image
ImageLabel.pack( expand=True)   #if image bigger than window expand

#function for every time button is clicked (select random image 1-6)
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage

button = tkinter.Button(root, text='Roll the Dice!', fg='black', command=rolling_dice)   #creating button and calling function(rolling_dice) when clicked

button.pack( expand=True)

root.mainloop()   #main loop the window so always open
