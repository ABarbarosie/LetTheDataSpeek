from Tkinter import Tk, Label, OptionMenu
from ttk import Frame, Style
from webpage import WebPage
import re
import Tkinter


def OnMouseDown(event, arg, login, password, instr, flag, link):
    if flag.get() == 1:
        # get data locally
        print ""
    else:
        # get data from website
        print ""

    words = ["a","b"]

    for i in xrange(len(arg)):
        word = arg[i].get()
        if (word != ""):
            words += [word]

    page = WebPage(words)
    link.set(page.link)
    print page.link + "\n"

    #page.login('letthedataspeak','Ilovemagic!')
    #page.getContent(login,password)

    f1 = open('data.csv', 'r')
    file1 = f1.read();
    #f1.write(page.content)

    #csv = page.content

    con = ""
    for line in file1:
        con += line

    regex = '[0-9]+-.*?-.*?'
    for i in xrange(len(words)):
        regex += ',[0-9]+'
    
    info = re.findall(regex,con) #page.content instead of con
    
    data = []
    for i in xrange(len(info)):
        temp = re.findall(',[0-9]+,[0-9]+',info[i])
        num = re.findall(r'\d+',temp[0])
        data += num

    output = open('data.txt','w')
    for i in xrange(len(data)):
        output.write(data[i])
        if (i!=0 and i % len(words)):
            output.write('\n')
        else:
            output.write(' ')

    params = []
    for i in xrange(len(words)):
        params += instr[i].get()[0]
    print params


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

    options = ("Paino", "Instrument2", "Instrument3", "Instrument4", "Instrument5")
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
                instr = [default1,default2,default3,default4,default5], flag=cb, lnk=linkContent
                : OnMouseDown(event, arg, login, password, instr, flag, lnk))
    button_start.grid(row=8, column=1, columnspan=2, sticky='W')


    root.mainloop()


if __name__ == '__main__':
    main()
