from source.rules.Rule import Rule
#from source.detect_passive import Tagger

class Passive(Rule):
	#one should not be used as personal pronoun

	def __init__(self, word_id, tagger):
		self.sentence = ''
		self.start_index = -1

		self.error_message = 'Avoid using passive!'

		super(Passive, self).__init__(word_id, tagger)

		self.font_color = "#000000"
		self.background_color = "#ffff00"

	@staticmethod
	def get_alternatives():
		return 1

	def add_to_sentence(self, term):
		self.sentence += str(term)
		self.status += 1
		return 1

	def step(self, term):
		if self.status == 0:
			if term.symbol.tokenIndex == 0 or str(term) == '.' or str(term) == ':' or str(term) == '!' or str(term) == '?':
				self.start_index = term.symbol.tokenIndex
				return self.add_to_sentence(term)
		else:
			if term.symbol.tokenIndex == 0 or str(term) == '.' or str(term) == ':' or str(term) == '!' or str(term) == '?':
				self.sentence += str(term)

				self.sentence = self.sentence.replace("\n", " ")
				self.sentence = self.sentence.replace("\t", " ")

				'''
				lid = 0
				while lid < range(len(self.sentence)):
					if not self.sentence[lid] in " .\n\t!:?":
						break
					lid += 1
				self.sentence = self.sentence[lid:len(self.sentence)]
				'''

				if self.tagger.is_passive(self.sentence):
					tagger = None
					self.error_intervals.append((self.start_index, term.symbol.tokenIndex))
					return 2
				else:
					tagger = None
					return 0
			else:
				return self.add_to_sentence(term)