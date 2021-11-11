#%%
#? Uma matriz é uma lista de listas que contem inteiros ou floats
matriz = list[list[int | float]]

def criar_matriz(linhas: int, colunas: int, valores: list[int | float] or int) -> matriz:
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
        # items: list[int] = []
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


def multiplicar_matriz(mat_a: matriz, mat_b: matriz) -> matriz | None:
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


def matriz_transposta(mat_a: matriz) -> matriz:
    """Calcula a transposta de uma matriz.
    
    Argumentos:
    --------
        `mat_a (matriz)`: uma matriz qualquer
    
    Retornos:
    --------
        `matriz`: a matriz transposta
    
    Exemplos:
    --------
    >>> matriz_transposta([[1, 2], [3, 4]])
    >>> output: [[1, 3], [2, 4]]
    """
    matriz_retorno: matriz = []
    for i in range(len(mat_a[0])):
        matriz_retorno.append([])
        for j in range(len(mat_a)):
            matriz_retorno[i].append(mat_a[j][i])
    return matriz_retorno


def determinante_matriz(mat_a: matriz) -> float:
    """Calcula o determinante de uma matriz. Usa uma funcao recursiva até achar uma matriz 2x2
    
    Argumentos:
    --------
        `mat_a (matriz)`: uma matriz qualquer
    
    Retornos:
    --------
        `float`: o determinante da matriz
    
    Exemplos:
    --------
    >>> determinante_matriz([[1, 2], [3, 4]])
    >>> output: -2
    --------
    >>> determinante_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> output: 0
    --------
    >>> determinante_matriz([[1, 3, 1, 4], [3, 9, 5, 15], [0, 2, 1, 1], [0, 4, 2, 3]])
    >>> output: -4
    """
    #? checking if its a valid and square matrix
    if not isinstance(mat_a, list):
        raise TypeError("Insira uma matriz.")
    if len(mat_a) != len(mat_a[0]):
        raise ValueError("Matriz nao e quadrada")
    
    #? break case for the recursion
    if len(mat_a) == 2:
        return mat_a[0][0] * mat_a[1][1] - mat_a[0][1] * mat_a[1][0]
    
    #? if the matrix is a 1x1, return the value
    if len(mat_a) == 1 and len(mat_a[0]) == 1:
        return mat_a[0][0]
    
    soma: float = 0
    for i in range(len(mat_a)):
        soma += (-1)**i * mat_a[0][i] * determinante_matriz(matriz_submatriz_det(mat_a, i))
    return soma


def matriz_submatriz_det(mat_a: matriz, coluna: int) -> matriz:
    """Usado internamente pela funcao determinante_matriz(). Dado uma matriz `n` x `n`, retorna uma matriz `n-1` x `n-1`
    onde se remove a linha e a coluna do valor de `matriz[0][coluna]`
    
    Argumentos:
    --------
    mat_a (matriz): uma matriz qualquer, deve ser `n` x `n`
    coluna (int): a coluna em que se encontra o valor a ser removido
    
    Retornos:
    --------
        matriz: retorna uma matriz `n-1` x `n-1`
    
    Exemplos:
    --------
    >>> matriz_submatriz_det([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0)
    >>> output: [[5, 6], [8, 9]]
    --------
    >>> matriz_submatriz_det([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
    >>> output: [[1, 3], [7, 9]]
    """
    matriz_retorno: matriz = []
    for linha in mat_a[1:]:
        matriz_retorno.append([])
        for val, col in enumerate(linha):
            if val != coluna:
                matriz_retorno[-1].append(col)
    return matriz_retorno
