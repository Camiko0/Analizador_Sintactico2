from lexer_rules import tokens
from expressions import *

def p_expression_plus(subexpr):
    'expression : expression expression PLUS'
    subexpr[0] = subexpr[1] + subexpr[2]
    
def p_expression_minus(subexpr):
    'expression : expression expression MINUS'
    subexpr[0] = subexpr[1] - subexpr[2]
    
def p_expression_times(subexpr):
    'expression : expression expression TIMES'
    subexpr[0] = subexpr[1] * subexpr[2]
    
def p_expression_divide(subexpr):
    'expression : expression expression DIVIDE'
    subexpr[0] = subexpr[1] / subexpr[2]

def p_expression_term(subexpr):
    'expression : term'
    subexpr[0] = subexpr[1]

def p_term_factor(subexpr):
    'term : factor'
    subexpr[0] = subexpr[1]

def p_factor_num(subexpr):
    'factor : NUMBER'
    subexpr[0] = subexpr[1]

def p_error(subexpr):
    raise Exception("Syntax error.")
