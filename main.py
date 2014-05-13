from Tkinter import Tk, Label, OptionMenu
from ttk import Frame, Style
from webpage import WebPage
import re
import Tkinter
import sys
import subprocess
import os

def OnMouseDown(event, arg, login, password, instr, flag, link, canvas):
    words = []
    for i in xrange(len(arg)):
        if (arg[i].get() != ""):
            words += [arg[i].get()]

    if flag.get() == 1:
        # only to set the link
        page = WebPage(words)
        link.set(page.link)

        # get data locally
        globalFile = open('data.csv', 'r')
        globalC = globalFile.read()

        globalCon = ""
        for line in globalC:
            globalCon += line

        regex = '[0-9]+-.*?-.*?'
        for i in xrange(len(words)):
            regex += ',[0-9]+'
        globalInfo = re.findall(regex,globalCon)

        regex = ""
        for i in xrange(len(words)):
            regex += ',[0-9]+'

        globalData = []
        for i in xrange(len(globalInfo)):
            temp = re.findall(regex,globalInfo[i])
            num = re.findall(r'\d+',temp[0])
            globalData += num
        # read individual
        allwords = []
        for i in xrange(len(words)):
            string = words[i] + ".csv"
            fle = open(string, 'r')
            file1 = fle.read()
            con = ""
            for line in file1:
                con += line
            info = re.findall(r'[0-9]+-.*?-.*?,[0-9]+',con)
            data = []
            for j in xrange(len(info)):
                temp = re.findall(',[0-9]+',info[j])
                num = re.findall(r'\d+',temp[0])
                data += num
            allwords.append(data)

        # output
        output = open('Java/LetTheDataSpeak/data.txt','w')
        for i in xrange(len(allwords[0])):
            for j in xrange(len(allwords)):
                output.write(allwords[j][i] + " " + globalData[i*len(words)+j] + " ")
            output.write("\n")

    else:
        # get data from website
        page = WebPage(words)
        link.set(page.link)

        page.getContent(login,password)
        # get global data
        globalFile = open('data.csv', 'r')
        globalC = globalFile.read()

        globalCon = ""
        for line in globalC:
            globalCon += line

        regex = '[0-9]+-.*?-.*?'
        for i in xrange(len(words)):
            regex += ',[0-9]+'
        globalInfo = re.findall(regex,globalCon)

        regex = ""
        for i in xrange(len(words)):
            regex += ',[0-9]+'
        globalData = []
        for i in xrange(len(globalInfo)):
            temp = re.findall(regex,globalInfo[i])
            num = re.findall(r'\d+',temp[0])
            globalData += num

        for i in xrange(len(words)):
            page = WebPage([words[i]])
            link.set(page.link)
            page.getContent(login,password)

        # rename 
        for i in xrange(len(words)):
            bashCommand = "rename "
            bashCommand += "data(" + str(i+1) + ").csv " + words[i] + ".csv"
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]

        # read individual
        allwords = []
        for i in xrange(len(words)):
            string = words[i] + ".csv"
            fle = open(string, 'r')
            file1 = fle.read()
            con = ""
            for line in file1:
                con += line
            info = re.findall(r'[0-9]+-.*?-.*?,[0-9]+',con)
            data = []
            for j in xrange(len(info)):
                temp = re.findall(',[0-9]+',info[j])
                num = re.findall(r'\d+',temp[0])
                data += num
            allwords.append(data)

        # output
        output = open('Java/LetTheDataSpeak/data.txt','w')
        for i in xrange(len(allwords[0])):
            for j in xrange(len(allwords)):
                output.write(allwords[j][i] + " " + globalData[i*len(words)+j] + " ")
            output.write("\n")




    canvas.create_line(0,114,520,114, fill="black", width = 4)
    color = ["coral", "yellow", "green", "blue", "red"]
    # visualisation
    for i in xrange(len(words)):
        for j in xrange(len(allwords[0])):
            if (j<520):
                canvas.create_line(j,110-int(allwords[i][j]),j+1,110-int(allwords[i][j+1]),
                    fill=color[i], width=1)

    ARGS = "ARGS="
    for i in xrange(len(words)):
        ARGS += instr[i].get() + ' '

    ARGS += ""
    print ARGS
    sys.stdout.flush()
    command = "make " + ARGS
    ret1 = os.fork()
    if ret1==0:
        # os.system(command)
        subprocess.call(["make", ARGS])
    else:
        os.wait(ret1)
    #     import time
    #     time.sleep(1)
    #     sys.exit(0)



