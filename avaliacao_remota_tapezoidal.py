def metodo_trapezios(f, a, b, n):
    """
    Realiza a integração numérica da função f utilizando o método dos trapézios.
    
    Args:
        f: Função a ser integrada.
        a: Limite inferior do intervalo de integração.
        b: Limite superior do intervalo de integração.
        n: Número de subintervalos para a discretização.
    
    Returns:
        Valor da integral de f no intervalo [a, b] utilizando o método dos trapézios.
    """
    h = (b - a) / n  # Tamanho de cada subintervalo
    soma = 0
    
    for i in range(1, n):
        xi = a + i * h  # Ponto xi dentro do subintervalo
        soma += f(xi)
    
    integral = h * (0.5 * (f(a) + f(b)) + soma)  # Valor da integral
    
    return integral

def f(x):
    return x**2  # Função a ser integrada

a = 0  # Limite inferior do intervalo de integração
b = 1  # Limite superior do intervalo de integração
n = 100  # Número de subintervalos

integral_trapezios = metodo_trapezios(f, a, b, n)
print("Integral pelo Método dos Trapézios:", integral_trapezios)
