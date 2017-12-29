# -*- coding: utf-8 -*-

import unittest

from antlr4 import *
from source.grammar.HelloLexer import HelloLexer
from source.Hello import HelloPrintListener
from source.grammar.HelloParser import HelloParser


class MyTest(unittest.TestCase):

    show_in_browser = False
    check_passive = False

    def infrastructure(self, input):
        input = InputStream(input)
        lexer = HelloLexer(input)
        stream = CommonTokenStream(lexer)
        parser = HelloParser(stream)
        tree = parser.rule_set()
        printer = HelloPrintListener(MyTest.show_in_browser, MyTest.check_passive)
        walker = ParseTreeWalker()
        walker.walk(printer, tree)

    def check(self, expected_log):
        file = open('/tmp/log.log', "r")
        log = file.read()
        file.close()
        assert log == expected_log, "Log does not show expected result"



if __name__ == '__main__':
    unittest.main()