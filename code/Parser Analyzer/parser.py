import ply.yacc as yacc
from lexer import tokens
import lexer
import sys

VERBOSE = 1

def p_program(p): 
	'''pascal-program : PROGRAM ID program-heading SEMICOLON block DOT
						| PROGRAM ID SEMICOLON'''
	pass

def p_heading(p):
	'''program-heading : LPAREN identifier-list RPAREN'''
	pass


def p_identifierList(p):
	'''identifier-list : ID 
					   | identifier-list COMMA ID'''
	pass


def p_block(p):
	'''block : block1 
			 | label-declaration SEMICOLON block1'''
	pass



def p_block1(p):
	'''block1 : block2 
			  | constant-declaration SEMICOLON block2''' 
	pass

def p_block2(p):
	'''block2 : block3 
			  | type-declaration SEMICOLON block3''' 
	pass


def p_block3(p):
	'''block3 : block4 
			  | variable-declaration SEMICOLON block4''' 
	pass

def p_block4(p):
	'''block4 : block5 
			  | proc-and-func-declaration SEMICOLON block5''' 
	pass

def p_block5(p):
	'''block5 : BEGIN statement-list END''' 
	pass

def p_labelDeclaration(p):
	'''label-declaration : label INTEGER 
						 | label-declaration COMMA  INTEGER''' 
	pass


def p_constantDeclaration(p):
	'''constant-declaration : CONST ID COMPARATION constant 
							| constant-declaration  SEMICOLON  ID COMPARATION constant''' 
	pass

def p_typeDeclaration(p):
	'''type-declaration : type ID COMPARATION type 
						| type-declaration SEMICOLON ID COMPARATION type '''
	pass

def p_variableDeclaration(p):
	'''variable-declaration : VAR variableid-list COLON type SEMICOLON
							| variable-declaration SEMICOLON variableid-list COLON type '''
	pass

def p_variableIdList(p):
	'''variableid-list : ID 
					   | variableid-list COMMA ID'''
	pass

def p_constant(p):
	'''constant : INTEGER 
				| REAL 
				| STRING 
				| constid  
				| PLUS constid'''
	pass
	
"""def p_type(p):
	'''type : simple-type 
			| structured-type 
			| typeid'''
	pass"""

def p_type(p):
	'''type : simple-type 
			| structured-type 
			| typeid 	
	        | INTEGER   
			| REAL 
			| STRING 
			| constid  
			| PLUS constid'''
	pass


def p_simpleType(p):
	'''simple-type : LPAREN identifier-list RPAREN 
				   | constant
				   | typeid'''
	pass

def p_structuredType(p):
	'''structured-type : ARRAY LBRACKET index-list RBRACKET OF type 
					   | RECORD field-list END 
					   | SET OF simple-type 
					   | FILE OF type 
					   | PACKED structured-type'''
	pass

def p_indexList(p):
	'''index-list : simple-type 
				  | index-list COMMA simple-type'''
	pass

def p_fieldList(p):
	'''field-list : fixed-part 
				  | fixed-part SEMICOLON variant-part 
				  | variant-part'''
	pass

def p_fixedPart(p):
	'''fixed-part : record-field 
				  | fixed-part SEMICOLON record-field'''
	pass

def p_recordField(p):
	'''record-field : empty 
					| fieldid-list COLON type'''
	pass

def p_fieldidList(p):
	'''fieldid-list : ID 
					| fieldid-list COMMA ID'''
	pass

def p_variantPart(p):
	'''variant-part : CASE tag-field OF variant-list'''
	pass

def p_tagField(p):
	'''tag-field : typeid 
				 | ID COLON typeid'''
	pass

def p_variantList(p):
	'''variant-list : variant 
					| variant-list SEMICOLON variant'''
	pass

def p_variant(p):
	'''variant : empty 
			   | case-label-list COLON LPAREN field-list RPAREN'''
	pass
 
def p_caseLabelList(p):
	'''case-label-list : constant 
					   | case-label-list COMMA constant'''
	pass

def p_procAndFuncDeclaration(p):
	'''proc-and-func-declaration : proc-or-func 
								 | proc-and-func-declaration SEMICOLON proc-or-func '''
	pass

def p_procOrFunc(p):
	'''proc-or-func : PROCEDURE ID parameters SEMICOLON block-or-forward
		 			| FUNCTION  ID parameters COLON typeid SEMICOLON block-or-forward '''
	pass

def p_blockOrFordward(p):
	'''block-or-forward : block 
						| FORWARD'''
	pass

