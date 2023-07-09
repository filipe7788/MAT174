import numpy as np

def gauss_jacobi(A, b, tol, max_iter):
    n = len(b)
    x = np.zeros(n)  # Vetor inicial de soluções
    x_novo = np.zeros(n)  # Vetor para armazenar as novas soluções a cada iteração

    for _ in range(max_iter):
        for i in range(n):
            soma_termos = 0
            for j in range(n):
                if j != i:
                    soma_termos += A[i][j] * x[j]  # Calcula a soma dos termos que não envolvem a variável atual
            x_novo[i] = (b[i] - soma_termos) / A[i][i]  # Atualiza a variável com a nova solução estimada
        
        if np.linalg.norm(x_novo - x) < tol:  # Verifica a convergência comparando a norma do vetor de diferenças com a tolerância
            return x_novo  # Retorna as soluções estimadas
        
        x = x_novo.copy()  # Atualiza o vetor de soluções para a próxima iteração
    
    return None  # Retorna None se o método não convergir para uma solução


A = np.array([[4, 1, -1], [2, 7, 1], [1, -3, 12]])  # Matriz dos coeficientes
b = np.array([3, 19, 31])  # Vetor de termos independentes
tol = 1e-6  # Tolerância para critério de convergência
max_iter = 100  # Número máximo de iterações

posto_A = np.linalg.matrix_rank(A)  # Calcula o posto da matriz dos coeficientes A
posto_A_ext = np.linalg.matrix_rank(np.column_stack((A, b)))  # Calcula o posto da matriz estendida [A | b]

if posto_A == posto_A_ext == A.shape[0]:  # Verifica se o sistema possui solução única
    solucao = gauss_jacobi(A, b, tol, max_iter)  # Executa o Método de Gauss-Jacobi para obter as soluções
    if solucao is not None:
        print("Solução única encontrada pelo Método de Gauss-Jacobi:", solucao)
    else:
        print("O Método de Gauss-Jacobi não convergiu para a solução.")
else:
    print("O sistema não possui solução única.")
