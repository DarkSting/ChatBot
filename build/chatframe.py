
import tkinter
from pathlib import Path
from model import ChatBotModel as bot


# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import ttk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Lenovo\PycharmProjects\ChatBot\build\assets\frame0")

#initializing the bot in the chatframe
bot = bot()
bot.loadModel()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#clearing the textbox
def clearTextBox(widget):
    widget.delete(1.0, tk.END)

#reading the user input
def readTextBox(input,widget):
    value = input.get()
    widget.insert(tk.END,"YOU : "+value)
    widget.config(fg="#654E92")
    response = bot.chat(value)
    widget.insert(tk.END,"\n"+response)

    widget.insert(tk.END,"\n")
    widget.insert(tk.END, "\n")

#initiating the frame
def openChat(window):

    #making the canvas
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 800,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1000.0,
        87.0,
        fill="#FCFFE7",
        outline="")

    canvas.create_rectangle(
        0.0,
        676.0,
        1000.0,
        800.0,
        fill="#FAE28B",
        outline="")

    frame = tk.Frame(canvas, bg="#FBF8F8", bd=0, highlightthickness=0)
    frame.place(x=24, y=87, width=1000, height=589)

    # create a scrollable canvas inside the frame widget
    scrollable_canvas = Canvas(frame, bg="#FBF8F8", bd=0, highlightthickness=0,width=1000.0,height=580.0)
    scrollable_canvas.place(x=24,y=87)
    scrollable_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # create a rectangle inside the scrollable canvas
    scrollable_canvas.create_rectangle(
        20.0,
        20.0,
        950.0,
        550.0,
        fill="#FBF8F8",
        outline=""
    )

    # create a Text widget inside the scrollable canvas
    text_widget = Text(scrollable_canvas, bg="#FBF8F8", wrap=tk.WORD,font=("RobotoRoman CondensedBold", 30 * -1))
    text_widget.insert(tk.END,"clear the text when you reach the bound")
    # add the Text widget to the scrollable canvas
    scrollable_canvas.create_window(60, 60, anchor=tk.NW, window=text_widget, width=880)

    # add the frame widget containing the scrollable canvas to the main canvas
    canvas.create_window(0, 87, anchor=tk.NW, window=frame)

    #images
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        943.0,
        43.0,
        image=image_image_1
    )

    canvas.create_text(
        721.0,
        19.0,
        anchor="nw",
        text="U-CHAT",
        fill="#2B3467",
        font=("RobotoRoman CondensedBold", 48 * -1)
    )

    #textbox
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        431.0,
        736.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font=("RobotoRoman CondensedBold", 25 * -1)
    )
    entry_1.place(
        x=44.0,
        y=700.0,
        width=774.0,
        height=70.0
    )

    #send button
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: readTextBox(entry_1,text_widget),
        relief="flat"
    )
    button_1.place(
        x=872.0,
        y=700.0,
        width=80.0,
        height=71.66668701171875
    )

    #delete button
    button_image_2 = PhotoImage(
        file=relative_to_assets("remove.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: clearTextBox(text_widget),
        relief="flat"
    )
    button_2.place(
        x=15.0,
        y=12,
        width=70.0,
        height=70.0
    )
    window.resizable(False, False)
    window.mainloop() #infinte loop to track events
