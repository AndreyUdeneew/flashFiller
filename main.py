# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter.filedialog import *
from tkinter import *
import fileinput

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def selectFullScreens():
    filenames = askopenfilenames(parent=window)
    for fileName in filenames:
        f = open(fileName)
        raw = f.read()
        print(raw)
        f.close()
        print(fileName)
    text0.insert(INSERT, 'Готово')


def selectSmallImages():
    filenames = askopenfilenames(parent=window)
    for fileName in filenames:
        f = open(fileName)
        raw = f.read()
        print(raw)
        f.close()
        print(fileName)
    text1.insert(INSERT,'Готово')

def selectSounds():
    filenames = askopenfilenames(parent=window)
    for fileName in filenames:
        f = open(fileName)
        raw = f.read()
        print(raw)
        f.close()
        print(fileName)
    text2.insert(INSERT, 'Готово')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('350x100')
    window.title("flashFiller")

    lbl0 = Label(window, text="Выбор полноэкранных картинок")
    lbl0.grid(column=0, row=0)
    lbl1 = Label(window, text="Выбор маленьких картинок")
    lbl1.grid(column=0, row=1)
    lbl2 = Label(window, text="Выбор звуков")
    lbl2.grid(column=0, row=2)

    text0 = Text(width=7, height=1)
    text0.grid(column=1, row=0)
    # text0.pack()
    text1 = Text(width=7, height=1)
    text1.grid(column=1, row=1)
    # text1.pack()
    text2 = Text(width=7, height=1)
    text2.grid(column=1, row=2)
    # text2.pack()

    btn0 = Button(window, text="Выбрать", command=selectFullScreens)
    btn0.grid(column=2, row=0)
    btn1 = Button(window, text="Выбрать", command=selectSmallImages)
    btn1.grid(column=2, row=1)
    btn2 = Button(window, text="Выбрать", command=selectSounds)
    btn2.grid(column=2, row=2)

    window.mainloop()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
