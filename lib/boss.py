import tkinter as tk
from PIL import Image, ImageTk
from lib.modString import addString, minusString
from lib.drop import drop

DROPS = {
	'akasha': ['CoronationRing', 'LinegaeRing', 'IntricacyRing',
				'ChampionMerit', 'SupremeMerit', 'LegendaryMerit',
				'WeaponPlusMark', 'WeaponPlusMark2', 'WeaponPlusMark3',
				'HollowKey', 'SilverCentrum', 'GoldBrick'],
	'grandorder': ['CoronationRing', 'LinegaeRing', 'IntricacyRing',
					'ChampionMerit2', 'SupremeMerit2', 'LegendaryMerit',
					'VerdantAzurite', 'SilverCentrum', 'GoldBrick'],
	'probaha': ['CoronationRing', 'LinegaeRing', 'IntricacyRing', 'GoldBrick']
}


class boss:
	"""
	@ parent: the frame that should be located on
	@ name: name of the boss raid
	@ title: name of the boss raid in JP
	############################################
	@ parent: frame
	@ name: string, name of boss
	@ title: string, title of boss, in JP
	@ drops: array of drop classes, in boss's blue chest
	@ title_label: string, title shown on frame
	@ count_label: string, count of total blue chests
	@ total: string, total number of boss raids
	@ cur: string, current number of boss raids
	"""
	def __init__(self, parent, name, title):
		self.parent = parent
		self.name = name
		self.title = title
		self.drops = []
		self.title_label = tk.Label(self.parent, text=self.title, font=("Arial", 16))


		image = Image.open("img/"+self.name+"/"+self.name+".jpg")
		photo = ImageTk.PhotoImage(image)
		self.title_label.grid(row=0, column=1)

		# boss icon
		pic = tk.Label(self.parent, image=photo)
		pic.image = photo
		pic.grid(row=1, column=1)

		# read value from user file
		file = open('usr/'+self.name+'.txt', 'r')
		total_counts = file.readline().rstrip().split(',')
		cur_counts = file.readline().rstrip().split(',')

		self.total = total_counts[0]
		self.cur = cur_counts[0]
		self.count_label = tk.Label(self.parent, text=self.paint(), font=("Arial", 18))
		self.count_label.grid(row=1, column=2)

		for i in range(1, len(total_counts)):
			j = i-1
			drop_name = DROPS[self.name][j]
			item_drop = drop(self.parent, drop_name, self, 2+2*(j//3), j%3, total_counts[i], cur_counts[i])
			self.drops.append(item_drop)
		file.close()

		b = tk.Button(parent, text='Reset', fg='Red', font=('Arial', 12), command=self.reset)
		b.grid(row=10, column=1)

	def reset(self, event=None):
		for d in self.drops:
			d.cur_count = '0'
			d.label['text'] = d.paint()
		self.cur = '0'
		self.count_label['text'] = self.paint()

	def paint(self):
		return self.total+'('+self.cur+')'

	# write new information onto the file
	def update(self):
		file = open('usr/'+self.name+'.txt', 'w')
		total_line = [self.total]
		cur_line = [self.cur]
		for d in self.drops:
			total_line.append(d.total_count)
			cur_line.append(d.cur_count)
		file.write(','.join(total_line)+'\n')
		file.write(','.join(cur_line)+'\n')
		file.close()
