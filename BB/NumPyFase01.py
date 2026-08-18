"""
FASE 1: CONSOLIDAÇÃO DE CONHECIMENTO BÁSICO
Tópicos: Reshape, Transpose e Funções de Agregação
"""

import numpy as np

print("=" * 60)
print("FASE 1: CONSOLIDANDO CONHECIMENTO BÁSICO")
print("=" * 60)

# ============================================================================
# 1. RESHAPE E TRANSPOSE - Alterar a forma dos arrays
# ============================================================================
print("\n1. RESHAPE - Mudando dimensões do array")
print("-" * 60)

# Criar um array 1D
arr_1d = np.arange(12)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(f"Array 1D: {arr_1d}")
print(f"Shape: {arr_1d.shape}")

# Reshape para 2D (3 linhas, 4 colunas)
arr_2d = arr_1d.reshape(3, 4)
print(f"\nArray 2D (3x4):\n{arr_2d}")
print(f"Shape: {arr_2d.shape}")

# Reshape para 3D (2 matrizes de 2x3)
arr_3d = arr_1d.reshape(2, 2, 3)
print(f"\nArray 3D (2x2x3):\n{arr_3d}")
print(f"Shape: {arr_3d.shape}")

# Reshape com -1 (NumPy calcula automaticamente)
arr_auto = arr_1d.reshape(4, -1)  # 4 linhas, NumPy calcula colunas
print(f"\nArray com reshape automático (4, -1):\n{arr_auto}")
print(f"Shape: {arr_auto.shape}")

# ============================================================================
print("\n2. FLATTEN E RAVEL - Converter para 1D")
print("-" * 60)

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matriz original:\n{matriz}")

# Flatten - cria uma cópia
flattened = matriz.flatten()
print(f"\nFlatten (cópia): {flattened}")

# Ravel - cria uma view (mais eficiente)
raveled = matriz.ravel()
print(f"Ravel (view): {raveled}")

# ============================================================================
print("\n3. TRANSPOSE - Transpor arrays")
print("-" * 60)

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matriz original (2x3):\n{matriz}")

transposta = matriz.T
print(f"\nMatriz transposta (3x2):\n{transposta}")

# Para arrays multidimensionais
arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"\nArray 3D original shape: {arr_3d.shape}")
transposta_3d = arr_3d.T
print(f"Array 3D transposto shape: {transposta_3d.shape}")

# ============================================================================
print("\n4. FUNÇÕES DE AGREGAÇÃO - Operações de resumo")
print("-" * 60)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Array: {arr}")

# Soma
print(f"\nSoma total: {np.sum(arr)}")
print(f"Método alternativo (arr.sum()): {arr.sum()}")

# Média
print(f"Média: {np.mean(arr)}")
print(f"Média com 2 casas decimais: {np.mean(arr):.2f}")

# Mínimo e Máximo
print(f"Mínimo: {np.min(arr)}")
print(f"Máximo: {np.max(arr)}")

# Desvio padrão
print(f"Desvio padrão: {np.std(arr):.4f}")

# Variância
print(f"Variância: {np.var(arr):.4f}")

# ============================================================================
print("\n5. AGREGAÇÃO COM EIXOS - Operações em dimensões específicas")
print("-" * 60)

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"Matriz:\n{matriz}")

# Soma por eixo 0 (colunas)
print(f"\nSoma por coluna (axis=0): {np.sum(matriz, axis=0)}")

# Soma por eixo 1 (linhas)
print(f"Soma por linha (axis=1): {np.sum(matriz, axis=1)}")

# Média por coluna
print(f"Média por coluna (axis=0): {np.mean(matriz, axis=0)}")

# Média por linha
print(f"Média por linha (axis=1): {np.mean(matriz, axis=1)}")

# ============================================================================
print("\n6. FUNÇÕES ÚTEIS DE AGREGAÇÃO")
print("-" * 60)

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print(f"Array: {arr}")

# Índice do máximo e mínimo
print(f"Índice do máximo: {np.argmax(arr)} (valor: {arr[np.argmax(arr)]})")
print(f"Índice do mínimo: {np.argmin(arr)} (valor: {arr[np.argmin(arr)]})")

# Produto (multiplicação de todos elementos)
print(f"Produto: {np.prod(arr)}")

# Mediana
print(f"Mediana: {np.median(arr)}")

# Percentil
print(f"25º percentil: {np.percentile(arr, 25)}")
print(f"75º percentil: {np.percentile(arr, 75)}")

# ============================================================================
print("\n7. PRÁTICA: DESAFIO DA FASE 1")
print("-" * 60)

# Crie uma matriz 4x5 com números de 1 a 20
dados = np.arange(1, 21).reshape(4, 5)
print(f"Matriz de dados (4x5):\n{dados}")

