from source.rules.Rule import Rule

class Capitalize(Rule):
	#[words] space -> error
	words = [
				['figure', ' '],
				['chapter', ' '],
				['section', ' '],
				['table', ' '],
				['algorithm', ' '],
			]

	def __init__(self, word_id, tagger):
		self.start_id = -1
		self.end_id = -1

		self.error_message = 'Avoid it!'

		super(Capitalize, self).__init__(word_id, tagger)

	@staticmethod
	def get_alternatives():
		return len(Capitalize.words)

	def step(self, term):
		if self.status == 0:
			self.start_id = term.symbol.tokenIndex

		if self.status == len(Capitalize.words[self.word_id]):
			self.error_intervals.append((self.start_id, self.start_id))
			if term.symbol.type == 11:
				return 2  # found
			else:
				return 0

		if Capitalize.words[self.word_id][self.status] == str(term):
			self.status += 1
			if self.status == len(Capitalize.words[self.word_id]):
				self.end_id = term.symbol.tokenIndex
			return 1 #active
		else:
			return 0 #not present