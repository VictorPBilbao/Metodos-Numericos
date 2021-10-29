# import Union for types
from typing import Union

#? Uma matriz é uma lista de listas que contem inteiros ou floats
matriz = list[list[Union[int, float]]]

def criar_matriz(linhas: int, colunas: int, valores: list[Union[int, float]] or int) -> matriz:
    """Cria uma matriz de `linhas` x `colunas` e o preenche com os `valores` passados. Primeiro verifica
    se `valores` é uma lista ou um inteiro, e entao cria a matriz e preenche com os `valores`.
    
    Argumentos:
    --------
        `linhas (int)`: quantas linhas a matriz terá
        `colunas (int)`: quantas colunas a matriz terá
        `valores (list[int|float] | int)`: Valor(es) com que a matriz sera preenchida. Se for apenas um numero, ele sera usado em toda a matriz. 
        Se `valores` for uma lista, ela deve ter o mesmo tamanho que `linhas` x `colunas`.
        
    Retornos:
    --------
        `Matriz`: retorna uma matriz de tamanho `linhas x colunas` preenchida com os valores passados.
    
    Exemplos:
    --------
    >>> criar_matriz(2, 3, 1)
    >>> output: [[1, 1, 1], [1, 1, 1]]
    --------
    >>> criar_matriz(2, 3, [1, 2, 3, 4, 5, 6])
    >>> output: [[1, 2, 3], [4, 5, 6]]
    """
    matriz_retorno: matriz = []
    
    #? verifica se valores é um unico valor de inteiro ou float
    if type(valores) in [int, float]:
        items: list[int] = []
        for _ in range(linhas):
            matriz_retorno.append([valores] * colunas)
    # ? se for valores é uma lista com todos os valores inteiros ou floats
    elif type(valores) == list and all(isinstance(x, (int, float)) for x in valores):
        if linhas * colunas != len(valores):
            raise ValueError(
                f"Tamanho da lista deve ser de {linhas * colunas} (linhas x colunas), nao de {len(valores)}")
        #? separa a lista de valores em partes iguais onde cada sublisa tera o tamanho de colunas
        #? exemplo para matrix 2x3: [1, 2, 3, 4, 5, 6] -> [[1, 2, 3], [4, 5, 6]]
        for i in range(0, len(valores), colunas):
            matriz_retorno.append(valores[i:i + colunas])
    else:
        raise TypeError(
            "Insira um tipo de valor valido. Inteiro/Float ou Lista de inteiros/floats.")
    return matriz_retorno


def print_matriz(mat: matriz) -> None:
    """'Desenha' uma `matriz` na tela no formato convencional
    
    Argumentos:
    ------
        `mat (matriz)`: uma matriz qualquer para ser printada
    """
    linhas = len(mat)
    colunas = len(mat[0])
    for i in range(linhas):
        for j in range(colunas):
            print(f"{mat[i][j]}", end="  ")
        print()


def pode_multiplicar(mat_a: matriz, mat_b: matriz) -> bool:
    """verifica se duas matrizes podem ser multiplicadas entre si, e na mesma ordem `mat_a x mat_b`. Para isso,
        retornar `True`, o número de colunas de `mat_a` deve ser igual ao numero de linhas de `mat_b`.
    
    Argumentos:
    --------
        mat_a (matriz): a primeira matriz (mais a esquerda)
        mat_b (matriz): a segunda matriz (mais a esquerda)
    
    Retornos:
    --------
        `bool`: True se pode multiplicar, caso contrario, False
    
    Exemplos:
    --------
    >>> pode_multiplicar([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    >>> output: True (2 == 2)
    |
    >>> pode_multiplicar([[1, 2], [3, 4]], [[1, 2], [3, 4], [1, 2]])
    >>> output: False (2 != 3)
    """
    colunas = len(mat_a[0])
    linhas = len(mat_b)
    return colunas == linhas


def multiplicar_matriz(mat_a: matriz, mat_b: matriz) -> Union[matriz, None]:
    """Cria um loop triplo para calcular o produto de duas matrizes, se possivel.
    Neste caso, a ordem importa.
    
    Argumentos:
    --------
        `mat_a (matriz)`: a primeira matriz a ser multiplicada (mais a esquerda)
        `mat_b (matriz)`: a segunda matriz a ser multiplicada (mais a direita)
    
    Retornos:
    --------
        `matriz`: uma matriz resultante da multiplicacao
        `None`: Caso nao seja possivel multiplicar as matrizes
    
    Exemplos:
    --------
    >>> multiplicar_matriz([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    >>> output: [[7, 10], [15, 22]]
    |
    >>> multiplicar_matriz([[1, 2], [3, 4]], [[1, 2], [3, 4], [1, 2]])
    >>> output: None
    """
    if not pode_multiplicar(mat_a, mat_b):
        print(
            f"Matrizes sao de tamanhos incompativeis, mat_a tem {len(mat_a[0])} colunas e a mat_b tem {len(mat_b)} linhas")
        return None
    linhas_a = len(mat_a)
    colunas_b = len(mat_b[0])
    mat_c = criar_matriz(linhas_a, colunas_b, 0)
    for i in range(len(mat_c)):
        for j in range(len(mat_c[0])):
            soma: int = 0
            for k in range(len(mat_a[0])):
                soma += mat_a[i][k] * mat_b[k][j]
            mat_c[i][j] = soma
    return mat_c

a = criar_matriz(3, 3, 0)
