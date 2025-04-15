import tkinter as tk
from tkinter import *
import webbrowser
import os


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #label for custom field
        self.lbl_custom = tk.Label(self.master,text='Enter custom text or click the Default HTML page button')
        self.lbl_custom.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    
        # field for custom user text
        self.custom_html = tk.Entry(self.master,text='')
        self.custom_html.grid(row=1,column=0,rowspan=20, columnspan=1,padx=(30,40),pady=(0,0),sticky=N+W)
    

        #default html button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=5,column=0,padx=(10,10), pady=(10,10), sticky=S+E)

        #custom user created html button
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=5,column=1,padx=(10,10), pady=(10,10), sticky=S+E)


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        # Mac seems to need this line to use realpath, otherwise the file gets created ok but does not open in the browser.
        webbrowser.open("file://" + os.path.realpath("index.html"))

    def customHTML(self):
        htmlText = self.custom_html.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        # Mac seems to need this line to use realpath, otherwise the file gets created ok but does not open in the browser.
        webbrowser.open("file://" + os.path.realpath("index.html"))





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
