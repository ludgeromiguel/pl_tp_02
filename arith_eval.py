# arith_eval
import random


class ArithEval:
    # guardar as atribuições de variáveis
    symbols = {}

    # guardar as funções declaradas
    functions = {}

    # Defenir o que cada operador faz
    operators = {
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "/": lambda args: args[0] / args[1],
        # Condições dos ifs
        "==": lambda args: args[0] == args[1],
        "!=": lambda args: args[0] != args[1],
        "<": lambda args: args[0] < args[1],
        ">": lambda args: args[0] > args[1],
        "<=": lambda args: args[0] <= args[1],
        ">=": lambda args: args[0] >= args[1],
        "&&": lambda args: args[0] and args[1],
        "||": lambda args: args[0] or args[1],
        'neg': lambda args: not args[0],
        #####
        "seq": lambda args: args[-1],
        "string": lambda args: str(args[0]),
        "float": lambda args: float(args[0]),
        "int": lambda args: int(args[0]),
        "escrever": lambda args: print(args[0]),
        "atribuicao": lambda args: ArithEval._atribuicao(args),
        "comentario": lambda args: ArithEval._comentario(args),
        "concat": lambda args: f'{args[0]}{args[1]}',
        "interpolacao": lambda args: ''.join(args),
        "entrada": lambda args: ArithEval._entrada(args),
        "aleatorio": lambda args: ArithEval._aleatorio(args),
        "call_func": lambda args: ArithEval._call_func(args),
        "elementos_array": lambda args: args,
        "array_vazio": lambda args: [],
        "map": lambda args: ArithEval._map(args),
        "fold": lambda args: ArithEval._fold(args),
    }

    @staticmethod
    def _atribuicao(args):
        varid = args[0]  # 'A'
        value = args[1]  # 10
        ArithEval.symbols[varid] = value  # symbols { 'A':10 }
        #print(f'{varid}: {value}')
        return value

    @staticmethod
    def _comentario(args):
        # Devolver None porque é um comentario
        return None

    @staticmethod
    def _entrada(args):
        # Chamar a função de input do python para introduzir o valor
        return input("Função entrada, introduza o valor: ")

    @staticmethod
    def _aleatorio(args):
        maxNumero = int(args[0])  # Obter o parametro da função aleatorio
        # Validar se não é menor que 0
        if maxNumero <= 0:
            raise Exception("O valor do aleatorio tem de ser maior que 0")

        # Devolver um número random entre 0 e o parametro
        return random.randint(0, maxNumero)

    @staticmethod
    def _funcao(args):
        nome_funcao = args[0]
        parametros_funcao = args[1]
        corpo_funcao = args[2]

        if nome_funcao not in ArithEval.functions:
            ArithEval.functions[nome_funcao] = []

        ArithEval.functions[nome_funcao].append({
            'parametros': parametros_funcao,
            'corpo': corpo_funcao
        })

        return nome_funcao

    @staticmethod
    def _call_func(args):
        nome_funcao = args[0]
        parametros_chamada = args[1]

        # Validar se a função foi declarada
        if nome_funcao not in ArithEval.functions:
            raise Exception(f"Função '{nome_funcao}' não declarada")

        # Percorrer as funções com o nome
        for func_def in ArithEval.functions[nome_funcao]:
            parametros_funcao = func_def['parametros'] # Obter os parametros da função
            copor_funcao = func_def['corpo'] # Obter o corpo da função

            # Validar se os parametros da função e os que estamos a passar são os mesmos
            if len(parametros_funcao) == len(parametros_chamada):
                # Salvar o estado atual das variaveis
                estado_temp = ArithEval.symbols.copy()

                # Adicionar as variaveis as variaveis da função porque as mesmas são globais
                funcao_symbols = estado_temp.copy()

                # O zip é para percorrer os dois arrays ao mesmo tempo, ou sejá, ele meio que gera uma matriz
                for param, value in zip(parametros_funcao, parametros_chamada):
                    # Se o parametro da função for uma var adicionamos o valor que estamos a passar na chamada
                    if 'var' in param:
                        funcao_symbols[param['var']] = value
                    # Se for um var:array pegamos no 1º valor do array e depois passamos o resto do array
                    elif 'op' in param and param['op'] == 'var_id_array':
                        # Validar se é realmente um array
                        if type(value) is not list:
                            raise Exception(f"O parametro da função {nome_funcao} tem de ser um array")

                        funcao_symbols[param['args'][0]] = value.pop()  # Remover o 1º elemento do array
                        funcao_symbols[param['args'][1]] = value  # Passar o resto dos elementos do array
                    # Se o parametro for um numero e for igual ao que estamos a passar nós avançamos
                    elif 'op' in param and ArithEval.evaluate(param) == value:
                        continue
                    else:
                        break
                else: # Se todos os parametros da função estiverem validos nós executamos a função da iteração atual do loop
                    # Substituir temporariamente as variaveis globais
                    ArithEval.symbols = funcao_symbols
                    # Processar o corpo da função
                    result = ArithEval.evaluate(copor_funcao)

                    # Restaurar as variaveis globais
                    ArithEval.symbols = estado_temp
                    # Returnar o resultado da execução do corpo da função
                    return result

        # Devolver o erro caso não exista nenhuma convinação de parametros correta para a função
        raise Exception(f"Nenhuma correspondência de parâmetros para a função '{nome_funcao}'")

    @staticmethod
    def _map(args):
        funcao = args[0]  # Obter o nome da função
        array = args[1]  # Obter o array

        # Validar se o parametro é mesmo um array
        if type(array) is not list:
            raise Exception(f"O segundo parametro do map tem de ser um array")

        # Validar se a função existe
        if funcao not in ArithEval.functions:
            raise Exception(f"A função passada no map não foi declarada")

        resultado = []

        # Percorrer os elementos do array e chamar a função para cada elemento
        for item in array:
            resultado.append(ArithEval._call_func([funcao, [item]]))

        # Devolver o resultado final
        return resultado

    @staticmethod
    def _fold(args):
        funcao = args[0]  # Obter o nome da função
        array = args[1]  # Obter o array
        valor_inicial = args[2]  # Obter o valor inicial para o fold

        # Validar se o parametro é mesmo um array
        if type(array) is not list:
            raise Exception(f"O segundo parametro do fold tem de ser um array")

        # Validar se o parametro é mesmo um número
        if type(valor_inicial) is not int:
            raise Exception(f"O terceiro parametro do fold tem de ser um número ")

        # Validar se a função existe
        if funcao not in ArithEval.functions:
            raise Exception(f"A função passada no map não foi declarada")

        # O resultado começa com o valor inicial
        resultado = valor_inicial

        # Percorrer o array ao "contrario"
        for item in reversed(array):
            resultado = ArithEval._call_func([funcao, [item, resultado]])

        return resultado

    @staticmethod
    def _se(args):
        condicao = ArithEval._eval_operator(args[0]) # Validar a condição

        # Se for verdadeira retornar o valor do SE
        if condicao:
            return ArithEval.evaluate(args[1])
        elif len(args) > 2: # Se os args forem maiores que 2 quer dizer que tem um senão ou um senão se
            index = 2
            while index < len(args):
                # Verificar se é uma condição senao_se
                if 'op' in args[index] and args[index]['op'] == 'senao_se':
                    condicao_senao_se = ArithEval.evaluate(args[index]['args'][0]) # Obter o valor da condição
                    # Validar condição, se for verdadeira executar o código da mesma
                    if condicao_senao_se:
                        return ArithEval.evaluate(args[index]['args'][1])
                    index +=1  # Pular para o proxima senão_se ou senao
                # Validar a condição de senão
                elif 'op' in args[index] and args[index]['op'] == 'senao':
                    return ArithEval.evaluate(args[index]['args'][0])
                else:
                    index += 1

        return None


    @staticmethod
    def evaluate(ast):
        if type(ast) is int:  # constant value, eg in (int, str)
            return ast
        if type(ast) is dict:  # { 'op': ... , 'args': ...}
            return ArithEval._eval_operator(ast)
        if type(ast) is str:
            return ast
        if type(ast) is list: # [ item, item ]
            return [ArithEval.evaluate(a) for a in ast]
        raise Exception(f"Tipo de AST desconhecido {ast}")

    @staticmethod
    def _eval_operator(ast):
        # Processar quando for uma função
        if 'op' in ast and ast['op'] == 'funcao':
            return ArithEval._funcao(ast['args'])

        # Processar quando for um se
        if 'op' in ast and ast['op'] == 'se':
            return ArithEval._se(ast['args'])

        if 'op' in ast:
            op = ast["op"]
            args = [ArithEval.evaluate(a) for a in ast['args']]
            if op in ArithEval.operators:
                func = ArithEval.operators[op]
                return func(args)
            else:
                raise Exception(f"Operador '{op}' desconhecido")

        if 'var' in ast:
            varid = ast["var"]  # ast={ 'var': "A" } =>   ast["var"]   varid="A"
            if varid in ArithEval.symbols:  # "A" in symbols { 'A':10 }
                return ArithEval.symbols[varid]  # 10
            raise Exception(f"error: '{varid}' não declarado (primeira utilização nesta função)")
        raise Exception('AST indefinido')
