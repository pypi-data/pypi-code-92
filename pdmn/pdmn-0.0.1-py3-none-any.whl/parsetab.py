
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSHASHTAGABS ABS COMMA COMPARE DIVIDE DOT EQUALS HASHTAG ID LACC LBRACK LPAREN LQUOTE MAX MAX MIN MIN MINUS NO NO NOT NOT NUMBER PERCENT PLUS RACC RBRACK RPAREN RQUOTE STRAIGHTQUOTE TIMES UNTIL YES YESreturn : statementstatement : expression EQUALS YESstatement : expression EQUALS NOstatement : expression EQUALS MINUS\n                     | expression EQUALS statement : expression EQUALS NOT LPAREN expression RPARENstatement : expression EQUALS NOT LPAREN list RPARENstatement : expression EQUALS liststatement : expression EQUALS expressionstatement : expression COMPARE expression\n        statement : expression EQUALS lbound expression UNTIL expression rbound\n                  | expression EQUALS lbound expression COMMA expression rbound\n        \n        statement : expression EQUALS LPAREN expression UNTIL expression RPAREN\n        \n        statement : expression EQUALS LPAREN expression UNTIL expression RBRACK\n        \n        statement : expression EQUALS NOT LPAREN lbound expression COMMA         expression rbound RPAREN\n        list : expression COMMA expression\n                | list COMMA expressionexpression : ABS expression\n        expression : LQUOTE expression RQUOTE\n                   | STRAIGHTQUOTE expression STRAIGHTQUOTE\n        \n        expression : HASHTAG expression\n        \n        expression : expression PLUS expression\n                   | expression MINUS expression\n                   | expression TIMES expression\n                   | expression DIVIDE DIVIDE expression\n                   | expression DIVIDE expression\n                   | expression PERCENT expression\n        expression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENlbound : LPAREN\n                  | LBRACK\n                  | RBRACKrbound : RPAREN\n                  | RBRACK\n                  | LBRACKexpression : NUMBERexpression : NUMBER DOT NUMBERexpression : ID'
    
