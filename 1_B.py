# Joao felipe melo - ATIV ASL - Questao 1 B
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da onda de dente de serra
amplitude = 5  # Volts
frequencia_fundamental = 20  # Hz
periodo = 1 / frequencia_fundamental

# Tempo de amostragem
tempo_total = 5 * periodo  # Plote cinco ciclos
num_pontos = 1000
tempo = np.linspace(0, tempo_total, num_pontos)

# Gere a onda de dente de serra
onda_dente_de_serra = amplitude * (tempo % periodo)

# Plote a onda de dente de serra
plt.plot(tempo, onda_dente_de_serra)
plt.title("Onda de Dente de Serra")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