def p_parameters(p):
	'''parameters : LPAREN formal-parameter-list RPAREN'''
	pass

def p_formalParameterList(p):
	'''formal-parameter-list : formal-parameter-section
		 	 				 | formal-parameter-list SEMICOLON formal-parameter-section'''
	pass

def p_formalParameterSection(p):
	'''formal-parameter-section : parameterid-list COLON typeid 
							    | VAR parameterid-list COLON typeid 
								| PROCEDURE ID parameters 
								| FUNCTION ID parameters COLON typeid'''	
	pass

def p_parameteridList(p):
	'''parameterid-list : ID 
					    | parameterid-list COMMA ID'''
	pass

def p_statementList(p):
	'''statement-list : statement 
					  | statement-list SEMICOLON statement'''
	pass

def p_statement(p): 
   '''statement : empty 
   				| variable EQUAL expression 
   				| BEGIN statement-list END  
   				| IF expression THEN statement 
   				| IF expression THEN statement ELSE statement  
   				| CASE expression OF case-list END  
   				| WHILE expression DO statement  
  				| REPEAT statement-list UNTIL expression  
   				| FOR varid EQUAL for-list DO statement  
   				| procid  
   				| procid LPAREN expression-list RPAREN  
   				| GOTO label 
   				| WITH record-variable-list DO statement  
   				| label COLON statement'''	
   pass

def p_variable(p):
   '''variable  : ID  
			    | variable LBRACKET subscript-list RBRACKET  
			    | variable COMMA fieldid  
			    | variable'''
   pass

def p_subscriptlist(p):
	'''subscript-list : expression  
    				  |	subscript-list COMMA expression'''
	pass

def p_caselist(p):  
   '''case-list : case-label-list COLON statement  
   				| case-list SEMICOLON case-label-list COLON statement'''
   pass

def p_forlist(p): 
	'''for-list : expression TO expression  
    			| expression DOWNTO expression'''
	pass

def p_expressionlist(p):
	'''expression-list : expression  
    				   | expression-list COMMA expression'''
	pass
	
def p_label(P):  
   '''label : INTEGER'''
   pass

def p_recordvariablelist(p):
	'''record-variable-list : variable  
    						| record-variable-list COMMA variable''' 
	pass


def p_expression(p):
   '''expression : expression relational-op additive-expression 
   				 | additive-expression''' 
   pass

def p_relationalop(p):
   '''relational-op : LESS
					| LESSEQUAL  
					| EQUAL  
					| DEQUAL  
					| GREATEREQUAL  
					| GREATER''' 
   pass
	
def p_additiveExpression(P): 
   '''additive-expression : additive-expression additive-op multiplicative-expression 
   						  | multiplicative-expression''' 
   pass

def p_additiveop(p): 
   '''additive-op : PLUS  
   				  |	MINUS  
				  |	OR'''
   pass

def p_multiplicativeexpression(p): 
   '''multiplicative-expression : multiplicative-expression multiplicative-op unary-expression 
   								| unary-expression'''
   pass
   
def p_multiplicative_op(p): 
   '''multiplicative-op : TIMES  
   						| DIVIDE  
					    | DIV  
						| MOD  
						| AND  
						| IN'''
   pass

def p_unaryExpression(P): 
   '''unary-expression : unary-op unary-expression 
   					   | primary-expression'''  
   pass

def p_unaryop(p):  
	'''unary-op : PLUS 
				| MINUS 
				| NOT'''	
	pass

def p_primaryexpression(p):  
   '''primary-expression : variable 
						 | INTEGER
						 | REAL
						 | STRING 
						 | NIL
						 | funcid LPAREN expression-list RPAREN 
						 | LBRACKET element-list RBRACKET 
						 | LPAREN expression RPAREN'''
   pass

def p_elementlist(p):  
   '''element-list : empty 
				   | element 
				   | element-list COMMA element'''
   pass

def p_element(p):  
   '''element : expression 
   			  | expression DOT DOT DOT expression'''
   pass

def p_constid(p):  
   '''constid : ID'''
   pass

def p_typeid(p):
	'''typeid : ID'''
	pass

def p_funcid(p):
	'''funcid : ID'''
	pass 

def p_procid(p):
	'''procid : ID'''
	pass

def p_fieldid(p):
	'''fieldid : ID''' 
	pass

def p_varid(p):
	'''varid : ID'''
	pass


def p_empty(p):
	'''empty : '''
	pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(lexerPascal.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.pas'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informa que Tu parser reconocio correctamente todo")
	#input() 