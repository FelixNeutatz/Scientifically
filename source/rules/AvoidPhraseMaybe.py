from source.rules.Rule import Rule

class AvoidPhraseMaybe(Rule):
	#[words] space -> error
	words = [
				['also']
			]

	def __init__(self, word_id, tagger):
		self.start_id = -1
		self.end_id = -1

		self.error_message = 'Maybe remove it.'

		super(AvoidPhraseMaybe, self).__init__(word_id, tagger)

		self.font_color = "#000000"
		self.background_color = "#ff69b4"

	@staticmethod
	def get_alternatives():
		return len(AvoidPhraseMaybe.words)

	def step(self, term):
		if self.status == 0:
			self.start_id = term.symbol.tokenIndex

		if AvoidPhraseMaybe.words[self.word_id][self.status] == str(term):
			self.status += 1
			if self.status == len(AvoidPhraseMaybe.words[self.word_id]):
				self.end_id = term.symbol.tokenIndex
				self.error_intervals.append((self.start_id, self.end_id))
				return 2 #found
			return 1 #active
		else:
			return 0 #not present