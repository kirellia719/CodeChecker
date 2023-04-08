// PHAM HONG KHANH - 1913754
grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decl_list? EOF;
decl_list: decl decl_list | decl;
decl: vardecl | funcdecl | main_entry;

// VarDecl
vardecl: var_short | var_init;
var_short: idlist COLON var_type SEMICOLON;
var_init: midvar SEMICOLON;
midvar:
	ID COMMA midvar COMMA expr
	| ID COLON (var_type | AUTO) EQUAL expr;

main_entry: MAIN COLON FUNCTION VOID LP RP block_stmt;
funcdecl:
	ID COLON FUNCTION func_type LP param_list? RP (INHERIT ID)? block_stmt;

// ParamDecl
param_list: param COMMA param_list | param;
param: INHERIT? OUT? ID COLON var_type;

// Statement
block_stmt: LCB stmt_list? RCB;
stmt_list: stmt stmt_list | stmt;
stmt:
	vardecl
	| assign_stmt
	| return_stmt
	| if_stmt
	| for_stmt
	| while_stmt
	| do_while_stmt
	| break_stmt
	| continue_stmt
	| call_stmt
	| block_stmt;
assign_stmt: lhs EQUAL expr SEMICOLON;
lhs: ID | index_operator;
return_stmt: RETURN expr? SEMICOLON;
if_stmt: IF LP expr RP stmt else_stmt?;
else_stmt: ELSE stmt;
for_stmt: FOR LP scalar_var EQUAL init_expr COMMA condition_expr COMMA update_expr RP stmt;
scalar_var: ID;
init_expr: expr;
condition_expr: expr;
update_expr: expr;
while_stmt: WHILE LP expr RP stmt;
do_while_stmt: DO block_stmt WHILE LP expr RP SEMICOLON;
break_stmt: BREAK SEMICOLON;
continue_stmt: CONTINUE SEMICOLON;
call_stmt: func_call SEMICOLON;

func_call: ID LP expr_list? RP;

// Expression
expr_list: expr COMMA expr_list | expr;
expr: expr1;
expr1: expr2 DOUBLE_COLON expr2 | expr2;
expr2: expr3 relational expr3 | expr3;
relational:
	DOUBLE_EQUAL
	| NOT_EQUAL
	| LESS
	| LESS_EQUAL
	| GREATER
	| GREATER_EQUAL;

expr3: expr3 logical expr4 | expr4;
logical: AND | OR;

expr4: expr4 adding expr5 | expr5;
adding: ADD | SUB;

expr5: expr5 multiplying expr6 | expr6;
multiplying: MUL | DIV | MOD;

expr6: NOT expr6 | expr7;
expr7: SUB expr7 | expr8;
expr8: index_operator | expr_last;
index_operator: ID LSB expr_list RSB;
expr_last:
	ID
	| INTEGER_LIT
	| FLOAT_LIT
	| boolean_lit
	| STRING_LIT
	| func_call
	| array_lit
	| LP expr RP;
boolean_lit: TRUE | FALSE;


// Rest
idlist: ID COMMA idlist | ID;
var_type: atomic_type | array_type;
func_type: atomic_type | VOID | AUTO | array_type;
atomic_type: INTEGER | FLOAT | BOOLEAN | STRING;
array_type: ARRAY LSB int_list RSB OF atomic_type;
int_list: INTEGER_LIT COMMA int_list | INTEGER_LIT;
array_lit: LCB expr_list? RCB;

// COMENT
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
INLINE_COMMENT: '//' .*? ([\n] | EOF) -> skip;

// KEYWORD
MAIN: 'main';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
IF: 'if';
ELSE: 'else';
FOR: 'for';
FUNCTION: 'function';
WHILE: 'while';
DO: 'do';
OUT: 'out';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';
INTEGER: 'integer';
FLOAT: 'float';
BOOLEAN: 'boolean';
STRING: 'string';
VOID: 'void';
AUTO: 'auto';
TRUE: 'true';
FALSE: 'false';

// Operator
DOUBLE_EQUAL: '==';
NOT_EQUAL: '!=';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';
DOUBLE_COLON: '::';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
AND: '&&';
OR: '||';
EQUAL: '=';
NOT: '!';
LESS: '<';
GREATER: '>';
COLON: ':';
DOT: '.';
LP: '(';
// Left Parenthesis
RP: ')';
// Right Parenthesis
LSB: '[';
// Left Square Bracket
RSB: ']';
// Right Square Bracket
LCB: '{';
// Left Curly Bracket
RCB: '}';
// Right Curly Bracket
COMMA: ',';
SEMICOLON: ';';
DOUBLE_QUOTE: '"';

INTEGER_LIT:
	[0]
	| [1-9] ([_] [0-9] | [0-9])* {
				self.text = self.text.replace('_', '');
			};

fragment DECIMAL_PART: '.' [0-9]*;
fragment EXPONENT_PART: [Ee] [-+]? [0-9]+;
FLOAT_LIT:
	(
		INTEGER_LIT DECIMAL_PART EXPONENT_PART
		| INTEGER_LIT DECIMAL_PART
		| INTEGER_LIT EXPONENT_PART
		| DECIMAL_PART EXPONENT_PART
	) {
		self.text = self.text.replace('_', '');
	};

fragment LEGAL_CHARATER: ('\\' ([bfrnt] | '\\' | '\'' | '"'))
	| ~([\r\n] | '"' | '\\');

fragment ILLEGAL_CHARACTER: ('\\' ~([bfrnt] | '\\' | '\'' | '"'))
	| ([\r\n] | '"' | '\\');

STRING_LIT:
	DOUBLE_QUOTE LEGAL_CHARATER* DOUBLE_QUOTE {
	self.text = self.text[1:];
	self.text = self.text[:-1];
};

ID: [A-Za-z_] [a-zA-Z0-9_]*;

WS: [ \b\f\t\r\n]+ -> skip;
// skip spaces, tabs, newlines

ILLEGAL_ESCAPE:
	DOUBLE_QUOTE LEGAL_CHARATER* ILLEGAL_CHARACTER {
	raise IllegalEscape(self.text[1:]);
};
UNCLOSE_STRING:
	DOUBLE_QUOTE LEGAL_CHARATER* EOF {
	raise UncloseString(self.text[1:]);
};
ERROR_CHAR:
	.{
	raise ErrorToken(self.text);
};