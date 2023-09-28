# Joao felipe melo - ATIV ASL - Questao 3 B
import numpy as np
import matplotlib.pyplot as plt

# Definindo a entrada x[n] = (0.9)^n * u[n] para n de 0 a 19
entrada_x = [(0.9**n) if n >= 0 else 0 for n in range(20)]

# Respostas ao impulso dos sistemas h1[n] e h2[n]
h1 = [1/4 if 0 <= n <= 3 else 0 for n in range(20)]
h2 = [1/4 if n in [0, 2] else -1/4 if n in [1, 3] else 0 for n in range(20)]

# Convolução da entrada x[n] com as respostas ao impulso h1[n] e h2[n]
y1 = np.convolve(entrada_x, h1, mode='full')[:20]  
y2 = np.convolve(entrada_x, h2, mode='full')[:20]  

# Array de tempo para plotagem
n = np.arange(20)

# Plotagem da saída para o sistema h1[n]
plt.figure(figsize=(1, 10))
plt.stem(n, y1, basefmt='b-', label='Sistema h1[n]')
plt.title('Saída do Sistema h1[n] para x[n]')
plt.xlabel('n')
plt.ylabel('y1[n]')
plt.legend()
plt.grid(True)

# Plotagem da saída para o sistema h2[n]
plt.figure(figsize=(10, 6))
plt.stem(n, y2, basefmt='b-', label='Sistema h2[n]')
plt.title('Saída do Sistema h2[n] para x[n]')
plt.xlabel('n')
plt.ylabel('y2[n]')
plt.legend()
plt.grid(True)

plt.show()