# Calcule:
print(f"\na) Soma total: {np.sum(dados)}")
print(f"b) Soma por linha: {np.sum(dados, axis=1)}")
print(f"c) Média por coluna: {np.mean(dados, axis=0)}")
print(f"d) Máximo em cada linha: {np.max(dados, axis=1)}")
print(f"e) Mínimo em cada coluna: {np.min(dados, axis=0)}")

# Reshapes
print(f"\nf) Transposta da matriz:\n{dados.T}")
print(f"g) Flatten (1D): {dados.flatten()}")

print("\n" + "=" * 60)
print("FIM DA FASE 1 - CONSOLIDAÇÃO")
print("=" * 60)

#============================================================================
#EXERCICIOS
#============================================================================
#exercicio 1 Reshape e Transpose 
print("\nExercício 1: Reshape e Transpose")

arr = np.arange(30) #cria um array de 0 a 29
print(f"Cria o array original\n(1d) que vai de 0 a 29: {arr}")

#a) reshape para(5, 6)
arr_reshaped_5x6= arr.reshape(5, 6)
print(f"\nReshape para (5, 6):\n{arr_reshaped_5x6}") #5 linhas e 6 colunas

#b) Reshape para (3, 2, 5) 
arr_reshaped_3x2x5 = arr.reshape(3, 2, 5)
print(f"\nReshape para (3, 2, 5):\n{arr_reshaped_3x2x5}") #3 matrizes de 2 linhas e 5 colunas

#c) Transpose da matriz 5x6
arr_transpose_5x6 = arr_reshaped_5x6.transpose()
print(f"\nTranspose da matriz (5, 6):\n{arr_transpose_5x6}") #6 linhas e 5 colunas

#exercicio 2 Funções de Agregação
print("\nExercício 2: Funções de Agregação")
vendas = np.array([
    [100, 120, 115, 130, 125, 140, 150],  # Loja A
    [110, 105, 120, 115, 130, 125, 140],  # Loja B
    [95, 110, 105, 120, 115, 130, 125],   # Loja C
    [130, 140, 135, 145, 150, 155, 160]   # Loja D
])
print("Vendas por loja (dias):\n", vendas)

#a) Total de vendas por loja (soma por linha)
total_vendas_loja = np.sum(vendas, axis=1)
print(f"\nTotal de vendas por loja (soma por linha): {total_vendas_loja}")

#b) Vendas médias por dia (média por coluna)
vendas_medias_dia = np.mean(vendas, axis=0)
print(f"\nVendas médias por dia (média por coluna): {vendas_medias_dia}")

#c) melhor dia de vendas (máximo por coluna)
melhor_dia = np.argmax(vendas, axis=0)
print(f"\nMelhor dia de vendas (índice): {melhor_dia} com {np.sum(vendas, axis=0)[melhor_dia]} vendas totais")

#d) pior dia de vendas (mínimo por coluna)
pior_dia = np.argmin(vendas, axis=0)
print(f"\nPior dia de vendas (índice): {pior_dia} com {np.sum(vendas, axis=0)[pior_dia]} vendas totais")

#e) loja com melhor desempenho (máximo por linha)
loja_melhor_desempenho = np.argmax(total_vendas_loja)
print(f"\nLoja com melhor desempenho (índice): {loja_melhor_desempenho} com {total_vendas_loja[loja_melhor_desempenho]} vendas totais")

#exercicio 3: Analise notas de estudantes
print("\nExercício 3: Análise de notas de estudantes")

# Notas de 5 estudantes em 4 disciplinas
notas = np.array([
    [8.5, 9.0, 7.5, 8.0],   # Estudante 1
    [7.0, 8.5, 9.0, 8.5],   # Estudante 2
    [9.0, 8.0, 8.5, 9.5],   # Estudante 3
    [6.5, 7.0, 7.5, 8.0],   # Estudante 4
    [8.0, 9.5, 9.0, 8.5]    # Estudante 5
])
print("Notas dos estudantes:\n", notas)

#a) Média por estudante (média por linha):
media_estudante = np.mean(notas, axis=1)
print(f"\nMédia por estudante (média por linha): {media_estudante}")

#b) Média por disciplina (média por coluna):
media_disciplina = np.mean(notas, axis=0)
print(f"\nMédia por disciplina (média por coluna): {media_disciplina}")

#c) Estudante com melhor média (máximo por linha): 
estudante_melhor_media = np.argmax(media_estudante)
print(f"\nEstudante com melhor média (índice): {estudante_melhor_media} com média {media_estudante[estudante_melhor_media]}")

#d) Disciplina mais difícil (mínimo por coluna):
disciplina_mais_dificil = np.argmin(media_disciplina)
print(f"\nDisciplina mais difícil (índice): {disciplina_mais_dificil} com média {media_disciplina[disciplina_mais_dificil]}")

