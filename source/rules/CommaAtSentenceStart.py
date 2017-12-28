from source.rules.Rule import Rule

class CommaAtSentenceStart(Rule):
	#[words] space -> error
	words = [
				['So'],
			 	['Then'],
				['Moreover'],
			 	['Furthermore'],
				['Additionally'],
				['Here'],
				['Finally'],
				['Hence'],
				['Thus'],
				['Therefore'],
				['In', ' ', 'this', ' ', 'thesis'],
				['In', ' ', 'this', ' ', 'paper'],
				['In', ' ', 'general'],
				['In',' ','summary']
			]

	def __init__(self, word_id, tagger):
		self.start_id = -1
		self.end_id = -1

		self.error_pattern = list(CommaAtSentenceStart.words[word_id])
		self.error_pattern.append(' ')

		self.error_message = 'There is a comma missing after '

		for word in CommaAtSentenceStart.words[word_id]:
			self.error_message += word

		super(CommaAtSentenceStart, self).__init__(word_id, tagger)

	@staticmethod
	def get_alternatives():
		return len(CommaAtSentenceStart.words)

	def step(self, term):
		if self.status == 0:
			self.start_id = term.symbol.tokenIndex

		if self.error_pattern[self.status] == str(term):
			self.status += 1
			if self.status == len(self.error_pattern):
				self.end_id = term.symbol.tokenIndex
				self.error_intervals.append((self.start_id, self.end_id))
				return 2 #found
			return 1 #active
		else:
			return 0 #not present