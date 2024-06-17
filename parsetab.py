
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftANDORleftEQNELTGTLEGEleft+-left*/rightUMINUSUNARY_NEGALEATORIO AND COMENTARIO CONCAT ENTRADA EQ ESCREVER FIM FOLD FUNCAO GE GT LE LT MAP NE NEG NUM OR SE SENAO SENAOSE STRING VAR_IDlista_declaracoes : declaracao\n                             | lista_declaracoes declaracaodeclaracao : declaracao_atribuicao\n                      | declaracao_expressao\n                      | declaracao_funcao\n                      | declaracao_se\n                      | declaracao_escrever\n                      | declaracao_comentariodeclaracao_atribuicao : VAR_ID '=' lista_expressoes ';'declaracao_atribuicao : atribuicao\n                                 | declaracao_atribuicao ',' atribuicao ';'atribuicao : VAR_ID '=' expressaolista_expressoes : lista_expressoes ',' expressao\n                            | expressaodeclaracao_expressao : expressao ';'expressao : expressao '+' expressao\n                     | expressao '-' expressao\n                     | expressao '*' expressao\n                     | expressao '/' expressaoexpressao : expressao AND expressao\n                     | expressao OR expressao\n                     | expressao EQ expressao\n                     | expressao NE expressao\n                     | expressao LT expressao\n                     | expressao LE expressao\n                     | expressao GT expressao\n                     | expressao GE expressaoexpressao : '(' expressao ')'expressao : '-' expressao %prec UMINUSexpressao : NUMexpressao : STRINGexpressao : VAR_IDexpressao : '[' lista_elementos  ']' lista_elementos : lista_elementos ',' expressao\n                           | expressao\n                           | vazioexpressao : MAP '(' VAR_ID ',' expressao ')'expressao : FOLD '(' VAR_ID ',' expressao ',' expressao ')'expressao : ENTRADA '(' ')'expressao : ALEATORIO '(' NUM ')'expressao : VAR_ID '(' lista_expressoes ')'declaracao_funcao : FUNCAO VAR_ID '(' lista_parametros_opcional ')' ':' bloco_funcao FIM\n                             | FUNCAO VAR_ID '(' lista_parametros_opcional ')' ',' ':' expressao ';'lista_parametros_opcional : lista_parametros\n                                     | vaziolista_parametros : lista_parametros ',' parametro\n                            | parametroparametro : VAR_IDparametro : NUMparametro : VAR_ID ':' VAR_IDparametro : '[' ']'expressao : '[' ']'declaracao_se : SE expressao ':' lista_declaracoes senao_opcional FIMsenao_opcional  : SENAO ':' lista_declaracoes\n                           | senao_se\n                           | vaziosenao_se : SENAOSE expressao ':' lista_declaracoes senao_opcionalexpressao : NEG expressao %prec UNARY_NEGdeclaracao_escrever : ESCREVER '(' expressao ')' ';'declaracao_comentario : COMENTARIOvazio :expressao : expressao CONCAT expressaobloco_funcao : lista_declaracoes"
    
