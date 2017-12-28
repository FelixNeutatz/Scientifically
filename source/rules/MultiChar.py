from source.rules.Rule import Rule

class MultiChar(Rule):
	#[words] space -> error
	words = [
				[' ']
			]

	def __init__(self, word_id, tagger):
		self.start_id = -1

		self.error_message = 'Too many'

		super(MultiChar, self).__init__(word_id, tagger)

	@staticmethod
	def get_alternatives():
		return len(MultiChar.words)

	def step(self, term):
		if self.status == 0:
			self.start_id = term.symbol.tokenIndex

		if not MultiChar.words[self.word_id][0] == str(term) and self.status > 1:
			self.error_intervals.append((self.start_id, term.symbol.tokenIndex - 1))
			return 2  # found

		if MultiChar.words[self.word_id][0] == str(term):
			self.status += 1
			return 1 #active
		else:
			return 0 #not present