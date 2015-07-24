class card:
	def __init__(self, rank, suit):
		self.rank = rank 
		self.suit = suit
	def getRank(self):
		return self.rank
	def getSuit(self):
		return self.suit
	def BJValue(self):
		if self.rank == 1:
			return 1
		elif self.rank == 11 | self.rank == 12 | self.rank == 13:
			return 10
		else:
			return 0
	def __str__(self):
		name = ''
		if self.rank == 1:
			name = name + 'Ace'
		elif self.rank == 2:
			name = name + 'Two'
		elif self.rank == 3:
			name = name + 'Three'
		elif self.rank == 4:
			name = name + 'Four'
		elif self.rank == 5:
			name = name + 'Five'
		elif self.rank == 6:
			name = name + 'Six'
		elif self.rank == 7:
			name = name + 'Seven'
		elif self.rank == 8:
			name = name + 'Eight'
		elif self.rank == 9:
			name = name + 'Nine'
		elif self.rank == 10:
			name = name + 'Ten'
		elif self.rank == 11:
			name = name + 'Jack'
		elif self.rank == 12:
			name = name + 'Queen'
		elif self.rank == 13:
			name = name + 'King'
		else:
		    name = 'Wrong input'
		name = name + ' of ' 
		if self.suit=='d':
			name = name + 'diamonds'
		elif self.suit=='c':
			name = name + 'clubs'
		elif self.suit=='h':
			name = name + 'hearts'
		elif self.suit=='s':
			name = name + 'spades'
		else:
		    name = 'Wrong input'
		return name
		
		
		
c1 = card(13,'h')
print (c1)