def metodo_simpson(f, a, b, n):
    """
    Realiza a integração numérica da função f utilizando o método 1/3 de Simpson.
    
    Args:
        f: Função a ser integrada.
        a: Limite inferior do intervalo de integração.
        b: Limite superior do intervalo de integração.
        n: Número de subintervalos para a discretização (deve ser um múltiplo de 2).
    
    Returns:
        Valor da integral de f no intervalo [a, b] utilizando o método 1/3 de Simpson.
    """
    if n % 2 != 0:
        raise ValueError("O número de subintervalos (n) deve ser um múltiplo de 2.")
    
    h = (b - a) / n  # Tamanho de cada subintervalo
    soma = f(a) + f(b)
    
    for i in range(1, n):
        xi = a + i * h  # Ponto xi dentro do subintervalo
        if i % 2 == 0:
            soma += 2 * f(xi)
        else:
            soma += 4 * f(xi)
    
    integral = h * soma / 3  # Valor da integral
    
    return integral

def f(x):
    return x**2  # Função a ser integrada

a = 0  # Limite inferior do intervalo de integração
b = 1  # Limite superior do intervalo de integração
n = 100  # Número de subintervalos (deve ser um múltiplo de 2)

integral_simpson = metodo_simpson(f, a, b, n)
print("Integral pelo Método 1/3 de Simpson:", integral_simpson)
