from Tkinter import Tk, Label
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
    for index in range(1, len(data)):
        arg.create_line(
            index - 1, offset - data[index - 1], index, offset - data[index], fill="red")
        print index


class Application(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Let the Data Speek")


def main():
    root = Tk()
    root.geometry("1012x520+500+350")
    app = Application(root)

    frame = Tkinter.Frame(
        root, width=1000, height=100, borderwidth=2, highlightbackground="blue")
    frame.grid(row=0, column=0, rowspan=2, columnspan=5)

    label1 = Tkinter.Label(frame, text="1st Word", width=10, height=3)
    label2 = Tkinter.Label(frame, text="2nd Word", width=10, height=3)
    label3 = Tkinter.Label(frame, text="3rd Word", width=10, height=3)
    label4 = Tkinter.Label(frame, text="4th Word", width=10, height=3)
    label5 = Tkinter.Label(frame, text="5th Word", width=10, height=3)
    label1.grid(row=0, column=0, sticky='W')
    label2.grid(row=0, column=1, sticky='W')
    label3.grid(row=0, column=2, sticky='W')
    label4.grid(row=0, column=3, sticky='W')
    label5.grid(row=0, column=4, sticky='W')

    e1 = Tkinter.Entry(frame, width=20)
    e2 = Tkinter.Entry(frame, width=20)
    e3 = Tkinter.Entry(frame, width=20)
    e4 = Tkinter.Entry(frame, width=20)
    e5 = Tkinter.Entry(frame, width=20)
    e1.grid(row=1, column=0, sticky='W')
    e2.grid(row=1, column=1, sticky='W')
    e3.grid(row=1, column=2, sticky='W')
    e4.grid(row=1, column=3, sticky='W')
    e5.grid(row=1, column=4, sticky='W')

    canvas = Tkinter.Canvas(root, width=1000, height=400,
                            borderwidth=5, highlightbackground="black", bg="white", relief="groove")
    canvas.grid(row=2, column=0, columnspan=5, rowspan=2)

    button_start = Tkinter.Button(root, text="Sonify", width=15)
    button_start.bind("<Button-1>",
                      lambda event, arg=canvas: OnMouseDown(event, arg))
    button_start.grid(row=5, column=4)

    root.mainloop()

if __name__ == '__main__':
    main()