_lr_action_items = {'VAR_ID':([0,1,2,3,4,5,6,7,8,10,12,13,14,16,17,18,19,20,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,48,49,51,54,55,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,88,89,90,91,92,100,103,104,105,108,110,116,117,121,124,125,127,128,130,131,132,133,135,137,138,139,],[9,9,-1,-3,-4,-5,-6,-7,-8,-10,44,46,46,-60,46,-30,-31,46,46,-2,60,46,46,-15,46,46,46,46,46,46,46,46,46,46,46,46,46,-32,46,-29,-52,84,85,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,93,-28,9,-33,46,-39,-11,46,-9,46,-41,9,46,46,-40,120,93,46,-59,9,-53,9,-37,46,9,46,9,9,-42,9,-38,-43,]),'FUNCAO':([0,1,2,3,4,5,6,7,8,10,16,18,19,26,30,46,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,86,88,90,92,100,105,117,121,124,125,127,130,132,133,135,137,138,139,],[12,12,-1,-3,-4,-5,-6,-7,-8,-10,-60,-30,-31,-2,-15,-32,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,12,-33,-39,-11,-9,-41,12,-40,-59,12,-53,12,-37,12,12,12,-42,12,-38,-43,]),'SE':([0,1,2,3,4,5,6,7,8,10,16,18,19,26,30,46,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,86,88,90,92,100,105,117,121,124,125,127,130,132,133,135,137,138,139,],[14,14,-1,-3,-4,-5,-6,-7,-8,-10,-60,-30,-31,-2,-15,-32,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,14,-33,-39,-11,-9,-41,14,-40,-59,14,-53,14,-37,14,14,14,-42,14,-38,-43,]),'ESCREVER':([0,1,2,3,4,5,6,7,8,10,16,18,19,26,30,46,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,86,88,90,92,100,105,117,121,124,125,127,130,132,133,135,137,138,139,],[15,15,-1,-3,-4,-5,-6,-7,-8,-10,-60,-30,-31,-2,-15,-32,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,15,-33,-39,-11,-9,-41,15,-40,-59,15,-53,15,-37,15,15,15,-42,15,-38,-43,]),'COMENTARIO':([0,1,2,3,4,5,6,7,8,10,16,18,19,26,30,46,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,86,88,90,92,100,105,117,121,124,125,127,130,132,133,135,137,138,139,],[16,16,-1,-3,-4,-5,-6,-7,-8,-10,-60,-30,-31,-2,-15,-32,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,16,-33,-39,-11,-9,-41,16,-40,-59,16,-53,16,-37,16,16,16,-42,16,-38,-43,]),'(':([0,1,2,3,4,5,6,7,8,9,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,48,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,83,86,88,89,90,91,92,100,103,104,105,116,117,121,124,125,127,128,130,131,132,133,135,137,138,139,],[13,13,-1,-3,-4,-5,-6,-7,-8,29,-10,13,13,48,-60,13,-30,-31,13,54,55,56,57,13,-2,13,13,-15,13,13,13,13,13,13,13,13,13,13,13,13,13,78,29,13,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,13,-33,13,-39,-11,13,-9,13,-41,13,13,13,-40,13,-59,13,-53,13,-37,13,13,13,13,13,-42,13,-38,-43,]),'-':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,16,17,18,19,20,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,81,82,83,86,88,89,90,91,92,100,102,103,104,105,106,107,116,117,118,119,121,124,125,126,127,128,130,131,132,133,134,135,136,137,138,139,],[17,17,-1,-3,-4,-5,-6,-7,-8,-32,-10,32,17,17,-60,17,-30,-31,17,17,-2,17,17,-15,17,17,17,17,17,17,17,17,17,17,17,17,17,32,-32,32,17,-29,-52,32,-58,32,32,-16,-17,-18,-19,32,32,32,32,32,32,32,32,32,-28,17,32,-33,17,-39,-11,17,-9,17,-41,17,32,17,17,-40,32,32,17,-59,32,32,17,-53,17,32,-37,17,17,17,17,17,32,-42,32,17,-38,-43,]),'NUM':([0,1,2,3,4,5,6,7,8,10,13,14,16,17,18,19,20,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,48,49,51,57,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,88,89,90,91,92,100,103,104,105,110,116,117,121,124,125,127,128,130,131,132,133,135,137,138,139,],[18,18,-1,-3,-4,-5,-6,-7,-8,-10,18,18,-60,18,-30,-31,18,18,-2,18,18,-15,18,18,18,18,18,18,18,18,18,18,18,18,18,-32,18,-29,-52,87,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,98,-28,18,-33,18,-39,-11,18,-9,18,-41,18,18,18,-40,98,18,-59,18,-53,18,-37,18,18,18,18,18,-42,18,-38,-43,]),'STRING':([0,1,2,3,4,5,6,7,8,10,13,14,16,17,18,19,20,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,48,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,83,86,88,89,90,91,92,100,103,104,105,116,117,121,124,125,127,128,130,131,132,133,135,137,138,139,],[19,19,-1,-3,-4,-5,-6,-7,-8,-10,19,19,-60,19,-30,-31,19,19,-2,19,19,-15,19,19,19,19,19,19,19,19,19,19,19,19,19,-32,19,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,19,-33,19,-39,-11,19,-9,19,-41,19,19,19,-40,19,-59,19,-53,19,-37,19,19,19,19,19,-42,19,-38,-43,]),'[':([0,1,2,3,4,5,6,7,8,10,13,14,16,17,18,19,20,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,48,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,86,88,89,90,91,92,100,103,104,105,110,116,117,121,124,125,127,128,130,131,132,133,135,137,138,139,],[20,20,-1,-3,-4,-5,-6,-7,-8,-10,20,20,-60,20,-30,-31,20,20,-2,20,20,-15,20,20,20,20,20,20,20,20,20,20,20,20,20,-32,20,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,99,-28,20,-33,20,-39,-11,20,-9,20,-41,20,20,20,-40,99,20,-59,20,-53,20,-37,20,20,20,20,20,-42,20,-38,-43,]),'MAP':([0,1,2,3,4,5,6,7,8,10,13,14,16,17,18,19,20,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,48,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,83,86,88,89,90,91,92,100,103,104,105,116,117,121,124,125,127,128,130,131,132,133,135,137,138,139,],[21,21,-1,-3,-4,-5,-6,-7,-8,-10,21,21,-60,21,-30,-31,21,21,-2,21,21,-15,21,21,21,21,21,21,21,21,21,21,21,21,21,-32,21,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,21,-33,21,-39,-11,21,-9,21,-41,21,21,21,-40,21,-59,21,-53,21,-37,21,21,21,21,21,-42,21,-38,-43,]),'FOLD':([0,1,2,3,4,5,6,7,8,10,13,14,16,17,18,19,20,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,48,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,83,86,88,89,90,91,92,100,103,104,105,116,117,121,124,125,127,128,130,131,132,133,135,137,138,139,],[22,22,-1,-3,-4,-5,-6,-7,-8,-10,22,22,-60,22,-30,-31,22,22,-2,22,22,-15,22,22,22,22,22,22,22,22,22,22,22,22,22,-32,22,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,22,-33,22,-39,-11,22,-9,22,-41,22,22,22,-40,22,-59,22,-53,22,-37,22,22,22,22,22,-42,22,-38,-43,]),'ENTRADA':([0,1,2,3,4,5,6,7,8,10,13,14,16,17,18,19,20,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,48,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,83,86,88,89,90,91,92,100,103,104,105,116,117,121,124,125,127,128,130,131,132,133,135,137,138,139,],[23,23,-1,-3,-4,-5,-6,-7,-8,-10,23,23,-60,23,-30,-31,23,23,-2,23,23,-15,23,23,23,23,23,23,23,23,23,23,23,23,23,-32,23,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,23,-33,23,-39,-11,23,-9,23,-41,23,23,23,-40,23,-59,23,-53,23,-37,23,23,23,23,23,-42,23,-38,-43,]),'ALEATORIO':([0,1,2,3,4,5,6,7,8,10,13,14,16,17,18,19,20,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,48,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,83,86,88,89,90,91,92,100,103,104,105,116,117,121,124,125,127,128,130,131,132,133,135,137,138,139,],[24,24,-1,-3,-4,-5,-6,-7,-8,-10,24,24,-60,24,-30,-31,24,24,-2,24,24,-15,24,24,24,24,24,24,24,24,24,24,24,24,24,-32,24,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,24,-33,24,-39,-11,24,-9,24,-41,24,24,24,-40,24,-59,24,-53,24,-37,24,24,24,24,24,-42,24,-38,-43,]),'NEG':([0,1,2,3,4,5,6,7,8,10,13,14,16,17,18,19,20,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46,48,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,82,83,86,88,89,90,91,92,100,103,104,105,116,117,121,124,125,127,128,130,131,132,133,135,137,138,139,],[25,25,-1,-3,-4,-5,-6,-7,-8,-10,25,25,-60,25,-30,-31,25,25,-2,25,25,-15,25,25,25,25,25,25,25,25,25,25,25,25,25,-32,25,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,25,-33,25,-39,-11,25,-9,25,-41,25,25,25,-40,25,-59,25,-53,25,-37,25,25,25,25,25,-42,25,-38,-43,]),'$end':([1,2,3,4,5,6,7,8,10,16,18,19,26,30,46,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,82,86,88,90,92,105,117,124,127,135,138,139,],[0,-1,-3,-4,-5,-6,-7,-8,-10,-60,-30,-31,-2,-15,-32,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,-33,-39,-11,-9,-41,-40,-59,-53,-37,-42,-38,-43,]),'SENAO':([2,3,4,5,6,7,8,10,16,18,19,26,30,46,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,82,86,88,90,92,100,105,117,124,127,135,137,138,139,],[-1,-3,-4,-5,-6,-7,-8,-10,-60,-30,-31,-2,-15,-32,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,-33,-39,-11,-9,-41,113,-40,-59,-53,-37,-42,113,-38,-43,]),'SENAOSE':([2,3,4,5,6,7,8,10,16,18,19,26,30,46,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,82,86,88,90,92,100,105,117,124,127,135,137,138,139,],[-1,-3,-4,-5,-6,-7,-8,-10,-60,-30,-31,-2,-15,-32,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,-33,-39,-11,-9,-41,116,-40,-59,-53,-37,-42,116,-38,-43,]),'FIM':([2,3,4,5,6,7,8,10,16,18,19,26,30,46,49,51,58,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,82,86,88,90,92,100,105,112,114,115,117,124,127,129,130,132,135,137,138,139,140,],[-1,-3,-4,-5,-6,-7,-8,-10,-60,-30,-31,-2,-15,-32,-29,-52,-58,-12,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,-33,-39,-11,-9,-41,-61,-40,124,-55,-56,-59,-53,-37,135,-63,-54,-42,-61,-38,-43,-57,]),',':([3,10,18,19,20,46,49,50,51,52,53,58,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,82,84,85,86,88,90,92,93,95,97,98,102,105,107,109,111,119,120,123,127,138,],[27,-10,-30,-31,-61,-32,-29,83,-52,-35,-36,-58,91,-12,91,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,-33,103,104,-39,-11,-9,-41,-48,110,-47,-49,-34,-40,-13,122,-51,128,-50,-46,-37,-38,]),'=':([9,60,],[28,89,]),';':([9,11,18,19,46,49,51,58,59,61,62,65,66,67,68,69,70,71,72,73,74,75,76,77,79,82,86,92,101,105,106,107,127,136,138,],[-32,30,-30,-31,-32,-29,-52,-58,88,90,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,-33,-39,-41,117,-40,-12,-13,-37,139,-38,]),'+':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,31,-30,-31,31,-32,31,-29,-52,31,-58,31,31,-16,-17,-18,-19,31,31,31,31,31,31,31,31,31,-28,31,-33,-39,-41,31,-40,31,31,31,31,31,-37,31,31,-38,]),'*':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,33,-30,-31,33,-32,33,-29,-52,33,-58,33,33,33,33,-18,-19,33,33,33,33,33,33,33,33,33,-28,33,-33,-39,-41,33,-40,33,33,33,33,33,-37,33,33,-38,]),'/':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,34,-30,-31,34,-32,34,-29,-52,34,-58,34,34,34,34,-18,-19,34,34,34,34,34,34,34,34,34,-28,34,-33,-39,-41,34,-40,34,34,34,34,34,-37,34,34,-38,]),'AND':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,35,-30,-31,35,-32,35,-29,-52,35,-58,35,35,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,35,-28,35,-33,-39,-41,35,-40,35,35,35,35,35,-37,35,35,-38,]),'OR':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,36,-30,-31,36,-32,36,-29,-52,36,-58,36,36,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,36,-28,36,-33,-39,-41,36,-40,36,36,36,36,36,-37,36,36,-38,]),'EQ':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,37,-30,-31,37,-32,37,-29,-52,37,-58,37,37,-16,-17,-18,-19,37,37,-22,-23,-24,-25,-26,-27,37,-28,37,-33,-39,-41,37,-40,37,37,37,37,37,-37,37,37,-38,]),'NE':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,38,-30,-31,38,-32,38,-29,-52,38,-58,38,38,-16,-17,-18,-19,38,38,-22,-23,-24,-25,-26,-27,38,-28,38,-33,-39,-41,38,-40,38,38,38,38,38,-37,38,38,-38,]),'LT':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,39,-30,-31,39,-32,39,-29,-52,39,-58,39,39,-16,-17,-18,-19,39,39,-22,-23,-24,-25,-26,-27,39,-28,39,-33,-39,-41,39,-40,39,39,39,39,39,-37,39,39,-38,]),'LE':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,40,-30,-31,40,-32,40,-29,-52,40,-58,40,40,-16,-17,-18,-19,40,40,-22,-23,-24,-25,-26,-27,40,-28,40,-33,-39,-41,40,-40,40,40,40,40,40,-37,40,40,-38,]),'GT':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,41,-30,-31,41,-32,41,-29,-52,41,-58,41,41,-16,-17,-18,-19,41,41,-22,-23,-24,-25,-26,-27,41,-28,41,-33,-39,-41,41,-40,41,41,41,41,41,-37,41,41,-38,]),'GE':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,42,-30,-31,42,-32,42,-29,-52,42,-58,42,42,-16,-17,-18,-19,42,42,-22,-23,-24,-25,-26,-27,42,-28,42,-33,-39,-41,42,-40,42,42,42,42,42,-37,42,42,-38,]),'CONCAT':([9,11,18,19,45,46,47,49,51,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,81,82,86,92,102,105,106,107,118,119,126,127,134,136,138,],[-32,43,-30,-31,43,-32,43,-29,-52,43,-58,43,43,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,43,-28,43,-33,-39,-41,43,-40,43,43,43,43,43,-37,43,43,-38,]),')':([18,19,45,46,49,51,56,58,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,86,87,92,93,94,95,96,97,98,105,107,111,118,120,123,127,134,138,],[-30,-31,79,-32,-29,-52,86,-58,92,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-61,-28,101,-33,-39,105,-41,-48,109,-44,-45,-47,-49,-40,-13,-51,127,-50,-46,-37,138,-38,]),':':([18,19,46,47,49,51,58,65,66,67,68,69,70,71,72,73,74,75,76,77,79,82,86,92,93,105,109,113,122,126,127,138,],[-30,-31,-32,80,-29,-52,-58,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,-33,-39,-41,108,-40,121,125,131,133,-37,-38,]),']':([18,19,20,46,49,50,51,52,53,58,65,66,67,68,69,70,71,72,73,74,75,76,77,79,82,86,92,99,102,105,127,138,],[-30,-31,51,-32,-29,82,-52,-35,-36,-58,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-62,-28,-33,-39,-41,111,-34,-40,-37,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista_declaracoes':([0,80,121,125,133,],[1,100,130,132,137,]),'declaracao':([0,1,80,100,121,125,130,132,133,137,],[2,26,2,26,2,2,26,26,2,26,]),'declaracao_atribuicao':([0,1,80,100,121,125,130,132,133,137,],[3,3,3,3,3,3,3,3,3,3,]),'declaracao_expressao':([0,1,80,100,121,125,130,132,133,137,],[4,4,4,4,4,4,4,4,4,4,]),'declaracao_funcao':([0,1,80,100,121,125,130,132,133,137,],[5,5,5,5,5,5,5,5,5,5,]),'declaracao_se':([0,1,80,100,121,125,130,132,133,137,],[6,6,6,6,6,6,6,6,6,6,]),'declaracao_escrever':([0,1,80,100,121,125,130,132,133,137,],[7,7,7,7,7,7,7,7,7,7,]),'declaracao_comentario':([0,1,80,100,121,125,130,132,133,137,],[8,8,8,8,8,8,8,8,8,8,]),'atribuicao':([0,1,27,80,100,121,125,130,132,133,137,],[10,10,59,10,10,10,10,10,10,10,10,]),'expressao':([0,1,13,14,17,20,25,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,48,80,83,89,91,100,103,104,116,121,125,128,130,131,132,133,137,],[11,11,45,47,49,52,58,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,81,11,102,106,107,11,118,119,126,11,11,134,11,136,11,11,11,]),'lista_elementos':([20,],[50,]),'vazio':([20,78,100,137,],[53,96,115,115,]),'lista_expressoes':([28,29,],[61,63,]),'lista_parametros_opcional':([78,],[94,]),'lista_parametros':([78,],[95,]),'parametro':([78,110,],[97,123,]),'senao_opcional':([100,137,],[112,140,]),'senao_se':([100,137,],[114,114,]),'bloco_funcao':([121,],[129,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lista_declaracoes","S'",1,None,None,None),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','arith_grammar.py',39),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','arith_grammar.py',40),
  ('declaracao -> declaracao_atribuicao','declaracao',1,'p_declaracao','arith_grammar.py',49),
  ('declaracao -> declaracao_expressao','declaracao',1,'p_declaracao','arith_grammar.py',50),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','arith_grammar.py',51),
  ('declaracao -> declaracao_se','declaracao',1,'p_declaracao','arith_grammar.py',52),
  ('declaracao -> declaracao_escrever','declaracao',1,'p_declaracao','arith_grammar.py',53),
  ('declaracao -> declaracao_comentario','declaracao',1,'p_declaracao','arith_grammar.py',54),
  ('declaracao_atribuicao -> VAR_ID = lista_expressoes ;','declaracao_atribuicao',4,'p_declaracao_atribuicao','arith_grammar.py',59),
  ('declaracao_atribuicao -> atribuicao','declaracao_atribuicao',1,'p_declaracao_atribuicao_multipla','arith_grammar.py',64),
  ('declaracao_atribuicao -> declaracao_atribuicao , atribuicao ;','declaracao_atribuicao',4,'p_declaracao_atribuicao_multipla','arith_grammar.py',65),
  ('atribuicao -> VAR_ID = expressao','atribuicao',3,'p_atribuicao','arith_grammar.py',79),
  ('lista_expressoes -> lista_expressoes , expressao','lista_expressoes',3,'p_lista_expressoes','arith_grammar.py',83),
  ('lista_expressoes -> expressao','lista_expressoes',1,'p_lista_expressoes','arith_grammar.py',84),
  ('declaracao_expressao -> expressao ;','declaracao_expressao',2,'p_declaracao_expressao','arith_grammar.py',95),
  ('expressao -> expressao + expressao','expressao',3,'p_expressao','arith_grammar.py',100),
  ('expressao -> expressao - expressao','expressao',3,'p_expressao','arith_grammar.py',101),
  ('expressao -> expressao * expressao','expressao',3,'p_expressao','arith_grammar.py',102),
  ('expressao -> expressao / expressao','expressao',3,'p_expressao','arith_grammar.py',103),
  ('expressao -> expressao AND expressao','expressao',3,'p_expressao_se','arith_grammar.py',109),
  ('expressao -> expressao OR expressao','expressao',3,'p_expressao_se','arith_grammar.py',110),
  ('expressao -> expressao EQ expressao','expressao',3,'p_expressao_se','arith_grammar.py',111),
  ('expressao -> expressao NE expressao','expressao',3,'p_expressao_se','arith_grammar.py',112),
  ('expressao -> expressao LT expressao','expressao',3,'p_expressao_se','arith_grammar.py',113),
  ('expressao -> expressao LE expressao','expressao',3,'p_expressao_se','arith_grammar.py',114),
  ('expressao -> expressao GT expressao','expressao',3,'p_expressao_se','arith_grammar.py',115),
  ('expressao -> expressao GE expressao','expressao',3,'p_expressao_se','arith_grammar.py',116),
  ('expressao -> ( expressao )','expressao',3,'p_expressao_grupo','arith_grammar.py',122),
  ('expressao -> - expressao','expressao',2,'p_expressao_uminus','arith_grammar.py',127),
  ('expressao -> NUM','expressao',1,'p_expressao_num','arith_grammar.py',132),
  ('expressao -> STRING','expressao',1,'p_expressao_string','arith_grammar.py',141),
  ('expressao -> VAR_ID','expressao',1,'p_expressao_var_id','arith_grammar.py',162),
  ('expressao -> [ lista_elementos ]','expressao',3,'p_expressao_array','arith_grammar.py',167),
  ('lista_elementos -> lista_elementos , expressao','lista_elementos',3,'p_lista_elementos','arith_grammar.py',172),
  ('lista_elementos -> expressao','lista_elementos',1,'p_lista_elementos','arith_grammar.py',173),
  ('lista_elementos -> vazio','lista_elementos',1,'p_lista_elementos','arith_grammar.py',174),
  ('expressao -> MAP ( VAR_ID , expressao )','expressao',6,'p_expressao_map','arith_grammar.py',186),
  ('expressao -> FOLD ( VAR_ID , expressao , expressao )','expressao',8,'p_expressao_fold','arith_grammar.py',191),
  ('expressao -> ENTRADA ( )','expressao',3,'p_expressao_entrada','arith_grammar.py',196),
  ('expressao -> ALEATORIO ( NUM )','expressao',4,'p_expressao_aleatorio','arith_grammar.py',201),
  ('expressao -> VAR_ID ( lista_expressoes )','expressao',4,'p_expressao_chamada_funcao','arith_grammar.py',206),
  ('declaracao_funcao -> FUNCAO VAR_ID ( lista_parametros_opcional ) : bloco_funcao FIM','declaracao_funcao',8,'p_declaracao_funcao','arith_grammar.py',211),
  ('declaracao_funcao -> FUNCAO VAR_ID ( lista_parametros_opcional ) , : expressao ;','declaracao_funcao',9,'p_declaracao_funcao','arith_grammar.py',212),
  ('lista_parametros_opcional -> lista_parametros','lista_parametros_opcional',1,'p_lista_parametros_opcional','arith_grammar.py',221),
  ('lista_parametros_opcional -> vazio','lista_parametros_opcional',1,'p_lista_parametros_opcional','arith_grammar.py',222),
  ('lista_parametros -> lista_parametros , parametro','lista_parametros',3,'p_lista_parametros','arith_grammar.py',227),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','arith_grammar.py',228),
  ('parametro -> VAR_ID','parametro',1,'p_parametro_varid','arith_grammar.py',237),
  ('parametro -> NUM','parametro',1,'p_parametro_num','arith_grammar.py',242),
  ('parametro -> VAR_ID : VAR_ID','parametro',3,'p_parametro_var_id_array','arith_grammar.py',251),
  ('parametro -> [ ]','parametro',2,'p_parametro_array_vazio','arith_grammar.py',257),
  ('expressao -> [ ]','expressao',2,'p_empty_list','arith_grammar.py',262),
  ('declaracao_se -> SE expressao : lista_declaracoes senao_opcional FIM','declaracao_se',6,'p_declaracao_se','arith_grammar.py',267),
  ('senao_opcional -> SENAO : lista_declaracoes','senao_opcional',3,'p_senao_opcional','arith_grammar.py',276),
  ('senao_opcional -> senao_se','senao_opcional',1,'p_senao_opcional','arith_grammar.py',277),
  ('senao_opcional -> vazio','senao_opcional',1,'p_senao_opcional','arith_grammar.py',278),
  ('senao_se -> SENAOSE expressao : lista_declaracoes senao_opcional','senao_se',5,'p_senao_se','arith_grammar.py',287),
  ('expressao -> NEG expressao','expressao',2,'p_expressao_negacao','arith_grammar.py',296),
  ('declaracao_escrever -> ESCREVER ( expressao ) ;','declaracao_escrever',5,'p_declaracao_escrever','arith_grammar.py',301),
  ('declaracao_comentario -> COMENTARIO','declaracao_comentario',1,'p_declaracao_comentario','arith_grammar.py',306),
  ('vazio -> <empty>','vazio',0,'p_vazio','arith_grammar.py',311),
  ('expressao -> expressao CONCAT expressao','expressao',3,'p_expressao_concat','arith_grammar.py',316),
  ('bloco_funcao -> lista_declaracoes','bloco_funcao',1,'p_bloco_funcao','arith_grammar.py',321),
]
