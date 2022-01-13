# This is a sample Python script.

from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
from tkinter.filedialog import *
import os
# import scipy
# import wave
# from scipy.io import wavfile
import numpy as np
# import soundfile as sf
# from scipy.io.wavfile import read

# outputFile = "C:/Users/Stasy/Desktop/output2FLASH.txt"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def selectOutputDir():
    OutputDir = filedialog.askdirectory(parent=window)
    outputFile = OutputDir+'/output2FLASH.bin'
    text3.insert(INSERT, outputFile)
    # return outputFile
    # outputFile = 'C:/Users/Stasy/Desktop/output2FLASH.txt'

def selectFullScreens():
    outputFile = format(text3.get("1.0", 'end-1c'))
    fileNames = askopenfilenames(parent=window)
    fileNames = sorted(fileNames)
    # fOut = open(outputFile, 'w')
    fOut = open(outputFile, 'wb')
    for fileName in fileNames:
        f = open(fileName)
        lines = f.readlines()
        for line in lines:
            for word in line.split(' '):
                if word.startswith('0x'):
                    line = re.findall(r'[0x]\w+', str(line))
                    length_of_string=len(re.findall(r'[0x]\w+', str(line)))
                    line = str(line)
                    # print(line)
                    line = re.sub(r'\]', '', line)
                    line = re.sub(r'\[', '', line)

                    # line = re.sub(r'0x', '', line)
                    line = re.sub(r'\'', '', line)
                    line = re.sub(r'\ ', '', line)
                    # fOut.writelines(line+',')
                    # fOut.writelines('\n')
                    line = str(line)
                    # print(line)
                    values=line.split(",")
                    # line = str(line)
                    # print(values)
                    # print(type(values))

                    ############################################################################### bin ############
                    bytes=[]
                    for i in range(length_of_string):
                        bytes.append(int((values[i]), base=16))
                    for i in range(length_of_string):
                        fOut.write(int.to_bytes(bytes[i],1,byteorder='big'))
                    break
        f.close()
        print(fileName)
        # print(len(filenames))
    # adds = 0
    # for i in range(1, 256+1-len(fileNames), 1):
    #     for j in range(1, 128+1, 1):
    #         adds = ('ff,'*64)+'\n'
    #         adds = re.sub(r'\]', '', adds)
    #         adds = re.sub(r'\[', '', adds)
    #         # adds = re.sub(r'0x', '', adds)
    #         adds = re.sub(r'\'', '', adds)
    #         adds = re.sub(r'\ ', '', adds)
    #         # print(adds)
    #         # fOut.writelines(adds)
    #         # fOut.writelines('\n')
    # print(i)
    # print(int(len(adds)/5))
    # print(adds)
        # print(len(fileNames))
    add='0xff'
    add=int(add,base=16)
    for i in range((256-len(fileNames))*8192):
        fOut.write(int.to_bytes(add, 1, byteorder='big'))
    fOut.close()
    text0.insert(INSERT, 'Готово')


def selectSmallImages():
    outputFile = format(text3.get("1.0", 'end-1c'))
    fileNamesSmall = askopenfilenames(parent=window)
    fileNamesSmall = sorted(fileNamesSmall)
    print(len(fileNamesSmall))
    for fileNameSmall in fileNamesSmall:
        f = open(fileNameSmall)
        last_line = f.readlines()[-3]
        f.close()
        last_line = re.split(r',', last_line)
        print(last_line)
        height = last_line[1]
        width = last_line[2]
        print(width)
        print(height)
        print(type(width))
        print(type(height))
        height = int(height, base=10)
        width = int(width, base=10)
        print(width)
        print(height)
        print(type(width))
        print(type(height))
        if (height % 2) != 0:
            height += 1
        length = int(int(height) * int(width) / 2)
        length += 2

        # height = format(height, "x")
        # width = format(width, "x")
        # width=hex(width)
        # height=hex(height)
        # width = int(width, base=10)
        # height = int(height, base=10)
        # print(width)
        # print(height)
        # print(type(width))
        # print(type(height))

