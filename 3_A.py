# Joao felipe melo - ATIV ASL - Questao 3 A
import numpy as np
import matplotlib.pyplot as plt

# Respostas ao impulso dos sistemas h1[n] e h2[n]
h1 = [1/4 if 0 <= n <= 3 else 0 for n in range(20)]
h2 = [1/4 if n in [0, 2] else -1/4 if n in [1, 3] else 0 for n in range(20)]

# Cálculo das respostas ao degrau dos sistemas
y1 = np.cumsum(h1)
y2 = np.cumsum(h2)

# Array de tempo para plotagem
n = np.arange(20)

# Plotagem da resposta ao degrau do sistema h1[n]
plt.figure(figsize=(10, 6))
plt.stem(n, y1, basefmt='b-', label='Sistema h1[n]')
plt.title('Resposta ao Degrau do Sistema h1[n]')
plt.xlabel('n')
plt.ylabel('y1[n]')
plt.legend()
plt.grid(True)
plt.show()

# Plotagem da resposta ao degrau do sistema h2[n]
plt.figure(figsize=(10, 6))
plt.stem(n, y2, basefmt='b-', label='Sistema h2[n]')
plt.title('Resposta ao Degrau do Sistema h2[n]')
plt.xlabel('n')
plt.ylabel('y2[n]')
plt.legend()
plt.grid(True)
plt.show()
