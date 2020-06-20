import tkinter as tk
import shutil
import os

def move(pathFrom,pathDest,*suffix):
    try:
        for element in os.listdir(pathFrom):
            if element.endswith(suffix):
                shutil.move(os.path.join(pathFrom,element),pathDest)
        label = tk.Label(text='Files moved!')
        label.grid(row=8, column=0)
    except WindowsError:
        label = tk.Label(text='Path not found, try again')
        label.grid(row=8, column=0)



def draw():
    title=tk.Label(text='Hello, this is a program to automatically move your files from a folder to another!',font='helvetica')
    title.grid(row=0,column=0, sticky='N', padx=20, pady=20)

    instruction1=tk.Label(text='Please insert the full path of the folder you want to move files from.', font='helvetica')
    instruction1.grid(row=1,column=0, sticky='WE',padx=20,pady=20)

    text1=tk.Entry()
    text1.grid(row=2,column=0,sticky='WE',padx=20)

    instruction2=tk.Label(text='Write here the full path of the folder of destination of files.', font='helvetica')
    instruction2.grid(row=3,column=0, sticky='WE',padx=20,pady=20)

    text2=tk.Entry()
    text2.grid(row=4,column=0,sticky='WE',padx=20)

    instruction3=tk.Label(text='Write the extension of the file to move (nothing for moving all files)', font='helvetica')
    instruction3.grid(row=5,column=0, sticky='WE',padx=20,pady=20)

    text3=tk.Entry()
    text3.grid(row=6,column=0,sticky='WE',padx=20)

    start=tk.Button(text='Start moving!',font=('helvetica',16), height=3,width=50,command=lambda: move(text1.get(),text2.get(),text3.get()))
    start.grid(row=7,column=0, padx=30,pady=10)

def main():
    global window
    window=tk.Tk()
    window.title('File mover')
    window.geometry('600x500')
    window.grid_columnconfigure(0,weight=1)

if __name__=='__main__':
    global window
    main()
    draw()
    window.mainloop()
