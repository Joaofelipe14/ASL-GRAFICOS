# Joao felipe melo - ATIV ASL - Questao 1 A 
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da onda quadrada
amplitude = 5
frequencia_fundamental = 20  # Hz
ciclo_de_trabalho = 0.6
periodo = 1 / frequencia_fundamental

# Tempo de amostragem
tempo_total = 5 * periodo  # Plote cinco ciclos
num_pontos = 1000
tempo = np.linspace(0, tempo_total, num_pontos)

# Gere a onda quadrada
onda_quadrada = amplitude * np.where(np.mod(tempo, periodo) < ciclo_de_trabalho * periodo, 1, -1)

# Plote a onda quadrada
plt.plot(tempo, onda_quadrada)
plt.title("Onda Quadrada")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
