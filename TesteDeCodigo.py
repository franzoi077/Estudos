import numpy as np

vendas = np.array([
    [100, 120, 115, 130, 125, 140, 150],  # Loja A
    [110, 105, 120, 115, 130, 125, 140],  # Loja B
    [95, 110, 105, 120, 115, 130, 125],   # Loja C
    [130, 140, 135, 145, 150, 155, 160]   # Loja D
])
total_vendas_loja = np.sum(vendas, axis=1)

loja_melhor_desempenho = np.argmax(total_vendas_loja)
print(f"\nLoja com melhor desempenho (índice): {loja_melhor_desempenho} com {total_vendas_loja[loja_melhor_desempenho]} vendas totais")