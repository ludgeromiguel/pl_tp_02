# arith_lexer_test.py
from arith_lexer import ArithLexer

al = ArithLexer()
al.build()
al.input("(3-6)+9")  # "2++3") #"(3+5)*7")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("num+2")  # "2++3") #"(3+5)*7")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input(""" x = 10  ; 
   y = 10 + 20 * 30;
   z = x * 100 ; 
   b =  a + 1 ; """)

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""_cart? = 10, _cart! = 20;
            ESC(_cart+_cart)""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""_cart? = 10, _cart! = 20;
            FUNCAO soma (a, b)
                a + b
            FIM
            _Soma = soma(_cart?, _cart!)""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""_cart? = 10, _cart! = 20;
            FUNCAO soma (a, b) :, a + b;
            _Soma = soma(_cart?, _cart!)""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""ESC("Teste " <> 10 < 1)""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""ano=2023, _mes!="maio";""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""ESCREVER ("Olá, #{escola} teste #{inst}!");""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""SE var1 == var2: \nESCREVER(\"OLA\");\nSENAOSE var1 != var2:\nESCREVER(\"OLA2\");\nFIM""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""valor = ENTRADA();\nate10 = ALEATORIO(10);""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""FUNCAO soma(a,b),: a+b ;\nFUNCAO soma2(c) :\nc = c+1 ;\nc+1 ;\nFIM\nseis = soma(4,2);\noito = soma2(seis);""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""lista2 = map( mais2, [ 1, 2, 3 ] );
lista3 = FOLD( soma, [ 1, 2, 3 ], 0 ); """)

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""valor1 = 20;
valor2 = 20;
SE valor1 <= valor2 && 1 == 1
    ESCREVER("Menor");
SENAO:
    ESCREVER("Maior ou igual");
FIM""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")
