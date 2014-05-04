from Tkinter import Tk, Label, OptionMenu
from ttk import Frame, Style
from webpage import WebPage
import re
import Tkinter


def OnMouseDown(event, arg):

    page = WebPage(["boobs","money"])
    print page.link + "\n"

    #page.login('letthedataspeak','Ilovemagic!')
    page.getContent()

    f1 = open('data.csv', 'w')
    f1.write(page.content)

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 20, 30, 100, 70, 30, 40, 55, 56, 58, 60, 39, 38, 35, 36]
    offset = 100
<<<<<<< HEAD
    for index in range(1,len(data)):
        arg[0].create_line(index-1,offset-data[index-1],index,offset-data[index],fill="red")
    arg[1].delete(0,END)
    arg[1].insert(0,page.getLink())
=======
    for index in range(1, len(data)):
        arg.create_line(
            index - 1, offset - data[index - 1], index, offset - data[index], fill="red")
        print index
>>>>>>> 5a686eefa053c070ef70235f68ba5bd3a3c26610


class Application(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Let the Data Speak")

def main():
    root = Tk()
    root.geometry("525x550+500+350")
    app = Application(root)

    label1 = Tkinter.Label(root, text = "1st Word", width = 20, height = 3)
    label2 = Tkinter.Label(root, text = "2nd Word", width = 20, height = 3)
    label3 = Tkinter.Label(root, text = "3rd Word", width = 20, height = 3)
    label4 = Tkinter.Label(root, text = "4th Word", width = 20, height = 3)
    label5 = Tkinter.Label(root, text = "5th Word", width = 20, height = 3)
    label1.grid(row=1, column=0, sticky='W')
    label2.grid(row=2, column=0, sticky='W')
    label3.grid(row=3, column=0, sticky='W')
    label4.grid(row=4, column=0, sticky='W')
    label5.grid(row=5, column=0, sticky='W')

    e1 = Tkinter.Entry(root,width=20)
    e2 = Tkinter.Entry(root,width=20)
    e3 = Tkinter.Entry(root,width=20)
    e4 = Tkinter.Entry(root,width=20)
    e5 = Tkinter.Entry(root,width=20)
    e1.grid(row=1, column=1, sticky='W')
    e2.grid(row=2, column=1, sticky='W')
    e3.grid(row=3, column=1, sticky='W')
    e4.grid(row=4, column=1, sticky='W')
    e5.grid(row=5, column=1, sticky='W')

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
    opt1.grid(row=1, column=2, sticky="ew")

    opt2 = Tkinter.OptionMenu(root, default2, *options)
    opt2.config(width=15)
    opt2.grid(row=2, column=2, sticky="ew")

    opt3 = Tkinter.OptionMenu(root, default3, *options)
    opt3.config(width=15)
    opt3.grid(row=3, column=2, sticky="ew")

    opt4 = Tkinter.OptionMenu(root, default4, *options)
    opt4.config(width=15)
    opt4.grid(row=4, column=2, sticky="ew")

    opt5 = Tkinter.OptionMenu(root, default5, *options)
    opt5.config(width=15)
    opt5.grid(row=5, column=2, sticky="ew")

    empty1 = Tkinter.Label(root, text = "")
    empty1.grid(row=15, column=0, columnspan=3)

    empty2 = Tkinter.Label(root, text = "")
    empty2.grid(row=9, column=0, columnspan=3)

    empty3 = Tkinter.Label(root, text = "")
    empty3.grid(row=10, column=0, columnspan=3)

    empty4 = Tkinter.Label(root, text = "")
    empty4.grid(row=0, column=0, columnspan=3)


    link = Tkinter.Entry(root, width=40)
    link.grid(row=16, column=0, columnspan=3, sticky='W')
    link.insert(0,"Link to the data:")

    canvas = Tkinter.Canvas(root, width=512, height=125, 
        borderwidth=5, highlightbackground="black", bg="white", relief="groove")
    canvas.grid(row=11, column=0, columnspan=3, rowspan=4)

    button_start = Tkinter.Button(root, text ="DO THE MAGIC", width=17, height=3, bg="red")
    button_start.bind("<Button-1>",
        lambda event, arg=[canvas,link]: OnMouseDown(event, arg))
    button_start.grid(row=6, column=1, columnspan=2, sticky='W')

    root.mainloop()

if __name__ == '__main__':
    main()
