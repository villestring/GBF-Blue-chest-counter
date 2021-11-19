from tkinter import *
from tkinter import ttk
import sys
from lib.boss import boss

root = Tk()
root.title('Blue Chest Counter')
root.iconbitmap('img/GoldBrick.ico')
# root.resizable(height=720, width=720)

notebook = ttk.Notebook(root)
notebook.pack()

frame_names = [['akasha', 'アーカーシャ'], 
				['grandorder', 'グランデ'], 
				['probaha', 'つよバハ']]


bosses = []
for boss_name, boss_title in frame_names:
	boss_frame = Frame(notebook, padx=5, pady=5)
	boss_frame.grid(row=0, column=0)
	notebook.add(boss_frame, text=boss_title, sticky=E+W+N+S)
	b = boss(boss_frame, boss_name, boss_title)
	bosses.append(b)

def on_closing():
	# write on file
	# close file
	for b in bosses:
		b.update()
	root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

