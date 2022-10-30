from tkinter import *
from tkinter import ttk

from pyparsing import col

LENGTH = 400
WIDTH = 400

class MainWindow():
    
    def __init__(self,mainWidget):
        self.main_frame = ttk.Frame(mainWidget,width=400, height=400)
        self.main_frame.grid(row=0,column=0)
        
        self.some_kind_of_controler = 0
        self.main_gui()

    def main_gui(self):
        root.title("Trippie")
        self.l1 = ttk.Label(self.main_frame,text="No. of Persons")
        self.l1.grid(row=0,column=0)
        
        self.next_ = ttk.Button(self.main_frame,text="NEXT")
        self.next_.grid(row=1,column=0)
        self.next_.bind('<Button-1>', self.next_gui)
        
        self.gui_elements = [self.l1,
                             self.next_]
    
    def next_gui(self, event):
        self.gui_elements_remove(self.gui_elements)
        
        self.l1 = ttk.Label(self.main_frame,text="Name\tRS\tNotes")
        self.l1.grid(row=0, column=0)
        
        self.n1 = ttk.Entry(self.main_frame).get()
    
    def gui_elements_remove(self, elements):
        for element in elements:
            element.destroy()

def main():
    global root

    root = Tk()
    root.geometry('400x400')
    window = MainWindow(root)

    root.mainloop()

if __name__ == '__main__':
    main()

# window = tk.Tk()
# window.geometry("400x400")
# nop = tk.Label(text="No. of Persons")
# nop.pack()

# count = tk.Entry()
# count.pack()

# # Python has theirs by default keywords
# # which we can not use as the variable name.
# # To avoid such conflict between python keyword 
# # and variable we use underscore after the name 
# next_ = tk.Button(text="NEXT")
# next_.pack()