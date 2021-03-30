# This is a sample Python script.

from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter.filedialog import *
import os
outputFile = "C:/Users/Stasy/Desktop/output2FLASH.txt"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def selectFullScreens():
    fileNames = askopenfilenames(parent=window)
    fOut = open(outputFile, 'w')
    for fileName in fileNames:
        f = open(fileName)
        lines = f.readlines()
        for line in lines:
            for word in line.split(' '):
                if word.startswith('0x'):
                    line = re.findall(r'[0x]\w+', str(line))
                    line = str(line)
                    line = re.sub(r'\]', '', line)
                    line = re.sub(r'\[', '', line)
                    line = re.sub(r'0x', '', line)
                    line = re.sub(r'\'', '', line)
                    line = re.sub(r'\ ', '', line)
                    fOut.writelines(line+',')
                    fOut.writelines('\n')
                    # print(line)
                    break
        f.close()
        # print(fileName)
        # print(len(filenames))
    adds = 0
    for i in range(1, 256+1-len(fileNames), 1):
        for j in range(1, 128+1, 1):
            adds = ('0xff,'*64)+'\n'
            adds = re.sub(r'\]', '', adds)
            adds = re.sub(r'\[', '', adds)
            adds = re.sub(r'0x', '', adds)
            adds = re.sub(r'\'', '', adds)
            adds = re.sub(r'\ ', '', adds)
            # print(adds)
            fOut.writelines(adds)
            # fOut.writelines('\n')
    print(i)
    print(int(len(adds)/5))
    # print(adds)
        # print(len(fileNames))
    fOut.close()
    text0.insert(INSERT, 'Готово')


def selectSmallImages():
    fileNames = askopenfilenames(parent=window)
    for fileName in fileNames:
        f = open(fileName)
        last_line = f.readlines()[-3]
        f.close()
        last_line = re.split(r',', last_line)
        width = last_line[1]
        height = last_line[2]
        length = int((int(width)+1)*int(height)/2)
#################################################################################
        f = open(fileName)          #   width and height became known
        fOut = open(outputFile, 'a')
        lines = f.readlines()
        for line in lines:
            for word in line.split(' '):
                if word.startswith('0x'):
                    line = re.findall(r'[0x]\w+', str(line))
                    line = str(line)
                    line = re.sub(r'\]', '', line)
                    line = re.sub(r'\[', '', line)
                    line = re.sub(r'0x', '', line)
                    line = re.sub(r'\'', '', line)
                    line = re.sub(r'\ ', '', line)
                    fOut.writelines(line + ',')
                    fOut.writelines('\n')
                    # print(line)
                    break
        f.close()
        complement=0
        if (length < 8192):
            print('small image')
            for i in range(1, int((8192-length)/64)+1, 1):
                adds = ('0xff,' * 64) + '\n'
                adds = re.sub(r'\]', '', adds)
                adds = re.sub(r'\[', '', adds)
                adds = re.sub(r'0x', '', adds)
                adds = re.sub(r'\'', '', adds)
                adds = re.sub(r'\ ', '', adds)
                # print(adds)
                fOut.writelines(adds)
        for i in range(1, 256 + 1 - len(fileNames), 1):
            for j in range(1, 128 + 1, 1):
                adds = ('0xff,' * 64) + '\n'
                adds = re.sub(r'\]', '', adds)
                adds = re.sub(r'\[', '', adds)
                adds = re.sub(r'0x', '', adds)
                adds = re.sub(r'\'', '', adds)
                adds = re.sub(r'\ ', '', adds)
                # print(adds)
                fOut.writelines(adds)
                # fOut.writelines('\n')
        print(i)
        print(int(len(adds) / 5))
    fOut.close()
    text1.insert(INSERT,'Готово')

def selectSounds():
    fileNames = askopenfilenames(parent=window)
    for fileName in fileNames:
        f = open(fileName)
        raw = f.read()
        f.close()
        print(raw)
        print(fileName)
    text2.insert(INSERT, 'Готово')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('320x100')
    window.title("flashFiller")

    lbl0 = Label(window, text="Выбор полноэкранных картинок")
    lbl0.grid(column=0, row=0)
    lbl1 = Label(window, text="Выбор маленьких картинок")
    lbl1.grid(column=0, row=1)
    lbl2 = Label(window, text="Выбор звуков")
    lbl2.grid(column=0, row=2)

    text0 = Text(width=7, height=1)
    text0.grid(column=2, row=0)
    # text0.pack()
    text1 = Text(width=7, height=1)
    text1.grid(column=2, row=1)
    # text1.pack()
    text2 = Text(width=7, height=1)
    text2.grid(column=2, row=2)
    # text2.pack()

    btn0 = Button(window, text="Выбрать", command=selectFullScreens)
    btn0.grid(column=1, row=0)
    btn1 = Button(window, text="Выбрать", command=selectSmallImages)
    btn1.grid(column=1, row=1)
    btn2 = Button(window, text="Выбрать", command=selectSounds)
    btn2.grid(column=1, row=2)

    window.mainloop()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
