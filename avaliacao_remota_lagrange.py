def interpolacao_lagrange(x, y, xi):
    """
    Realiza a interpolação de Lagrange para estimar o valor de f(xi) dado um conjunto de pontos (x, y).
    
    Args:
        x: Array contendo as coordenadas x dos pontos conhecidos.
        y: Array contendo as coordenadas y dos pontos conhecidos.
        xi: Valor de x para o qual se deseja estimar f(xi).
    
    Returns:
        Estimativa de f(xi) utilizando o método de interpolação de Lagrange.
    """
    n = len(x)  # Número de pontos conhecidos
    
    yi = 0  # Valor estimado de f(xi)
    
    for i in range(n):
        # Calcula o termo Li(x) do polinômio de Lagrange
        Li = 1
        for j in range(n):
            if j != i:
                Li *= (xi - x[j]) / (x[i] - x[j])
        
        # Adiciona o termo Li(x) * f(xi) à estimativa yi
        yi += Li * y[i]
    
    return yi


def f(x):
    return x**2  # Função para interpolar

# Pontos conhecidos
x = [0, 1, 2, 3]
y = [0, 1, 4, 9]

# Valor para interpolar
xi = 1.5

valor_estimado_lagrange = interpolacao_lagrange(x, y, xi)
print("Valor estimado pelo Método de Interpolação de Lagrange:", valor_estimado_lagrange)
