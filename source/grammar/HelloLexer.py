# Generated from Hello.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\17P\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\3\2\7\2\37\n\2\f\2\16\2\"\13\2\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write(u"\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13:\n\13\r\13\16\13;\3")
        buf.write(u"\13\3\13\3\f\6\fA\n\f\r\f\16\fB\3\f\3\f\6\fG\n\f\r\f")
        buf.write(u"\16\fH\5\fK\n\f\3\r\3\r\3\16\3\16\2\2\17\3\3\5\4\7\5")
        buf.write(u"\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3")
        buf.write(u"\2\4\n\2\f\f\17\17\"#*+..\60\60\62<AA\4\2\13\13\17\17")
        buf.write(u"\2T\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write(u"\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write(u"\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write(u"\3\2\2\2\3 \3\2\2\2\5#\3\2\2\2\7*\3\2\2\2\t,\3\2\2\2")
        buf.write(u"\13.\3\2\2\2\r\60\3\2\2\2\17\62\3\2\2\2\21\64\3\2\2\2")
        buf.write(u"\23\66\3\2\2\2\259\3\2\2\2\27@\3\2\2\2\31L\3\2\2\2\33")
        buf.write(u"N\3\2\2\2\35\37\n\2\2\2\36\35\3\2\2\2\37\"\3\2\2\2 \36")
        buf.write(u"\3\2\2\2 !\3\2\2\2!\4\3\2\2\2\" \3\2\2\2#$\7g\2\2$%\7")
        buf.write(u"v\2\2%&\7\"\2\2&\'\7c\2\2\'(\7n\2\2()\7\60\2\2)\6\3\2")
        buf.write(u"\2\2*+\7<\2\2+\b\3\2\2\2,-\7\60\2\2-\n\3\2\2\2./\7A\2")
        buf.write(u"\2/\f\3\2\2\2\60\61\7#\2\2\61\16\3\2\2\2\62\63\7.\2\2")
        buf.write(u"\63\20\3\2\2\2\64\65\7\"\2\2\65\22\3\2\2\2\66\67\7\f")
        buf.write(u"\2\2\67\24\3\2\2\28:\t\3\2\298\3\2\2\2:;\3\2\2\2;9\3")
        buf.write(u"\2\2\2;<\3\2\2\2<=\3\2\2\2=>\b\13\2\2>\26\3\2\2\2?A\4")
        buf.write(u"\62;\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2CJ\3\2")
        buf.write(u"\2\2DF\7\60\2\2EG\4\62;\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2")
        buf.write(u"\2HI\3\2\2\2IK\3\2\2\2JD\3\2\2\2JK\3\2\2\2K\30\3\2\2")
        buf.write(u"\2LM\7*\2\2M\32\3\2\2\2NO\7+\2\2O\34\3\2\2\2\b\2 ;BH")
        buf.write(u"J\3\b\2\2")
        return buf.getvalue()


class HelloLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WORD = 1
    CITE = 2
    COLON = 3
    DOT = 4
    QUESTION = 5
    EXCLAMATION = 6
    COMA = 7
    SPACE = 8
    NEWLINE = 9
    WS = 10
    NUMBER = 11
    PARO = 12
    PARC = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'et al.'", u"':'", u"'.'", u"'?'", u"'!'", u"','", u"' '", 
            u"'\n'", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>",
            u"WORD", u"CITE", u"COLON", u"DOT", u"QUESTION", u"EXCLAMATION", 
            u"COMA", u"SPACE", u"NEWLINE", u"WS", u"NUMBER", u"PARO", u"PARC" ]

    ruleNames = [ u"WORD", u"CITE", u"COLON", u"DOT", u"QUESTION", u"EXCLAMATION", 
                  u"COMA", u"SPACE", u"NEWLINE", u"WS", u"NUMBER", u"PARO", 
                  u"PARC" ]

    grammarFileName = u"Hello.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(HelloLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


