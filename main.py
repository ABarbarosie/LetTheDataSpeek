from Tkinter import Tk, Label
from ttk import Frame, Style
from webpage import WebPage
import re

class Application(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        self.parent.title("Let the Data Speek")
        page = WebPage(["The","words","go","here"])
        print page.link + "\n"
        page.getContent()
        obj = re.findall(r'\[\{".*?\]',page.content)
        print obj[1]      

def main():
    root = Tk()
    root.geometry("300x280+300+300")
    app = Application(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  