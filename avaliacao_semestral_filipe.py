def metodo_euler(f, y0, h, n):
    # Inicializa os arrays para armazenar os pontos discretos
    x = [0] * (n + 1)
    y = [0] * (n + 1)

    # Define as condições iniciais
    x[0] = 0
    y[0] = y0

    # Aplica o método de Euler iterativamente
    for i in range(n):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h * f(x[i], y[i])

    return x, y


# Função para a qual queremos calcular a solução aproximada
def f(x, y):
    return x * y  # Exemplo: y' = x * y

# Entradas fornecidas pelo usuário
y0 = float(input("Digite o valor de y(x0): "))  # Condição inicial y(x0)
h = float(input("Digite o valor de h (espaçamento entre x): "))  # Tamanho do passo
n = int(input("Digite o número de subintervalos (n): "))  # Número de subintervalos

# Chama a função do método de Euler
x_vals, y_vals = metodo_euler(f, y0, h, n)

# Imprime os resultados
print("Pontos discretos (x, y):")
for i in range(len(x_vals)):
    print(f"({x_vals[i]}, {y_vals[i]})")
