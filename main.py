# This is a sample Python script.

from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
from tkinter.filedialog import *
import os
import scipy
import wave
from scipy.io import wavfile
import numpy as np
import soundfile as sf
from scipy.io.wavfile import read

# outputFile = "C:/Users/Stasy/Desktop/output2FLASH.txt"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def selectOutputDir():
    OutputDir = filedialog.askdirectory(parent=window)
    outputFile = OutputDir+'/output2FLASH.txt'
    text3.insert(INSERT, outputFile)
    # return outputFile
    # outputFile = 'C:/Users/Stasy/Desktop/output2FLASH.txt'

def selectFullScreens():
    outputFile = format(text3.get("1.0", 'end-1c'))
    fileNames = askopenfilenames(parent=window)
    fileNames = sorted(fileNames)
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
        print(fileName)
        # print(len(filenames))
    adds = 0
    for i in range(1, 256+1-len(fileNames), 1):
        for j in range(1, 128+1, 1):
            adds = ('ff,'*64)+'\n'
            adds = re.sub(r'\]', '', adds)
            adds = re.sub(r'\[', '', adds)
            # adds = re.sub(r'0x', '', adds)
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
    outputFile = format(text3.get("1.0", 'end-1c'))
    fileNames = askopenfilenames(parent=window)
    fileNames = sorted(fileNames)
    for fileName in fileNames:
        f = open(fileName)
        last_line = f.readlines()[-3]
        f.close()
        last_line = re.split(r',', last_line)
        height = last_line[1]
        width = last_line[2]
        height = int(height)
        width = int(width)
        if (height % 2) != 0:
            height += 1
        length = int(int(height) * int(width) / 2)
        length += 2
        height = format(height, "x")
        width = format(width, "x")
#################################################################################
        f = open(fileName)          #   width and height became known
        fOut = open(outputFile, 'a')
        lines = f.readlines()
        imDimensions = str(width) + ',' + str(height) + ',\n'
        fOut.writelines(imDimensions)
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
            print(fileName)
            for i in range(1, int((8192 - length)/64)+1, 1):
                complement = ('ff,' * 64) + '\n'
                complement = re.sub(r'\]', '', complement)
                complement = re.sub(r'\[', '', complement)
                # complement = re.sub(r'0x', '', complement)
                complement = re.sub(r'\'', '', complement)
                complement = re.sub(r'\ ', '', complement)
                # print(adds)
                fOut.writelines(complement)
            nComplements = 64*i
            nAddComplements = 8192 - length - nComplements
            print(nComplements + int(length)+nAddComplements)
            if (nComplements+length)<8192:
                complement = ('ff,'*nAddComplements)+'\n'
                complement = re.sub(r'\]', '', complement)
                complement = re.sub(r'\[', '', complement)
                complement = re.sub(r'\'', '', complement)
                complement = re.sub(r'\ ', '', complement)
                fOut.writelines(complement)
            # print(i)
    for m in range(1, 256 + 1 - len(fileNames), 1):
        for n in range(1, 128 + 1, 1):
            adds = ('ff,' * 64) + '\n'
            adds = re.sub(r'\]', '', adds)
            adds = re.sub(r'\[', '', adds)
            # adds = re.sub(r'0x', '', adds)
            adds = re.sub(r'\'', '', adds)
            adds = re.sub(r'\ ', '', adds)
            # print(adds)
            fOut.writelines(adds)
            # fOut.writelines('\n')
    # print(n)
    fOut.close()
    text1.insert(INSERT,'Готово')

def selectSounds():
    outputFile = format(text3.get("1.0", 'end-1c'))
    types = {
        1: np.int8,
        2: np.int16,
        4: np.int32
    }
    fileNames = askopenfilenames(parent=window)
    fileNames = sorted(fileNames)
    fOut = open(outputFile, 'a')

    # for n in range(1, 262144 + 1, 1):
    #     adds = ('ff,' * 64) + '\n'
    #     adds = re.sub(r'\]', '', adds)
    #     adds = re.sub(r'\[', '', adds)
    #     # adds = re.sub(r'0x', '', adds)
    #     adds = re.sub(r'\'', '', adds)
    #     adds = re.sub(r'\ ', '', adds)
    #     # print(adds)
    #     fOut.writelines(adds)

    soundNum = -1
    
    prevAddr = 0x01400900
    
    for fileName in fileNames:
        frames=''
        wav = wave.open(fileName, mode="r")
        (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()

        content = wav.readframes(nframes)
        content = str(content)
        content = re.findall(r'[x]\w+', str(content))
        content = str(content)
        content = re.sub(r'\]', '', content)
        content = re.sub(r'\[', '', content)
        content = re.sub(r'x', '', content)
        content = re.sub(r'\'', '', content)
        content = re.sub(r'\ ', '', content)
        print(content)
        print(fileName)

        soundNum = soundNum + 1
        soundNumHex = hex(soundNum)
        print(soundNumHex)
        soundNumHex = int(soundNumHex, base=16)
        soundNumHex = format(int(soundNumHex), 'x')
        print(soundNumHex)

        nframes_3 = hex((nframes >> 24) & 0xFF)
        nframes_2 = hex((nframes >> 16) & 0xFF)
        nframes_1 = hex((nframes >> 8) & 0xFF)
        nframes_0 = hex((nframes >> 0) & 0xFF)
        nframes_3 = int(nframes_3, base=16)
        nframes_2 = int(nframes_2, base=16)
        nframes_1 = int(nframes_1, base=16)
        nframes_0 = int(nframes_0, base=16)
        nframes_3 = format(nframes_3, "x")
        nframes_2 = format(nframes_2, "x")
        nframes_1 = format(nframes_1, "x")
        nframes_0 = format(nframes_0, "x")
        print(nframes_3)
        print(nframes_2)
        print(nframes_1)
        print(nframes_0)
        print(nframes)
        print('compname=' + str(compname))
        print('comptype=' + str(comptype))
        print('N channels=' + str(nchannels))
        print('sample width='+str(sampwidth))
        print('framerate='+str(framerate))
        fOut.writelines(content)
        fOut.writelines('\n')
        wav.close()
    fOut.close()
    text2.insert(INSERT, 'Готово')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('900x100')
    window.title("flashFiller")

    lbl0 = Label(window, text="Выбор полноэкранных картинок")
    lbl0.grid(column=0, row=1)
    lbl1 = Label(window, text="Выбор маленьких картинок")
    lbl1.grid(column=0, row=2)
    lbl2 = Label(window, text="Выбор звуков")
    lbl2.grid(column=0, row=3)
    lbl3 = Label(window, text="Выбор директории выходного файла")
    lbl3.grid(column=0, row=0)

    text0 = Text(width=7, height=1)
    text0.grid(column=2, row=1, sticky=(W))
    # text0.pack()
    text1 = Text(width=7, height=1)
    text1.grid(column=2, row=2, sticky=(W))
    # text1.pack()
    text2 = Text(width=7, height=1)
    text2.grid(column=2, row=3, sticky=(W))
    # text2.pack()
    text3 = Text(width=70, height=1)
    text3.grid(column=2, row=0)

    btn0 = Button(window, text="Выбрать", command=selectFullScreens)
    btn0.grid(column=1, row=1)
    btn1 = Button(window, text="Выбрать", command=selectSmallImages)
    btn1.grid(column=1, row=2)
    btn2 = Button(window, text="Выбрать", command=selectSounds)
    btn2.grid(column=1, row=3)
    btn3 = Button(window, text="Выбрать", command=selectOutputDir)
    btn3.grid(column=1, row=0)

    window.mainloop()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
