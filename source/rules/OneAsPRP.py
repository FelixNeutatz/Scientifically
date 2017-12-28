from pycorenlp import StanfordCoreNLP
from source.rules.Rule import Rule
import json

class OneAsPRP(Rule):
	#one should not be used as personal pronoun

	def __init__(self, word_id, tagger):
		self.sentence = ''
		self.contains_one = []

		self.nlp = StanfordCoreNLP('http://localhost:9000')

		self.error_message = 'The word _one_ should not be used as a personal pronoun. Use _we_ instead. In the worst case, use passive.'

		super(OneAsPRP, self).__init__(word_id, tagger)

	@staticmethod
	def get_alternatives():
		return 1

	def add_to_sentence(self, term):
		self.sentence += str(term)
		self.status += 1
		if str(term).upper() == 'ONE':
			self.contains_one.append(term.symbol.tokenIndex)
		return 1

	def step(self, term):
		if self.status == 0:
			if term.symbol.tokenIndex == 0 or str(term) == '.' or str(term) == ':' or str(term) == '!' or str(term) == '?':
				return self.add_to_sentence(term)
		else:
			if term.symbol.tokenIndex == 0 or str(term) == '.' or str(term) == ':' or str(term) == '!' or str(term) == '?':
				self.sentence += str(term)

				if len(self.contains_one) == 0:
					return 0

				self.sentence = self.sentence.replace("\n", " ")
				self.sentence = self.sentence.replace("\t", " ")

				l = 0
				while l < range(len(self.sentence)):
					if not self.sentence[l] in " .\n\t!:?":
						break
					l += 1
				self.sentence = self.sentence[l:len(self.sentence)]

				#search for one
				output = self.nlp.annotate(self.sentence,
					properties={
						'annotators': 'parse',
						'outputFormat': 'json'
					}
					)

				print output

				tree = output['sentences'][0]['parse']

				from nltk.tree import Tree
				tr1 = str(tree)
				s1 = Tree.fromstring(tr1)
				s2 = s1.productions()

				print s2

				results = []
				negative_results = []
				for tree_runner in range(len(s2)):
					if "'One'" in str(s2[tree_runner]) or "'one'" in str(s2[tree_runner]):
						if tree_runner < len(s2) and 'VP ->' in str(s2[tree_runner + 1]):
							results.append(tree_runner)
						else:
							negative_results.append(tree_runner)

				print tree

				print negative_results

				print "negative: " + str(len(negative_results))
				print "positive: " + str(len(results))
				print "total: " + str(len(self.contains_one))
				print self.contains_one
				print self.sentence

				assert len(negative_results) + len(results) == len(self.contains_one), "size doesnt fit!"


				p = 0
				n = 0
				all = 0
				while all < len(self.contains_one):
					if n < len(negative_results) and p < len(results):
						if results[p] < negative_results[n]:
							self.error_intervals.append((self.contains_one[all], self.contains_one[all]))
							p += 1
						else:
							n += 1
					else:
						if n == len(negative_results):
							self.error_intervals.append((self.contains_one[all], self.contains_one[all]))
							p += 1
						else:
							break
					all += 1


				if len(self.error_intervals) > 0:
					return 2
				else:
					return 0
			else:
				return self.add_to_sentence(term)