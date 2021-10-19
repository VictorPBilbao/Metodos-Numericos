# %% [markdown]
#  # <div style="text-align:center; color:yellow;">Exercício: multiplação de matrizes A<sub>(K x L)</sub> <var>x</var> B<sub>(M x N)</sub></div>
#  ## Usar matriz como lista de listas e implementar funcoes para:
#  <input type="checkbox" id="do1">Criar
#
#  <input type="checkbox" id="do2">Multiplicar
#
#  <input type="checkbox" id="do3">Ler
#
#  <input type="checkbox" id="do4">Imprimir
#
# </br>
#
#  ## **Passos**:
#
#  <br/>
#
#  > 1. Pergunta linha de A(k) e coluna de A(l)
#  > 2. Pergunta linha de B(m) e coluna de B(n)
#  > 3. Se pode multiplicar:
#  >>        3.1 ler matriz A
#  >>        3.2 ler matriz B
#  >>        3.3 calcular C(loop triplo)
#  >>        3.4 mostrar A, B e C
#
# </br>
#
#  [![Dot Product](https://i.ibb.co/r5CX7x4/Dot-Product-Defintion.png "Produto de uma matriz A por B")](https://en.wikipedia.org/wiki/Matrix_multiplication)

# %%
#* Definir o que significa uma matriz:
#* Uma lista de listas com numero/s dentro, nao eh obrigatorio mas ajuda na leitura
matriz = list[list[int or float]]


# %%
def criar_matriz(linhas: int, colunas: int, valores: list[int or float] or int) -> matriz:
    """Cria uma matriz de linhas x colunas
    
    Args:
        linhas (int): quantas linhas a matriz tera
        colunas (int): quantas colunas a matriz tera
        valores (list[int|float] | int): Valor(es) com que a matriz sera preenchida. Se for apenas um numero, ele sera usado em toda a matriz.
    
    Returns:
        matriz: retorna uma matriz feita
    """
    matriz_retorno: matriz = []
    if type(valores) in [int, float]:  # ? se o tipo de valor for inteiro ou float
        for _ in range(linhas):
            items: list[int] = []
            for _ in range(colunas):
                items.append(valores)
            matriz_retorno.append(items)
    elif type(valores) == list and all(isinstance(x, (int, float)) for x in valores):
        if linhas * colunas != len(valores):
            raise ValueError(
                f"Tamanho da lista deve ser de {linhas * colunas} (linhas x colunas), nao de {len(valores)}")
        for i in range(0, len(valores), colunas):
            matriz_retorno.append(valores[i:i + colunas])
    else:
        raise TypeError("Insira um tipo de valor valido. Inteiro ou Lista de inteiros.")
    return matriz_retorno


# %%
def print_matriz(mat: matriz) -> None:
    """'Desenha' a matriz na tela no formato convencional
    
    Args:
        mat (matriz): uma matriz qualquer para ser printada
    """
    linhas = len(mat)
    colunas = len(mat[0])
    for i in range(linhas):
        for j in range(colunas):
            print(f"{mat[i][j]}", end="  ")
        print()


# %%
def pode_multiplicar(mat_a: matriz, mat_b: matriz) -> bool:
    """verifica se duas matrizes podem ser multiplicadas entre si, e na mesma ordem A x b
    
    Args:
        mat_a (matriz): a primeira matriz (mais a esquerda)
        mat_b (matriz): a segunda matriz (mais a esquerda)
    
    Returns:
        bool: True se pode multiplicar, caso contrario, False
    """
    colunas = len(mat_a[0])
    linhas = len(mat_b)
    return colunas == linhas

# %% [markdown]
#  # Nao esquecer que:
#  [![Loops](https://preview.redd.it/bffwlmuzcur71.jpg?width=960&crop=smart&auto=webp&s=51f3a79fdb1446bff3bf2c6f699970e50aab9501 "O que eh uma somatoria em programacao")](https://www.reddit.com/r/ProgrammerHumor/comments/q2lsax/dont_be_scared_math_and_computing_are_friends/)
#
#  <hr/>
#
#  ##  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Em python teremos:
#
#  |  Summation</br>(Capital Sigma)  | <p style="font-size:x-large;">$\sum _{n=0}^4 3 n$</p> | `sum = 0`</br>`for n in range(0, 5, 1):`</br>&emsp;&emsp;`sum += 3 * n` |
#  |:--:|:-----:|-----|
#  | Product</br>(Capital Pi) |    <p style="font-size:x-large;">$\prod _{n=1}^4 2 n$</p>  | `prod = 1`</br>`for n in range(1, 5, 1):`</br>&emsp;&emsp;`prod *= 2 * n` |

# %%
def multiplicar_matriz(mat_a: matriz, mat_b: matriz) -> matriz or None:
    """cria um loop triplo para calcular o produto de duas matrizes, se possivel.
    Neste caso, a ordem importa
    
    Args:
        mat_a (matriz): a primeira matriz a ser multiplicada (mais a esquerda)
        mat_b (matriz): a segunda matriz a ser multiplicada (mais a direita)
    
    Returns:
        matriz: uma matriz resultante da multiplicacao
        None: Caso nao seja possivel multiplicar as matrizes
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