#################################################################################
        f = open(fileNameSmall)          #   width and height became known
        fOut = open(outputFile, 'ab')
        lines = f.readlines()
        fOut.write(int.to_bytes(width, 1, byteorder='big'))
        fOut.write(int.to_bytes(height, 1, byteorder='big'))
        # imDimensions = str(width) + ',' + str(height) + ',\n'
        # fOut.writelines(imDimensions)
        for line in lines:
            for word in line.split(' '):
                if word.startswith('0x'):
                    line = re.findall(r'[0x]\w+', str(line))
                    length_of_string = len(re.findall(r'[0x]\w+', str(line)))
                    line = str(line)
                    line = re.sub(r'\]', '', line)
                    line = re.sub(r'\[', '', line)
                    # line = re.sub(r'0x', '', line)
                    line = re.sub(r'\'', '', line)
                    line = re.sub(r'\ ', '', line)
                    # fOut.writelines(line + ',')
                    # fOut.writelines('\n')
                    # print(line)
                    values = line.split(",")
                    bytes = []
                    for i in range(length_of_string):
                        bytes.append(int((values[i]), base=16))
                    for i in range(length_of_string):
                        fOut.write(int.to_bytes(bytes[i], 1, byteorder='big'))
                    break
        f.close()
        # complement=0
        if (length < 8192):
            print('small image')
            print(fileNameSmall)
            complement = '0xff'
            complement = int(complement, base=16)
            for i in range(8192-length):
                fOut.write(int.to_bytes(complement, 1, byteorder='big'))
            # for i in range(1, int((8192 - length)/64)+1, 1):
                # complement = ('ff,' * 64) + '\n'
                # complement = re.sub(r'\]', '', complement)
                # complement = re.sub(r'\[', '', complement)
                # # complement = re.sub(r'0x', '', complement)
                # complement = re.sub(r'\'', '', complement)
                # complement = re.sub(r'\ ', '', complement)
                # print(adds)
            #     fOut.writelines(complement)
            # nComplements = 64*i
            # nAddComplements = 8192 - length - nComplements
            # print(nComplements + int(length)+nAddComplements)
            #
            # if (nComplements+length)<8192:
            #     complement = ('ff,'*nAddComplements)+'\n'
            #     complement = re.sub(r'\]', '', complement)
            #     complement = re.sub(r'\[', '', complement)
            #     complement = re.sub(r'\'', '', complement)
            #     complement = re.sub(r'\ ', '', complement)
            #     fOut.writelines(complement)
            # print(i)
            adds = '0xff'
            adds = int(adds, base=16)
            # print(adds)
    for i in range((256-len(fileNamesSmall))*8192):
        fOut.write(int.to_bytes(adds, 1, byteorder='big'))
    # for m in range(1, 256 + 1 - len(fileNames), 1):
    #     for n in range(1, 128 + 1, 1):
    #         adds = ('ff,' * 64) + '\n'
    #         adds = re.sub(r'\]', '', adds)
    #         adds = re.sub(r'\[', '', adds)
    #         # adds = re.sub(r'0x', '', adds)
    #         adds = re.sub(r'\'', '', adds)
    #         adds = re.sub(r'\ ', '', adds)
    #         # print(adds)
    #         fOut.writelines(adds)
    #         # fOut.writelines('\n')
    # # print(n)
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
#################Adding adds after images before sounds##########################################
    adds = '0xff'
    adds = int(adds, base=16)
    for n in range(262144*64):
        fOut.write(int.to_bytes(adds, 1, byteorder='big'))
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
    prevAddr = 20973824

    for fileName in fileNames:
        frames=''
        wav = wave.open(fileName, mode="r")
        (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
        print(fileName)
###############################################  soundNum obtaining ###############################
        soundNum = soundNum + 1
        soundNumHex = hex(soundNum)
        print('soundNum='+str(soundNumHex))
        soundNumHex = int(soundNumHex, base=16)
        soundNumHex = format(int(soundNumHex), 'x')
        print('soundNum='+str(soundNumHex))
################################################ length of sounв obtaining ########################
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
        print('nframes_3=' + str(nframes_3))
        print('nframes_2=' + str(nframes_2))
        print('nframes_1=' + str(nframes_1))
        print('nframes_0=' + str(nframes_0))
        print('nframes=' + str(nframes))
        # print('compname=' + str(compname))
        # print('comptype=' + str(comptype))
        # print('N channels=' + str(nchannels))
        # print('sample width='+str(sampwidth))
        # print('framerate='+str(framerate))
##################################################### current address obtaining #####################
        currAddr = prevAddr                         # bubble
        currAddr_3 = hex((currAddr >> 24) & 0xFF)
        currAddr_2 = hex((currAddr >> 16) & 0xFF)
        currAddr_1 = hex((currAddr >> 8) & 0xFF)
        currAddr_0 = hex((currAddr >> 0) & 0xFF)
        currAddr_3 = int(currAddr_3, base=16)
        currAddr_2 = int(currAddr_2, base=16)
        currAddr_1 = int(currAddr_1, base=16)
        currAddr_0 = int(currAddr_0, base=16)
        currAddr_3 = format(currAddr_3, "x")
        currAddr_2 = format(currAddr_2, "x")
        currAddr_1 = format(currAddr_1, "x")
        currAddr_0 = format(currAddr_0, "x")
        print('currAddr_3=' + str(currAddr_3))
        print('currAddr_2=' + str(currAddr_2))
        print('currAddr_1=' + str(currAddr_1))
        print('currAddr_0=' + str(currAddr_0))
        print('currAddr=' + str(currAddr))
        prevAddr = currAddr + nframes               # bubble
##################################################### write info to infoPage ########################
        fOut.writelines(str(soundNumHex)+','+str(currAddr_3)+','+str(currAddr_2)+','+str(currAddr_1)+','
                        +str(currAddr_0)+','+str(nframes_3)+','+str(nframes_2)+','+str(nframes_1)+','
                        +str(nframes_0)+',')
        fOut.writelines('\n')
##################################################### write adds after soundInfo to output file #####
    if len(fileNames)<256:
        nSoundComplements = (256 - len(fileNames)) * 9
        soundComplement = ('ff,' + '\n' )
        for i in range(1, nSoundComplements+1, 1):
            fOut.writelines(soundComplement)
##################################################### write content to output file ##################
    for fileName_ in fileNames:
        print(fileName_)
        frames = ''
        wav = wave.open(fileName_, mode="r")
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
        # print(content)
        fOut.writelines(content + ',')
        fOut.writelines('\n')
        wav.close()
    fOut.close()
    text2.insert(INSERT, 'Готово')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('1100x100')
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
    text3 = Text(width=100, height=1)
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