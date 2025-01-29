import numpy as np
import matplotlib.pyplot as plt

def simulacao_sistema(derivadas, condicoes_iniciais, t_final, dt=0.01):
    """
    Simula um sistema de equações diferenciais de primeira ordem.
    
    Parâmetros:
    derivadas - Função que recebe (t, estado) e retorna a derivada do estado.
    condicoes_iniciais - Lista com os valores iniciais das variáveis de estado.
    t_final - Tempo final da simulação (s).
    dt - Passo de tempo (s) (default: 0.01).
    """
    
    # Definir tempo de simulação
    n_steps = int(t_final / dt)
    t_vals = np.linspace(0, t_final, n_steps)
    estado_vals = np.zeros((n_steps, len(condicoes_iniciais)))
    
    # Condições iniciais
    estado_vals[0] = condicoes_iniciais
    
    # Loop de integração numérica (Euler)
    for i in range(n_steps - 1):
        estado_vals[i + 1] = estado_vals[i] + np.array(derivadas(t_vals[i], estado_vals[i])) * dt
    
    return t_vals, estado_vals

def oscilador_harmonico(t, estado):
    """
    Define as equações diferenciais para o problema do oscilador harmônico simples.
    """
    x, v = estado
    k = 1.0  # Constante da mola (N/m)
    m = 1.0  # Massa (kg)
    return [v, -k/m * x]

def solucao_analitica_oscilador(t, x0, v0, k, m):
    """
    Retorna a solução analítica do oscilador harmônico simples.
    """
    omega = np.sqrt(k / m)
    return x0 * np.cos(omega * t) + (v0 / omega) * np.sin(omega * t)

def plot_comparacao(t, estado_vals, x_analitico):
    """
    Plota a comparação entre a solução numérica e analítica.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(t, estado_vals[:, 0], '--', label="Solução Numérica (Posição)", linewidth=2)
    plt.plot(t, x_analitico, label="Solução Analítica (Posição)", linewidth=2)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (m)")
    plt.title("Oscilador Harmônico: Solução Analítica vs. Numérica")
    plt.legend()
    plt.grid()
    plt.show()

# Parâmetros iniciais
x0 = 1.0  # Posição inicial (m)
v0 = 0.0  # Velocidade inicial (m/s)
k = 1.0   # Constante da mola (N/m)
m = 1.0   # Massa (kg)
t_final = 10.0  # Tempo total de simulação (s)

t_vals, estado_vals = simulacao_sistema(oscilador_harmonico, [x0, v0], t_final)

# Solução analítica
x_analitico = solucao_analitica_oscilador(t_vals, x0, v0, k, m)

# Plotagem da comparação
plot_comparacao(t_vals, estado_vals, x_analitico)
