from tkinter import *


def guiB(argument):
    global arg
    arg = argument
    arg = Tk()
    arg.title(argument)

def cmdSet(cmd, moreData):
    global command
    global widget
    if cmd == "widget_text":
        widget.configure(text=moreData)
    command = "widget_text"

def guiC():
    global arg
    arg.mainloop()

def guiWidget(argument, argument2):
    global command
    global arg
    global widget
    widget = argument
    text = argument2
    if argument == "button":
        widget = Button(text=text, command=command)
    if argument == "text":
        widget = Label(text=text)
    if argument == "image":
        widget = Label(image=text)
    if argument == "button_image":
        widget = Button(image=text, command=command)
def guiWidgetPack():
    global widget
    widget.pack()


