import ply.lex as plex


class ArithLexer:
    tokens = (
        "NUM",  # numero inteiro
        "STRING",  # string delimitada por aspas duplas
        "FIM",  # atribuicao para o "FIM" das funções
        "FUNCAO",  # identificador de uma função
        "ESCREVER",  # Escrever dados
        "VAR_ID",  # identificador de variável ou função
        "COMENTARIO",  # identificador de um comentario
        "SE",  # identificador de uma confição if
        "SENAO",  # identificador de uma condição else
        "SENAOSE",  # Identificador do senão se
        "NEG",  # Negação da condição do if
        "ENTRADA",  # Identificador para input de dados
        "ALEATORIO",  # Identificador de gerado de um numero aleatorio
        "MAP",  # Identificador para a função MAP
        "FOLD",  # Identificador para a função FOLD
        "CONCAT",  # Identificador de concatnação
        "AND",  # Identificador do and
        "OR",  # Identificador do or
        "EQ",  # Identificador de igual
        "NE",  # Identificador do diferente
        "LT",  # Identificador do menor
        "LE",  # Identificador do menor ou igual
        "GT",  # Identificador do maior
        "GE",  # Identificador do maior ou igual
    )

    literals = [
        '+',  # sinal de soma
        '-',  # sinal de subtração
        '*',  # sinal de multiplicação
        '/',  # sinal de divisão
        '=',  # sinal de igual
        '(',  # parêntese esquerdo
        ')',  # parêntese direito
        '[',  # parêntese reto esquerdo
        ']',  # parêntese reto direito
        '>',  # sinal de maior que
        '<',  # sinal de menor que
        ',',  # vírgula
        ';',  # ponto-e-vírgula
        ':',  # dois pontos
        '!',  # Diferente
    ]

    # Ignorar espacos
    t_ignore = " \t\n"

    # Inicializa o lexer como None
    def __init__(self):
        self.lexer = None

    # Reconhecer numeros inteiros e decimais
    def t_NUM(self, t):
        r"[0-9]+(\.[0-9]+)?"
        return t

    # Reconhecer a Palavra ESC ou ESCREVER
    def t_ESCREVER(self, t):
        # \b -> limite de palavra, garante que é exatamente o que está no regex
        r"[Ee][Ss][Cc]([Rr][Ee][Vv][Ee][Rr])?\b"
        return t

    # Reconhecedor de FIM
    def t_FIM(self, t):
        r"[Ff][Ii][Mm]"
        return t

    # Reconhecedor de FUNCAO
    def t_FUNCAO(self, t):
        r"[Ff][Uu][Nn][Cc][Aa][Oo]"
        return t

    # Reconhecedor de uma string
    def t_STRING(self, t):
        # Proteção para não parar nos \"
        r'"(\\.|[^"\\])*"'
        t.value = t.value[1:-1]  # Remove aspas
        return t

    #Reconhecedor de COMENTARIO
    def t_COMENTARIO(self, t):
        # Reconhece comentários de uma linha iniciados por '--'
        # Reconhece comentários multilinha delimitados por '{-' e '-}', foi adicionado o [\s\S] para incluir quebras de linha
        r"(--[^\n]*|{-[\s\S]*?-})"

        # remover os "identificadores" dos comentarios
        if t.value.startswith('--'):
            t.value = t.value[2:].strip()
        elif t.value.startswith('{-'):
            t.value = t.value[2:-2].strip()

        return t

    #Reconhecedor de SE
    def t_SE(self, t):
        r"[Ss][Ee]\b"
        return t

    #Reconhecedor de SENAO
    def t_SENAO(self, t):
        r"[Ss][Ee][Nn][Aa][Oo]\b"
        return t

    #Reconhecedor de SENAOSE
    def t_SENAOSE(self, t):
        r"[Ss][Ee][Nn][Aa][Oo][Ss][Ee]\b"
        return t

    #Reconhecedor de NEG (negação da condição)
    def t_NEG(self, t):
        r"[Nn][Ee][Gg]"
        return t

    #Reconhecedor de ENTRADA
    def t_ENTRADA(self, t):
        # \b -> limite de palavra, garante que é exatamente o que está no regex
        r"[Ee][Nn][Tt]([Rr][Aa][Dd][Aa])?\b"
        return t

    #Reconhecedor de MAP
    def t_MAP(self, t):
        r"[Mm][Aa][Pp]\b"
        return t

    #Reconhecedor de FOLD
    def t_FOLD(self, t):
        r"[Ff][Oo][Ll][Dd]\b"
        return t

    #Reconhecedor de CONCAT
    def t_CONCAT(self, t):
        r"<>"
        return t

    #Reconhecedor de ALEATORIO
    def t_ALEATORIO(self, t):
        r"[Aa][Ll][Ee][Aa][Tt][Oo][Rr][Ii][Oo]"
        return t

    # Reconhecer o AND
    def t_AND(self, t):
        r"&&"
        return t

    # Reconhecer o OR
    def t_OR(self, t):
        r"\|\|"
        return t

    # Reconhecer o EQ
    def t_EQ(self, t):
        r"=="
        return t

    # Reconhecer o NE
    def t_NE(self, t):
        r"!="
        return t

    # Reconhecer o LE
    def t_LE(self, t):
        r"<="
        return t

    # Reconhecer o GE
    def t_GE(self, t):
        r">="
        return t

    # Reconhecer o LT
    def t_LT(self, t):
        r"<"
        return t

    # Reconhecer o GT
    def t_GT(self, t):
        r">"
        return t
    
    # Reconhecer uma variavel e função
    def t_VAR_ID(self, t):
        # Deve iniciar por letra minuscula ou _
        # Depois pode ter qualquer letra minuscula/maiuscula e números
        # Pode terminar com ? ou !
        r"[a-z_][a-zA-Z0-9_]*[?!]?"
        return t

    # cria o lexer
    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    # define a entrada do lexer
    def input(self, string):
        self.lexer.input(string)

    # Obter proximo token do lexer
    def token(self):
        token = self.lexer.token()  # percorrer todos os tokens
        return token if token is None else token.type

    # Ocorre quando ocorre erro lexico
    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)
