from source.rules.Rule import Rule

class AvoidPhrase(Rule):
	#[words] space -> error
	words = [
				['You'],
				['you'],
				['I'],
				#['('],
				#[')'],
				['a', ' ', 'number', ' ', 'of'], # several
				['obvious'], # was expected
				['makes', 'sense'], # can be expected
				['make', 'sense'],
				['clearly'],
				['In', ' ', 'this', ' ', 'section'],
				['in', ' ', 'the', ' ', 'history'],
				['In', ' ', 'the', ' ', 'history'],
				['!'],
				['question', ' ', 'is'], # expression
				['ask', ' ', 'ourselves'] # expression
			]

	def __init__(self, word_id, tagger):
		self.start_id = -1
		self.end_id = -1

		self.error_message = 'Avoid it!'

		super(AvoidPhrase, self).__init__(word_id, tagger)

	@staticmethod
	def get_alternatives():
		return len(AvoidPhrase.words)

	def step(self, term):
		if self.status == 0:
			self.start_id = term.symbol.tokenIndex

		if AvoidPhrase.words[self.word_id][self.status] == str(term):
			self.status += 1
			if self.status == len(AvoidPhrase.words[self.word_id]):
				self.end_id = term.symbol.tokenIndex
				self.error_intervals.append((self.start_id, self.end_id))
				return 2 #found
			return 1 #active
		else:
			return 0 #not present