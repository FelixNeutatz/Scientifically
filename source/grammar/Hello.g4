// Define a grammar called Hello
// java -Xmx500M -cp /home/felix/paperit/antlr-4.7.1-complete.jar org.antlr.v4.Tool -Dlanguage=Python2 Hello.g4
grammar Hello;
/* Lexical rules */

WORD : ~('\r' | '\n' | ':' | '.' | '?' | '!' | ',' | ' ' | '0' .. '9' | '(' | ')' )* ;
CITE : 'et al.' ;
COLON : ':' ;
DOT : '.' ;
QUESTION: '?' ;
EXCLAMATION: '!';
COMA : ',' ;
SPACE: ' ' ;
NEWLINE: '\n' ;
WS : [\r\t]+ -> skip ;

//DIGIT : ('0' .. '9') ;
NUMBER : ('0' .. '9')+ ('.' ('0' .. '9')+)? ;
PARO : '(' ;
PARC : ')' ;

/* Grammar rules */
rule_set : sentence* EOF ;

//number : DIGIT+ (DOT DIGIT+)? ;

sentence : (WORD | NUMBER | CITE | COMA | SPACE | NEWLINE | COLON | QUESTION | EXCLAMATION | DOT | PARO | PARC)
		 ;

