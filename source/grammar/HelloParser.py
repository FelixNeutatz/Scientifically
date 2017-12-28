# Generated from Hello.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\17\21\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2")
        buf.write(u"\3\2\3\2\3\3\3\3\3\3\2\2\4\2\4\2\3\4\2\3\13\r\17\2\17")
        buf.write(u"\2\t\3\2\2\2\4\16\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\13")
        buf.write(u"\3\2\2\2\t\7\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13\t\3\2")
        buf.write(u"\2\2\f\r\7\2\2\3\r\3\3\2\2\2\16\17\t\2\2\2\17\5\3\2\2")
        buf.write(u"\2\3\t")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"'et al.'", u"':'", u"'.'", 
                     u"'?'", u"'!'", u"','", u"' '", u"'\n'", u"<INVALID>", 
                     u"<INVALID>", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>", u"WORD", u"CITE", u"COLON", u"DOT", 
                      u"QUESTION", u"EXCLAMATION", u"COMA", u"SPACE", u"NEWLINE", 
                      u"WS", u"NUMBER", u"PARO", u"PARC" ]

    RULE_rule_set = 0
    RULE_sentence = 1

    ruleNames =  [ u"rule_set", u"sentence" ]

    EOF = Token.EOF
    WORD=1
    CITE=2
    COLON=3
    DOT=4
    QUESTION=5
    EXCLAMATION=6
    COMA=7
    SPACE=8
    NEWLINE=9
    WS=10
    NUMBER=11
    PARO=12
    PARC=13

    def __init__(self, input, output=sys.stdout):
        super(HelloParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Rule_setContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(HelloParser.Rule_setContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HelloParser.EOF, 0)

        def sentence(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.SentenceContext)
            else:
                return self.getTypedRuleContext(HelloParser.SentenceContext,i)


        def getRuleIndex(self):
            return HelloParser.RULE_rule_set

        def enterRule(self, listener):
            if hasattr(listener, "enterRule_set"):
                listener.enterRule_set(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRule_set"):
                listener.exitRule_set(self)




    def rule_set(self):

        localctx = HelloParser.Rule_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_rule_set)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.WORD) | (1 << HelloParser.CITE) | (1 << HelloParser.COLON) | (1 << HelloParser.DOT) | (1 << HelloParser.QUESTION) | (1 << HelloParser.EXCLAMATION) | (1 << HelloParser.COMA) | (1 << HelloParser.SPACE) | (1 << HelloParser.NEWLINE) | (1 << HelloParser.NUMBER) | (1 << HelloParser.PARO) | (1 << HelloParser.PARC))) != 0):
                self.state = 4
                self.sentence()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(HelloParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SentenceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(HelloParser.SentenceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(HelloParser.WORD, 0)

        def NUMBER(self):
            return self.getToken(HelloParser.NUMBER, 0)

        def CITE(self):
            return self.getToken(HelloParser.CITE, 0)

        def COMA(self):
            return self.getToken(HelloParser.COMA, 0)

        def SPACE(self):
            return self.getToken(HelloParser.SPACE, 0)

        def NEWLINE(self):
            return self.getToken(HelloParser.NEWLINE, 0)

        def COLON(self):
            return self.getToken(HelloParser.COLON, 0)

        def QUESTION(self):
            return self.getToken(HelloParser.QUESTION, 0)

        def EXCLAMATION(self):
            return self.getToken(HelloParser.EXCLAMATION, 0)

        def DOT(self):
            return self.getToken(HelloParser.DOT, 0)

        def PARO(self):
            return self.getToken(HelloParser.PARO, 0)

        def PARC(self):
            return self.getToken(HelloParser.PARC, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_sentence

        def enterRule(self, listener):
            if hasattr(listener, "enterSentence"):
                listener.enterSentence(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSentence"):
                listener.exitSentence(self)




    def sentence(self):

        localctx = HelloParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.WORD) | (1 << HelloParser.CITE) | (1 << HelloParser.COLON) | (1 << HelloParser.DOT) | (1 << HelloParser.QUESTION) | (1 << HelloParser.EXCLAMATION) | (1 << HelloParser.COMA) | (1 << HelloParser.SPACE) | (1 << HelloParser.NEWLINE) | (1 << HelloParser.NUMBER) | (1 << HelloParser.PARO) | (1 << HelloParser.PARC))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





