import tkinter as tk
from PIL import Image, ImageTk
from lib.modString import addString, minusString

class drop:
	"""
	@ parent: frame that the "drop" is on
	@ name: string representing the drop's name
	@ raid_boss: the boss that drops 'drop'
	@ r, c: position in the grid
	@ cur count
	@ total count
	########################################
	@ parent: frame
	@ name: string, name of item drop
	@ raid_boss: boss class, name of boss that this drop belongs to
	@ cur_count: string, current count
	@ total_count: string, total
	@ label: label, total(current) displayed
	"""
	def __init__(self, parent, name, raid_boss, r, c, total='0', cur='0'):
		self.parent = parent
		self.name = name
		self.raid_boss = raid_boss
		self.cur_count = cur
		self.total_count = total
		self.label = tk.Label(parent, text=self.paint(), font=("Arial", 12))
		image = Image.open("img/"+raid_boss.name+"/"+self.name+".jpg")
		photo = ImageTk.PhotoImage(image)

		l = tk.Label(parent, image=photo)
		l.image = photo
		l.grid(row=r, column=c)

		l.bind('<Button-1>', self.increment)
		l.bind('<Button-3>', self.decrement)

		self.label.grid(row=r+1, column=c)

	def increment(self, event=None):
		self.cur_count = addString(self.cur_count, '1')
		self.total_count = addString(self.total_count, '1')
		self.label['text'] = self.paint()

		self.raid_boss.total = addString(self.raid_boss.total, '1')
		self.raid_boss.cur = addString(self.raid_boss.cur, '1')
		self.raid_boss.count_label['text'] = self.raid_boss.paint()

	def paint(self):
		return self.total_count+'('+self.cur_count+')'

	def decrement(self, event=None):
		if self.cur_count == '0' or self.total_count == '0':
			return
		self.cur_count = minusString(self.cur_count, '1')
		self.total_count = minusString(self.total_count, '1')
		self.label['text'] = self.paint()

		self.raid_boss.total = minusString(self.raid_boss.total, '1')
		self.raid_boss.cur = minusString(self.raid_boss.cur, '1')
		self.raid_boss.count_label['text'] = self.raid_boss.paint()