_lr_action_items = {'ABS':([0,4,5,6,7,8,9,12,13,14,15,16,17,18,29,31,33,34,35,41,47,48,50,55,57,58,60,61,68,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-32,-31,6,6,6,6,6,6,6,6,6,6,]),'LQUOTE':([0,4,5,6,7,8,9,12,13,14,15,16,17,18,29,31,33,34,35,41,47,48,50,55,57,58,60,61,68,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-32,-31,7,7,7,7,7,7,7,7,7,7,]),'STRAIGHTQUOTE':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,24,29,31,33,34,35,36,38,39,40,41,42,43,44,45,46,47,48,50,52,55,57,58,60,61,68,],[8,8,8,8,8,8,8,-36,-38,8,8,8,8,8,8,8,-28,-18,45,-21,8,8,8,-32,-31,-23,-22,-24,-26,8,-27,-29,-19,-20,-37,8,8,8,-25,8,8,8,8,8,8,]),'HASHTAG':([0,4,5,6,7,8,9,12,13,14,15,16,17,18,29,31,33,34,35,41,47,48,50,55,57,58,60,61,68,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-32,-31,9,9,9,9,9,9,9,9,9,9,]),'MINUS':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,29,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,59,60,61,64,65,66,67,68,76,],[4,13,4,4,4,4,4,4,-36,-38,29,4,4,4,4,4,4,-28,13,13,13,13,-21,13,4,4,4,-32,-31,-23,13,-22,-24,-26,4,13,-29,-19,-20,-37,4,4,13,4,13,-25,13,13,4,4,4,13,4,4,13,13,13,13,4,13,]),'LPAREN':([0,4,5,6,7,8,9,12,13,14,15,16,17,18,29,30,31,33,34,35,41,47,48,50,55,57,58,60,61,68,],[5,5,5,5,5,5,5,31,5,5,5,5,5,5,5,48,5,5,-32,-31,5,5,55,5,5,5,5,5,5,5,]),'NUMBER':([0,4,5,6,7,8,9,12,13,14,15,16,17,18,25,29,31,33,34,35,41,47,48,50,55,57,58,60,61,68,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,46,10,10,10,-32,-31,10,10,10,10,10,10,10,10,10,10,]),'ID':([0,4,5,6,7,8,9,12,13,14,15,16,17,18,29,31,33,34,35,41,47,48,50,55,57,58,60,61,68,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-32,-31,11,11,11,11,11,11,11,11,11,11,]),'$end':([1,2,10,11,12,19,21,24,26,27,28,29,32,36,37,38,39,40,42,43,44,45,46,52,53,59,62,63,69,70,71,72,73,74,75,78,],[0,-1,-36,-38,-5,-28,-18,-21,-9,-2,-3,-4,-8,-23,-10,-22,-24,-26,-27,-29,-19,-20,-37,-25,-16,-17,-6,-7,-13,-14,-11,-33,-34,-35,-12,-15,]),'EQUALS':([3,10,11,19,21,24,36,38,39,40,42,43,44,45,46,52,],[12,-36,-38,-28,-18,-21,-23,-22,-24,-26,-27,-29,-19,-20,-37,-25,]),'COMPARE':([3,10,11,19,21,24,36,38,39,40,42,43,44,45,46,52,],[14,-36,-38,-28,-18,-21,-23,-22,-24,-26,-27,-29,-19,-20,-37,-25,]),'PLUS':([3,10,11,19,20,21,22,23,24,26,36,37,38,39,40,42,43,44,45,46,49,51,52,53,54,59,64,65,66,67,76,],[15,-36,-38,-28,15,15,15,15,-21,15,-23,15,-22,-24,-26,15,-29,-19,-20,-37,15,15,-25,15,15,15,15,15,15,15,15,]),'TIMES':([3,10,11,19,20,21,22,23,24,26,36,37,38,39,40,42,43,44,45,46,49,51,52,53,54,59,64,65,66,67,76,],[16,-36,-38,-28,16,16,16,16,-21,16,16,16,16,-24,-26,16,-29,-19,-20,-37,16,16,-25,16,16,16,16,16,16,16,16,]),'DIVIDE':([3,10,11,17,19,20,21,22,23,24,26,36,37,38,39,40,42,43,44,45,46,49,51,52,53,54,59,64,65,66,67,76,],[17,-36,-38,41,-28,17,17,17,17,-21,17,17,17,17,-24,-26,17,-29,-19,-20,-37,17,17,-25,17,17,17,17,17,17,17,17,]),'PERCENT':([3,10,11,19,20,21,22,23,24,26,36,37,38,39,40,42,43,44,45,46,49,51,52,53,54,59,64,65,66,67,76,],[18,-36,-38,-28,18,18,18,18,-21,18,-23,18,-22,-24,-26,18,-29,-19,-20,-37,18,18,-25,18,18,18,18,18,18,18,18,]),'RPAREN':([10,11,19,20,21,24,36,38,39,40,42,43,44,45,46,49,52,53,54,56,59,65,66,67,72,73,74,76,77,],[-36,-38,-28,43,-18,-21,-23,-22,-24,-26,-27,-29,-19,-20,-37,43,-25,-16,62,63,-17,69,72,72,-33,-34,-35,72,78,]),'RQUOTE':([10,11,19,21,22,24,36,38,39,40,42,43,44,45,46,52,],[-36,-38,-28,-18,44,-21,-23,-22,-24,-26,-27,-29,-19,-20,-37,-25,]),'COMMA':([10,11,19,21,24,26,32,36,38,39,40,42,43,44,45,46,51,52,53,54,56,59,64,],[-36,-38,-28,-18,-21,47,50,-23,-22,-24,-26,-27,-29,-19,-20,-37,61,-25,-16,47,50,-17,68,]),'UNTIL':([10,11,19,21,24,36,38,39,40,42,43,44,45,46,49,51,52,],[-36,-38,-28,-18,-21,-23,-22,-24,-26,-27,-29,-19,-20,-37,58,60,-25,]),'RBRACK':([10,11,12,19,21,24,36,38,39,40,42,43,44,45,46,48,52,65,66,67,76,],[-36,-38,34,-28,-18,-21,-23,-22,-24,-26,-27,-29,-19,-20,-37,34,-25,70,73,73,73,]),'LBRACK':([10,11,12,19,21,24,36,38,39,40,42,43,44,45,46,48,52,66,67,76,],[-36,-38,35,-28,-18,-21,-23,-22,-24,-26,-27,-29,-19,-20,-37,35,-25,74,74,74,]),'DOT':([10,],[25,]),'YES':([12,],[27,]),'NO':([12,],[28,]),'NOT':([12,],[30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'return':([0,],[1,]),'statement':([0,],[2,]),'expression':([0,4,5,6,7,8,9,12,13,14,15,16,17,18,29,31,33,41,47,48,50,55,57,58,60,61,68,],[3,19,20,21,22,23,24,26,36,37,38,39,40,42,19,49,51,52,53,54,59,20,64,65,66,67,76,]),'list':([12,48,],[32,56,]),'lbound':([12,48,],[33,57,]),'rbound':([66,67,76,],[71,75,77,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> return","S'",1,None,None,None),
  ('return -> statement','return',1,'p_returnval','idply.py',150),
  ('statement -> expression EQUALS YES','statement',3,'p_yes','idply.py',156),
  ('statement -> expression EQUALS NO','statement',3,'p_no','idply.py',160),
  ('statement -> expression EQUALS MINUS','statement',3,'p_dontcare','idply.py',165),
  ('statement -> expression EQUALS','statement',2,'p_dontcare','idply.py',166),
  ('statement -> expression EQUALS NOT LPAREN expression RPAREN','statement',6,'p_eqnotlist','idply.py',169),
  ('statement -> expression EQUALS NOT LPAREN list RPAREN','statement',6,'p_eqnot','idply.py',173),
  ('statement -> expression EQUALS list','statement',3,'p_eqlist','idply.py',178),
  ('statement -> expression EQUALS expression','statement',3,'p_equals','idply.py',183),
  ('statement -> expression COMPARE expression','statement',3,'p_compare','idply.py',187),
  ('statement -> expression EQUALS lbound expression UNTIL expression rbound','statement',7,'p_range','idply.py',192),
  ('statement -> expression EQUALS lbound expression COMMA expression rbound','statement',7,'p_range','idply.py',193),
  ('statement -> expression EQUALS LPAREN expression UNTIL expression RPAREN','statement',7,'p_prange','idply.py',201),
  ('statement -> expression EQUALS LPAREN expression UNTIL expression RBRACK','statement',7,'p_rrange','idply.py',210),
  ('statement -> expression EQUALS NOT LPAREN lbound expression COMMA expression rbound RPAREN','statement',10,'p_nrange','idply.py',218),
  ('list -> expression COMMA expression','list',3,'p_list','idply.py',229),
  ('list -> list COMMA expression','list',3,'p_list','idply.py',230),
  ('expression -> ABS expression','expression',2,'p_expression_abs','idply.py',238),
  ('expression -> LQUOTE expression RQUOTE','expression',3,'p_quotes','idply.py',243),
  ('expression -> STRAIGHTQUOTE expression STRAIGHTQUOTE','expression',3,'p_quotes','idply.py',244),
  ('expression -> HASHTAG expression','expression',2,'p_domain_size','idply.py',257),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','idply.py',267),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','idply.py',268),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','idply.py',269),
  ('expression -> expression DIVIDE DIVIDE expression','expression',4,'p_expression_binop','idply.py',270),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','idply.py',271),
  ('expression -> expression PERCENT expression','expression',3,'p_expression_binop','idply.py',272),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','idply.py',288),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','idply.py',292),
  ('lbound -> LPAREN','lbound',1,'p_lbound','idply.py',296),
  ('lbound -> LBRACK','lbound',1,'p_lbound','idply.py',297),
  ('lbound -> RBRACK','lbound',1,'p_lbound','idply.py',298),
  ('rbound -> RPAREN','rbound',1,'p_rbound','idply.py',302),
  ('rbound -> RBRACK','rbound',1,'p_rbound','idply.py',303),
  ('rbound -> LBRACK','rbound',1,'p_rbound','idply.py',304),
  ('expression -> NUMBER','expression',1,'p_expression_number','idply.py',308),
  ('expression -> NUMBER DOT NUMBER','expression',3,'p_dot','idply.py',312),
  ('expression -> ID','expression',1,'p_expression_name','idply.py',316),
]
