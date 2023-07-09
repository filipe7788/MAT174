def interpolacao_newton(x, y, xi):
    """
    Realiza a interpolação de Newton para estimar o valor de f(xi) dado um conjunto de pontos (x, y).
    
    Args:
        x: Array contendo as coordenadas x dos pontos conhecidos.
        y: Array contendo as coordenadas y dos pontos conhecidos.
        xi: Valor de x para o qual se deseja estimar f(xi).
    
    Returns:
        Estimativa de f(xi) utilizando o método de interpolação de Newton.
    """
    n = len(x)  # Número de pontos conhecidos
    
    yi = 0  # Valor estimado de f(xi)
    coeficientes = [y[0]]  # Coeficientes do polinômio de Newton
    
    for i in range(1, n):
        # Calcula os coeficientes do polinômio de Newton utilizando as diferenças divididas
        tabela_diferencas = [[y[j] for j in range(i)]]
        
        for j in range(i):
            tabela_diferencas.append([])
            for k in range(i):
                tabela_diferencas[j+1].append((tabela_diferencas[j][k+1] - tabela_diferencas[j][k]) / (x[j+k+1] - x[k]))
        
        # Calcula o termo produtório (x - xi) do polinômio de Newton
        termo = 1
        for j in range(i):
            termo *= (xi - x[j])
        
        # Adiciona o termo produtório (x - xi) * f[x0, x1, ..., xi] à estimativa yi
        yi += coeficientes[-1] * termo
        coeficientes.append(tabela_diferencas[0][0])
    
    return yi

def f(x):
    return x**2  # Função para interpolar

# Pontos conhecidos
x = [0, 1, 2, 3]
y = [0, 1, 4, 9]

# Valor para interpolar
xi = 1.5

valor_estimado_newton = interpolacao_newton(x, y, xi)
print("Valor estimado pelo Método de Interpolação de Newton:", valor_estimado_newton)

