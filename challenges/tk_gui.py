from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        # buttons
        self.btn_browse1 = tk.Button(self.master, width=12, height=1, text='Browse...', command=self.select_source)
        self.btn_browse1.grid(row=0, column=0, padx=(25,0), pady=(30,0), sticky=W)
        
        self.btn_browse2 = tk.Button(self.master, width=12, height=1, text='Browse...', command=self.select_destination)
        self.btn_browse2.grid(row=1, column=0, padx=(25,0), pady=(0,0), sticky=W)

        self.btn_dir = tk.Button(self.master, width=12, height=2, text='Check for files...', command=self.directory_path)
        self.btn_dir.grid(row=2, column=0, padx=(25,0), pady=(0,0), sticky=W)

        self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program', command=self.master.quit)
        self.btn_close.grid(row=2, column=1, padx=(0,0), pady=(0,0), sticky=S+E)

        # entry boxes
        self.entry1 = tk.Entry(self.master, width=50)
        self.entry1.grid(row=0, column=1, rowspan=8, columnspan=10, padx=(20,0), pady=(30,0), sticky=N+W)

        self.entry2 = tk.Entry(self.master, width=50)
        self.entry2.grid(row=1, column=1, rowspan=8, columnspan=10, padx=(20,0), pady=(0,0), sticky=N+W)

    # Functions to update entries with directory paths
    def select_source(self):
        path = filedialog.askdirectory(title="Select Source Directory")
        if path:
            self.entry1.delete(0, END)
            self.entry1.insert(0, path)

    def select_destination(self):
        path = filedialog.askdirectory(title="Select Destination Directory")
        if path:
            self.entry2.delete(0, END)
            self.entry2.insert(0, path)

    def directory_path(self):
        # Do something with the selected directories
        src = self.entry1.get()
        dst = self.entry2.get()
        print(f"Source: {src}\nDestination: {dst}")
        # You can add logic to check files here


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
