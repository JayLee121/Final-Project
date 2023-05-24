class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		# print(self.suit, self.rank) 錯了
		return f'{self.suit} {self.rank}'

card_1 = Card('Diamond', 12)
print(card_1)
print("Hello World")
