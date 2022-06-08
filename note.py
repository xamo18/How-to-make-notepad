from tkinter import *
from tkinter import filedialog
root = Tk()
root.geometry('500x400')

def save():
    file = filedialog.asksaveasfile(mode='w',initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('text','*txt')])
    try:
        save = str(text.get(10,END))
        file.write(save)
        file.close
    except:
        pass
def open():
    file = filedialog.askopenfile(mode='w',filetypes=[('text','*txt')])
    try:
        if file != None:
            text.delete(10,END)
            x=file.read()
            text.insert(end,x)
    except:
        pass

#menu_bar
menu_bar = Menu(root)
menu_bar.add_command(label='Open',command=open)
menu_bar.add_command(label='Save',command=save)
menu_bar.add_command(label='Quit',command=root.quit)
root.config(menu = menu_bar)

#Scrollbar
scrolly = Scrollbar(root)
scrollx = Scrollbar(root, orient='horizontal')
scrolly.pack(side=RIGHT,fill=Y)
scrollx.pack(side=BOTTOM,fill=X)

#Text widget
text = Text(root,font='Normal 14',background='white',yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
text.pack(expand=True,fill=BOTH)
scrolly.config(command=text.yview)
scrollx.config(command=text.xview)


root.mainloop()