import tkinter as tk
from PIL import Image, ImageTk
from lib.addString import addString

class drop:
	"""
	@ name: string representing the drop's name
	@ icon: an relative address to where the item's icon is stored
	@ current count
	@ total count
	@ button: a button class that does the counting
	"""
	def __init__(self, parent, name, boss_name, r, c, cur='0', total='0'):
		self.parent = parent
		self.name = name
		self.cur_count = cur
		self.total_count = total
		self.label = tk.Label(parent, text=self.paint(), font=("Arial", 12))
		image = Image.open("img/"+boss_name+"/"+self.name+".jpg")
		photo = ImageTk.PhotoImage(image)

		l = tk.Label(parent, image=photo)
		l.image = photo
		l.grid(row=r, column=c)

		l.bind('<Button-1>', self.increment)

		self.label.grid(row=r+1, column=c)

	def increment(self, event=None):
		self.cur_count = addString(self.cur_count, '1')
		self.total_count = addString(self.total_count, '1')
		self.label['text'] = self.paint()

	def paint(self):
		return self.total_count+'('+self.cur_count+')'