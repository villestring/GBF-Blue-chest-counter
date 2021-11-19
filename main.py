from tkinter import *
from tkinter import ttk
import sys
from lib.drop import drop

root = Tk()
root.title('Blue Chest Counter')
root.iconbitmap('img/GoldBrick.ico')
root.resizable(height=720, width=720)

notebook = ttk.Notebook(root)
notebook.pack()

frame_names = ['akasha', 'grandorder', 'probaha']
"""
next steps:
design frame class "boss"
init with name, notebook parent, width, height, and
an array consists the count of each drops

"""
akasha = Frame(notebook, padx=5, pady=5)
akasha.grid(row=0, column=0)
notebook.add(akasha, text="アーカーシャ", sticky=E+W+N+S)

goldbrick = drop(akasha, "GoldBrick", 'akasha', 0, 0)
key = drop(akasha, "Key", 'akasha', 0, 1)

grandorder = Frame(notebook, padx=5, pady=5)
grandorder.grid(row=0, column=0)
notebook.add(grandorder, text="ジ・オーダー・グランデ", sticky=E+W+N+S)
# with open('usr/data.log') as file:
# 	for line in file:
def on_closing():
	# write on file
	# close file
	root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

