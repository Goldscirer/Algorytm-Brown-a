from tkinter import *
from tkinter import filedialog
from main import main


def add_file():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    print(root.filename)


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Brown")
        self.pack(fill=BOTH, expand=1)
        addFileButton = Button(self, text="Add file...", command=add_file)
        addFileButton.place(x=50, y=50)
        runButton = Button(self, text="Run", command=self.run)
        runButton.place(x=50, y=100)

    def run(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()