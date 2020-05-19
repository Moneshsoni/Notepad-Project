from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


class Notepad:
    window = Tk()
    window.title("Titled by Smokescreem - Notepad")
    window.geometry("700x400+600+100")
    text_area = Text(window, font=('Times New Roman', 15), bg="#ffffff", selectbackground="#0034fe", fg="#000000")
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    editemenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    scrollbar = Scrollbar(text_area)
    file = None

    def __init__(self):
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.text_area.grid(sticky=N + S + E + W)

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.newfile)
        self.filemenu.add_command(label="Save", command=self.savethefile)
        self.filemenu.add_command(label="Open", command=self.open)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", activebackground='red', command=self.quit)

        self.menubar.add_cascade(label="Configure", menu=self.editemenu)
        self.editemenu.add_command(label="Cut            ctrl+X", command=self.xut)
        self.editemenu.add_command(label="Select All    ctrl+A", command=self.selectall)
        self.editemenu.add_command(label="Copy            ctrl+C", command=self.copy)
        self.editemenu.add_command(label="Paste         ctrl+V", command=self.paste)

        self.menubar.add_cascade(label="About", menu=self.helpmenu)
        self.helpmenu.add_command(label="Excited to implement ", activebackground="light green", command=self.about)

        self.window.config(menu=self.menubar)
        self.scrollbar.pack(side=RIGHT, fill="y")

        self.scrollbar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

    def start(self):
        self.window.mainloop()

    def quit(self):
        ask = askyesno('Exit Really', "Are you Exiting :(")
        print(ask)
        if ask:
            self.window.destroy()
        else:
            pass

    def about(self):
        showinfo("About", "Created by Monesh soni Swami vivekanand college of Engineering ")

    def open(self):
        self.file = askopenfile(initialdir="/", title="Select file to open",
                                filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if self.file != NONE:
            self.text_area.delete(1.0, END)
            for i in self.file:
                self.text_area.insert(END, i)
        self.file.close()

    def newfile(self):
        self.window.title("New File")
        self.file = None
        self.text_area.delete(1.0, END)

    def savethefile(self):
        self.f = asksaveasfile(mode="w", defaultextension=".txt")
        if self.f is None:
            return
        text2save = self.text_area.get(1.0, END)
        self.f.write(text2save)
        self.f.close()

    def xut(self):
        self.text_area.event_generate("<<Cut>>")

    def selectall(self):
        self.text_area.event_generate("<<SelectAll>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")


obj1 = Notepad()
obj1.start()