class Application(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Let the Data Speak")

def main():
    root = Tk()
    root.geometry("525x650+500+350")
    app = Application(root)

    label1 = Tkinter.Label(root, text = "1st Word", width = 20, height = 3)
    label2 = Tkinter.Label(root, text = "2nd Word", width = 20, height = 3)
    label3 = Tkinter.Label(root, text = "3rd Word", width = 20, height = 3)
    label4 = Tkinter.Label(root, text = "4th Word", width = 20, height = 3)
    label5 = Tkinter.Label(root, text = "5th Word", width = 20, height = 3)
    label1.grid(row=3, column=0, sticky='W')
    label2.grid(row=4, column=0, sticky='W')
    label3.grid(row=5, column=0, sticky='W')
    label4.grid(row=6, column=0, sticky='W')
    label5.grid(row=7, column=0, sticky='W')

    e1 = Tkinter.Entry(root,width=20)
    e2 = Tkinter.Entry(root,width=20)
    e3 = Tkinter.Entry(root,width=20)
    e4 = Tkinter.Entry(root,width=20)
    e5 = Tkinter.Entry(root,width=20)
    e1.grid(row=3, column=1, sticky='W')
    e2.grid(row=4, column=1, sticky='W')
    e3.grid(row=5, column=1, sticky='W')
    e4.grid(row=6, column=1, sticky='W')
    e5.grid(row=7, column=1, sticky='W')

    options = ("PIANO", "GUITAR", "TRUMPET", "VIOLIN", "XYLOPHONE")
    default1 = Tkinter.StringVar()
    default1.set("Pick an instrument")

    default2 = Tkinter.StringVar()
    default2.set("Pick an instrument")

    default3 = Tkinter.StringVar()
    default3.set("Pick an instrument")

    default4 = Tkinter.StringVar()
    default4.set("Pick an instrument")

    default5 = Tkinter.StringVar()
    default5.set("Pick an instrument")


    opt1 = Tkinter.OptionMenu(root, default1, *options)
    opt1.config(width=15)
    opt1.grid(row=3, column=2, sticky="ew")

    opt2 = Tkinter.OptionMenu(root, default2, *options)
    opt2.config(width=15)
    opt2.grid(row=4, column=2, sticky="ew")

    opt3 = Tkinter.OptionMenu(root, default3, *options)
    opt3.config(width=15)
    opt3.grid(row=5, column=2, sticky="ew")

    opt4 = Tkinter.OptionMenu(root, default4, *options)
    opt4.config(width=15)
    opt4.grid(row=6, column=2, sticky="ew")

    opt5 = Tkinter.OptionMenu(root, default5, *options)
    opt5.config(width=15)
    opt5.grid(row=7, column=2, sticky="ew")

    empty1 = Tkinter.Label(root, text = "")
    empty1.grid(row=17, column=0, columnspan=3)

    empty2 = Tkinter.Label(root, text = "")
    empty2.grid(row=11, column=0, columnspan=3)

    empty3 = Tkinter.Label(root, text = "")
    empty3.grid(row=12, column=0, columnspan=3)

    empty6 = Tkinter.Label(root, text = "")
    empty6.grid(row=2, column=0, columnspan=3)


    loginEntry = Tkinter.Entry(root,width=20)
    passwordEntry = Tkinter.Entry(root,width=20,show="*")
    loginEntry.grid(row=0,column=1, sticky = 'W')
    passwordEntry.grid(row=1,column=1, sticky='W')

    loginLabel = Tkinter.Label(root, text = "Login: ", width = 20, height = 3)
    passwordLabel = Tkinter.Label(root, text = "Password: ", width = 20, height = 3)
    loginLabel.grid(row=0,column=0, sticky='W')
    passwordLabel.grid(row=1,column=0, sticky='W')

    linkContent = Tkinter.StringVar()
    linkContent.set("Link to the data:")
    link = Tkinter.Entry(root, width=40, textvariable=linkContent)
    link.grid(row=18, column=0, columnspan=3, sticky='W')

    cb = Tkinter.IntVar()
    checkButton = Tkinter.Checkbutton(root,text="Local Data", variable = cb)
    checkButton.grid(row=0,column=2)

    canvas = Tkinter.Canvas(root, width=512, height=125, 
        borderwidth=5, highlightbackground="black", bg="white", relief="groove")
    canvas.grid(row=13, column=0, columnspan=3, rowspan=4)

    button_start = Tkinter.Button(root, text ="DO THE MAGIC", width=17, height=3, bg="red")
    button_start.bind("<Button-1>",
        lambda event, arg=[e1,e2,e3,e4,e5], login=loginEntry.get(), password=passwordEntry.get(),
                instr = [default1,default2,default3,default4,default5], flag=cb, lnk=linkContent,
                cnv = canvas
                : OnMouseDown(event, arg, login, password, instr, flag, lnk, cnv))
    button_start.grid(row=8, column=1, columnspan=2, sticky='W')


    root.mainloop()


if __name__ == '__main__':
    main()
