import numpy as np
import matplotlib.pyplot as plt

# Definição da função de velocidade v(t)
def v(t):
    return 24*t - t**2 + 5*np.sqrt(t)

# Solução analítica do deslocamento s(t)
def s_analitico(t):
    return 12*t**2 - (t**3)/3 + (10/3) * t**(3/2)

# Parâmetros da simulação numérica
dt = 0.01  # Passo de tempo
t_vals = np.arange(0, 10 + dt, dt)  # Intervalo de tempo de 0 a 10 segundos
s_numerico = np.zeros_like(t_vals)  # Inicialização do deslocamento numérico

# Método de Euler para calcular s(t) numericamente
for i in range(len(t_vals) - 1):
    s_numerico[i + 1] = s_numerico[i] + v(t_vals[i]) * dt

# Calculando a solução analítica
s_analitico_vals = s_analitico(t_vals)

# Plotando os resultados
plt.figure(figsize=(10, 5))
plt.plot(t_vals, s_analitico_vals, label="Solução Analítica", linewidth=2)
plt.plot(t_vals, s_numerico, '--', label="Solução Numérica (Euler)", linewidth=2)
plt.xlabel("Tempo (s)")
plt.ylabel("Deslocamento (pés)")
plt.title(f"Deslocamento do Carro Elétrico: Solução Analítica vs. Numérica para t = {dt}")
plt.legend()
plt.grid()
plt.show()
