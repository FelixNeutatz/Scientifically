import sys
import webbrowser

import numpy as np
from antlr4 import *

from source.grammar.HelloLexer import HelloLexer
from source.grammar.HelloListener import HelloListener
from source.grammar.HelloParser import HelloParser
from source.passive.detect_passive import Tagger
from source.rules.AvoidPhrase import AvoidPhrase
from source.rules.AvoidPhraseMaybe import AvoidPhraseMaybe
from source.rules.Capitalize import Capitalize
from source.rules.CommaAtSentenceStart import CommaAtSentenceStart
from source.rules.OneAsPRP import OneAsPRP
from source.rules.Passive import Passive
from source.rules.MultiChar import MultiChar


class HelloPrintListener(HelloListener):

	def __init__(self, show_in_browser=True, check_passive=False):
		self.show_in_browser = show_in_browser

		self.rules = [CommaAtSentenceStart, OneAsPRP, AvoidPhrase, AvoidPhraseMaybe, Capitalize, MultiChar]
		if check_passive:
			self.rules.append(Passive)

		super(HelloPrintListener, self).__init__()

	def to_html(self, mystring):
		return str(mystring).replace('\n', '<br>').replace(' ', '&nbsp;')

	def enterRule_set(self, ctx):

		tagger = Tagger()

		active_rules = {}
		found_errors = []
		active_counter = 0
		for child_new in ctx.getChildren():
			if child_new.getChildCount() >= 1:
				for c_new in child_new.getChildren():
					to_be_deleted = []
					for key, r in active_rules.iteritems():
						state = r.step(c_new)
						if state != 1:
							to_be_deleted.append(key)
						if state == 2:
							found_errors.append(r)

					#print "found: " + str(found_errors)

					for i in to_be_deleted:
						del active_rules[i]

					for class_rule in self.rules:
						for alternative in range(class_rule.get_alternatives()):
							rule = class_rule(alternative, tagger)
							state = rule.step(c_new)

							if state == 1:
								active_rules[active_counter] = rule
								active_counter += 1
							if state == 2:
								found_errors.append(rule)
								#print "active: " + str(active_counter)

						#print(str(c) + " "+ str(c.symbol.type))


		all_error_intervals = []
		pointer_to_rules = []
		for e in found_errors:
			for interval in e.error_intervals:
				all_error_intervals.append(interval)
				pointer_to_rules.append(e)

		all_error_intervals_sorted = sorted(all_error_intervals, key=lambda tup: tup[0])

		#print sorted_by_first

		print "test:" + str(all_error_intervals)
		if len(all_error_intervals) > 0:
			ids = np.argsort(all_error_intervals, axis=0)[:,0]


		print all_error_intervals_sorted

		html = ""

		html2 = ""

		for child_new in ctx.getChildren():
			#print(type(child))
			if child_new.getChildCount() >= 1:
				for c_new in child_new.getChildren():
					html2 += str(c_new)

					for error_counter in range(len(all_error_intervals_sorted)):
						if c_new.symbol.tokenIndex == all_error_intervals_sorted[error_counter][0]:
							html += '<p style="display:inline;cursor:Pointer; color: '+ pointer_to_rules[ids[error_counter]].font_color  +'; background-color: '+ pointer_to_rules[ids[error_counter]].background_color  +'" title="' + pointer_to_rules[ids[error_counter]].error_message + '"> '
							printed = True

					html += self.to_html(c_new)

					for error_counter in range(len(all_error_intervals_sorted)):
						if c_new.symbol.tokenIndex == all_error_intervals_sorted[error_counter][1]:
							html += '</p>'
							error_counter += 1


		log_errors = ""
		for ferror in found_errors:
			log_errors += ferror.__str__()

		print"LOG: errors: " + log_errors

		html_file = open('/tmp/scientifically.html', "w")
		html_file.write(html)
		html_file.close()

		log_file = open('/tmp/log.log', "w")
		log_file.write(log_errors)
		log_file.close()

		if self.show_in_browser:
			webbrowser.open('/tmp/scientifically.html')

		return found_errors


def run(text_file):
	input = FileStream(text_file)
	lexer = HelloLexer(input)
	stream = CommonTokenStream(lexer)
	parser = HelloParser(stream)
	tree = parser.rule_set()
	printer = HelloPrintListener()
	walker = ParseTreeWalker()
	walker.walk(printer, tree)

def main(argv):
	text_file = '/home/felix/paperit/pdf/test.txt'
	run(text_file)

if __name__ == '__main__':
	main(sys.argv)
