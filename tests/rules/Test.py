# -*- coding: utf-8 -*-

import unittest

from tests.rules.MyTest import MyTest

class ViolationTest(MyTest):

    def test_so(self):
        self.infrastructure("So here we are.")
        expected = "CommaAtSentenceStart word: 0_status_2: error intervals: (0,1), "
        self.check(expected)

    def test_then(self):
        self.infrastructure("Hello. Then we are.")
        expected = "CommaAtSentenceStart word: 1_status_2: error intervals: (3,4), "
        self.check(expected)

    def test_insummary(self):
        self.infrastructure("In summary this is it.")
        expected = "CommaAtSentenceStart word: 13_status_4: error intervals: (0,3), "
        self.check(expected)

    def test_one1(self):
        self.infrastructure("The tuples that contain the selected cells, are given to the user one by one.")
        expected = ""
        self.check(expected)

    def test_one2(self):
        self.infrastructure("One is happy and one is sad.")
        expected = "OneAsPRP word: 0_status_13: error intervals: (0,0), (8,8), "
        self.check(expected)

    def test_one3(self):
        self.infrastructure(".  Based on the initial labels provided by the user, the system trains one error detection classier for each column of the data.")
        expected = "MultiChar word: 0_status_2: error intervals: (1,2), "
        self.check(expected)

    def test_one4(self):
        self.infrastructure("one commonly used hospital dataset for eval- uating data cleaning [7], [20], [1], one with ight scheduling data [7], and one address dataset [10].")
        expected = ""
        self.check(expected)

    def test_one5(self):
        self.infrastructure("Hospital is one of the most commonly used datasets to benchmark data cleaning algorithms [20], [1].")
        expected = ""
        self.check(expected)

    def test_one6(self):
        self.infrastructure("We consider any cell that participates in at least one violation to be erroneous [10].")
        expected = ""
        self.check(expected)

    def test_one7(self):
        self.infrastructure("For instance, one can extend our method to a multi-user setting or use a more stable sampling method.");
        expected = "OneAsPRP word: 0_status_36: error intervals: (5,5), "
        self.check(expected)

    def test_one8(self):
        self.infrastructure("One can further improve the feature representation of relational data.");
        expected = "OneAsPRP word: 0_status_19: error intervals: (0,0), "
        self.check(expected)

    def test_passive1(self):
        MyTest.check_passive = True
        self.infrastructure("Passive is used. We use active.")
        MyTest.check_passive = False
        expected = "Passive word: 0_status_5: error intervals: (0,5), "
        self.check(expected)

    def test_and(self):
        self.infrastructure("I want one apple, oranges and icecream.")

    def test_you(self):
        self.infrastructure("You are great.")
        expected = "AvoidPhrase word: 0_status_1: error intervals: (0,0), "
        self.check(expected)

    def test_also(self):
        self.infrastructure("It is also great.")
        expected = "AvoidPhraseMaybe word: 0_status_1: error intervals: (4,4), "
        self.check(expected)

    def test_break(self):
        self.infrastructure("The Feature\nExtractor counts all character sequences of length n occurring\nin a given column of the dataset. In the case of a unigram\nmodel (n = 1), the Feature Extractor counts the occurrences\nof single characters such as A, a, 1, ., and   for each\ncell in a given column. The Feature Extractor applies the\ncommon approach of the TF-IDF score to represent n-grams\nin a numerical representation [16].")

    def test_capital(self):
        self.infrastructure("section 4.1 is great")
        expected = "Capitalize word: 2_status_2: error intervals: (0,0), "
        self.check(expected)

    def test_capital2(self):
        self.infrastructure("This section is great")
        expected = ""
        self.check(expected)

    '''
    def test_parentheses(self):
        self.infrastructure("Furthermore, in the case that we use a depth-limited decision\ntree (maximum tree depth < number of n-gram features), this\nmodel is not able to deduce string length from the language\nmodel representation.")
        expected = "AvoidPhrase word: 3_status_1: error intervals: (23,23), AvoidPhrase word: 4_status_1: error intervals: (39,39), "
        self.check(expected)
    '''

    def test_multispaces(self):
        self.infrastructure("This is  now.")
        expected = "MultiChar word: 0_status_2: error intervals: (3,4), "
        self.check(expected)


if __name__ == '__main__':
    unittest.main()