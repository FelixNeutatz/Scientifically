import abc
class Rule(object):
	__metaclass__ = abc.ABCMeta
	abstractstaticmethod = abc.abstractmethod

	def __init__(self, word_id, tagger):
		self.word_id = word_id
		self.error_intervals = []
		self.status = 0
		self.tagger = tagger
		self.font_color = "#ffffff"
		self.background_color = "#ff0000"

	@abstractstaticmethod
	def get_alternatives():
		raise NotImplementedError('users must define get_alternatives() to use this base class')

	def __str__(self):
		mystr = self.__class__.__name__ + \
				" word: " + str(self.word_id) + \
				"_status_" + str(self.status) + \
				": error intervals: "

		for tuple in self.error_intervals:
			mystr += "(" + str(tuple[0]) + "," + str(tuple[1]) + "), "

		return mystr

	@abc.abstractmethod
	def step(self, term):
		raise NotImplementedError('users must define step() to use this base class')