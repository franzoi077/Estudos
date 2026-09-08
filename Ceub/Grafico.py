import numpy as np
import matplotlib.pyplot as plt

# 1. Entrada dos Dados da Planilha 
tensao_V = np.array([2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0])
corrente_A = np.array([0.20, 0.40, 0.60, 0.80, 1.00, 1.20, 1.40, 1.60, 1.80, 2.00, 2.20, 2.40, 2.60, 2.80, 3.00])

# 2. Modelagem Matemática (Regressão Linear de 1º grau)
# O modelo busca y = ax + b, onde 'a' é o coeficiente angular
coef = np.polyfit(tensao_V, corrente_A, 1)
equacao_linear = np.poly1d(coef)

# 3. Criação do Gráfico
plt.figure(figsize=(10, 6))
plt.scatter(tensao_V, corrente_A, color='blue', label='Dados Medidos (PhET)')
plt.plot(tensao_V, equacao_linear(tensao_V), color='red', linestyle='--', label=f'Linha de Tendência: y = {coef[0]:.2f}x + {coef[1]:.2f}')

# Configurações de layout
plt.title('Análise da 1ª Lei de Ohm: Tensão vs. Corrente', fontsize=14)
plt.xlabel('Tensão da Bateria (V) - Variável Independente', fontsize=12)
plt.ylabel('Corrente Medida (A) - Variável Dependente', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Exibir a equação no terminal para o relatório
print(f"Equação gerada: I = {coef[0]:.2f} * V + {coef[1]:.2f}")

plt.show()