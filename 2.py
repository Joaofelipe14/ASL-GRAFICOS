# Joao felipe melo - ATIV ASL - Questao 2 
import numpy as np
import matplotlib.pyplot as plt

# Definindo tempos para a plotagem
tempos_plotagem = np.arange(0, 5.5, 0.5)  # Valores de tempo de 0 a 5 segundos com incremento de 0.5 segundos

# Calculando x(t) para os tempos de plotagem
x_t = 10 * np.exp(-tempos_plotagem) - 5 * np.exp(-0.5 * tempos_plotagem)

# Plotando x(t) em relação ao tempo (t)
plt.plot(tempos_plotagem, x_t, marker='o', linestyle='-')
plt.title("Solução da Equação Diferencial")
plt.xlabel("Tempo (s)")
plt.ylabel("x(t)")
plt.grid(True)

# Definindo rótulos personalizados do eixo x
eixo_x = [str(tempo) for tempo in tempos_plotagem]
plt.xticks(tempos_plotagem, eixo_x)

# Posicionando o rótulo do eixo x abaixo
plt.gca().xaxis.set_label_coords(0.5, -0.1)

# Exibindo o gráfico
plt.show()
