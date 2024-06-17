# arith.py
import json

from arith_grammar import ArithGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

teste = ArithGrammar()
teste.build()

exemplos = [ # exemplos a avaliar de forma independente...
            'ESCREVER("ola mundo!");',
            'ESCREVER("PL " <> 2 <> "o ano de" <> "ESI");',
            'ESCREVER("soma de " <> 9 <> "com " <> 3*4 <> "=" <> 9+2*3);',
            'FUNCAO teste(a, b) ,: a+b;',
            'FUNCAO soma2(c) :\nc = c+1 ;\nc+1 ;\nFIM',
            'nome="diogo", idade=10;',
            "FUNCAO soma(a,b) ,: a+b ;\nFUNCAO soma2(c) :\nc = c+1 ;\nc+1 ;\nFIM\nseis = soma(4,2);\noito = soma2(seis);",
            "ESCREVER(\"Ola, \"<> curso); -- Ola, ESI",
            "{- exemplo interpolação de strings\nOlá, EST IPCA! -}\nescola =\"EST\";\ninst = \"IPCA\";\nESCREVER (\"Olá, #{escola} #{inst}!\");",
            "FUNCAO area(a,b),: a*b ;\nFUNCAO area(c),: area(c, c);\nd = area(10, 20);\ne = area(30);",
            "FUNCAO fib( 0 ),: 0 ;\nFUNCAO fib( 1 ),: 0 ;\nFUNCAO fib( n ):\na = fib(n-1);\nb = fib(n-2);\na + b;\nFIM\nfib5 = fib(5);",
            "lista = [ 1, 2, 3 ] ;\nESCREVER( lista ); -- [1,2,3];\nvazia = [] ;\nlista_str = [\"teste\"];",
            "FUNCAO mais2( x ),: x + 2 ;\nFUNCAO soma( a, b ),: a + b ;\nlista1 = map( mais2, [] );\nlista2 = map( mais2, [ 1, 2, 3 ] );\nlista3 = fold( soma, [ 1, 2, 3 ], 0 );",
            "array = [1, 2, 3];",
            "FUNCAO somatorio( [] ),: 0 ;FUNCAO somatorio( x:xs ),: x + somatorio(xs) ;",
            "SE var1 == var2: \nESCREVER(\"OLA\");\nSENAOSE var1 != var2:\nESCREVER(\"OLA2\");\nFIM",
            "SE var1 == var2: \nESCREVER(\"OLA\");\nFIM",
            "SE NEG var1 == var2: \nESCREVER(\"OLA\");\nSENAOSE NEG var1 != var2:\nESCREVER(\"OLA2\");\nSENAO: var1 = 2 \nFIM",
            "SE NEG var1 == var2: \nESCREVER(\"OLA\");\nFIM",
            "valor = ENTRADA();",
            "ate10 = ALEATORIO(10);",
            """
            FUNCAO soma(a,b),: a+b ;
            FUNCAO soma2(c) :
                c = c+1 ;
                c+1 ;
            FIM
            seis = soma(4,2);
            oito = soma2(seis);""",
            """lista2 = map( mais2, [ 1, 2, 3 ] );
            lista3 = FOLD( soma, [ 1, 2, 3 ], 0 ); """,
"""valor1 = 20;
valor2 = 20;
SE valor1 <= valor2 && 1 == 1:
    ESCREVER("Menor");
SENAO:
    ESCREVER("Maior ou igual");
FIM"""
            ]

result = {}

for frase in exemplos:
    print(f"----------------------")
    print(f"--- frase '{frase}'")
    resposta = teste.parse( frase )
    print("resultado: ")
    pp.pprint(resposta)

    result[frase] = resposta

with open('result_grammar.json', 'w') as f:
    json.dump(result, f, indent=4)