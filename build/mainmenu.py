
from pathlib import Path

from build import chatframe
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Lenovo\PycharmProjects\ChatBot\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x800")
window.configure(bg = "#FFFFFF")

def setNextFrame(canvas,window):
    chatframe.openChat(window)
    canvas = chatframe.canvas



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
    496.10894775390625,
    800.0,
    fill="#13005A",
    outline="")

canvas.create_text(
    64.0,
    372.111083984375,
    anchor="nw",
    text="Ask any question related to \nYour UNI we wil help you",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 30 * -1)
)

canvas.create_text(
    157.50582885742188,
    238.0,
    anchor="nw",
    text="U-CHAT",
    fill="#FFFFFF",
    font=("RobotoRoman CondensedBold", 48 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: setNextFrame(canvas=canvas,window=window),
    relief="flat"
)
button_1.place(
    x=559.0,
    y=503.0,
    width=394.0,
    height=120.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    779.0,
    298.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
