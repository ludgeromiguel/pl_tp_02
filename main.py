from arith_grammar import ArithGrammar
from arith_eval import ArithEval
import sys
from pprint import PrettyPrinter
pp = PrettyPrinter(sort_dicts=False)

ag = ArithGrammar()
ag.build()


if len(sys.argv) == 2:
    if not sys.argv[1].endswith('.fca'):
        print('Arquivo não é da linguagem FCA')
        exit(0)

    with open(sys.argv[1], "r") as file:
        contents = file.read()
        try:
            ast = ag.parse(contents)
            print("Grammar gerado:")
            pp.pprint(ast)
            resultado = ArithEval.evaluate(ast)
            print(f"<< {resultado}")
        except Exception as e:
            print(e, file=sys.stderr)
else:
    for expr in iter(lambda: input(">> "), ""):
        try:
            ast = ag.parse(expr)
            print("Grammar gerado:")
            pp.pprint(ast)
            res = ArithEval.evaluate(ast)
            if res is not None:
                print(f"<< {res}")
        except Exception as e:
            print(e)