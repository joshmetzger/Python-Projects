import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import time
import datetime

class ParentWindow(Frame):
    def __init__(self, master):

        
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")


        #create button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # position source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        ##create entry for source directory selection
        self.source_dir = Entry(width=75)
        ##position entry in GUI using tkinter grid() padx and pady are the same as the button to ensure they line up                    
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        # button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # position destination button in GUI using grid() on next row under source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        # create entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # position entry in GUI using grid(), padx and pady are same as button to line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15, 10))

        # create trnasfer files button
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # position transfer button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        # createexit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        # position transfer button
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))



    #function to select source dir
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        if selectSourceDir:
            # clear content that is inserted in entry widget, allows path to be inserted into widget properly
            self.source_dir.delete(0, END)
            # insert user selection in source_dir Entry
            self.source_dir.insert(0, selectSourceDir)


    #function to destination source dir
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        if selectDestDir:
            # clear content that is inserted in entry widget, allows path to be inserted into widget properly
            self.destination_dir.delete(0, END)
            # insert user selection in destination_dir Entry
            self.destination_dir.insert(0, selectDestDir)

    
    #function to transfer the files from source to destination
    def transferFiles(self):
        #get source directory
        source = self.source_dir.get()
        #get destination directory
        destination = self.destination_dir.get()
        # get list of files in the source directory
        source_files = os.listdir(source)

        #get time to for 24 hour logic
        now = time.time()
        one_day = 24*60*60
        
        # iterate through each file in source dir
        for i in source_files:

            # check for hidden Mac files (DS_Store)
            if i == 'DS_Store':
                continue
            
            src = os.path.join(source, i)
            dst = os.path.join(destination, i)

            # check creation and modification times
            created_at = os.path.getctime(src)
            modified_at = os.path.getmtime(src)

            # if file has been created or updated in the last 24 hours, move to Customer Destination
            # if(now - created_at <= one_day) or (now - modified_at <= one_day):
            # it looks like in macOS is only metadata changes, so even copying files into source folder will casue those files to be transfered..
            if(now - modified_at <= one_day):
                if not os.path.exists(dst):
                    #move each file from source to destination
                    shutil.move(src, dst)
                    print(i + ' was created at: ' + str(datetime.datetime.fromtimestamp(created_at)))
                    print(i + ' was modified at: ' + str(datetime.datetime.fromtimestamp(modified_at)))
                    print(i + ' was transferred.')
                else:
                    print(i + ' already exists.')
            else:
                print(i + ' was not modified/created in the last 24 hours')
                  




            
    def exit_program(self):
        # root is the main GUI window, tkinter destroy method tells python to terminate root.mainloop and all widgets inside GUI window
        root.destroy()


    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
