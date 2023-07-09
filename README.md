# Meus Algoritmos Numéricos

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Bem-vindo ao Repositório de Algoritmos Numéricos!

Este repositório contém implementações em Python de algoritmos numéricos comumente utilizados para resolver problemas matemáticos e computacionais. Os algoritmos visam oferecer soluções eficientes e precisas para uma variedade de problemas.

Os algoritmos incluídos são:

- **Interpolação**: Interpolação de Lagrange e Interpolação de Newton.
- **Integração Numérica**: Método dos Trapézios e Método 1/3 de Simpson.
- **Eliminação de Gauss**: Gauss-Jacobi e Gauss-Seidel.
- **Método Numérico**: Método de Euler.

Cada algoritmo possui uma explicação detalhada e exemplos de uso em seus respectivos arquivos. Além disso, você encontrará um conjunto de funções e utilitários auxiliares para facilitar o uso dos algoritmos.

## Como Utilizar

1. Certifique-se de ter o Python instalado em seu sistema. Você pode verificar se o Python está instalado executando o seguinte comando no terminal ou prompt de comando:
   
 ```shell
   python --version
 ```

Se o comando for reconhecido e exibir a versão do Python, significa que o Python está instalado corretamente. Caso contrário, você precisará instalar o Python em seu sistema antes de prosseguir.

2. Verifique se você tem o **pip** instalado em seu sistema. O pip é um gerenciador de pacotes para instalar bibliotecas e dependências do Python. Para verificar se o pip está instalado, execute o seguinte comando:

 ```shell
   pip --version
 ```

Se o comando for reconhecido e exibir a versão do pip, significa que o pip está instalado corretamente. Caso contrário, você precisará instalar o pip em seu sistema. Consulte a documentação oficial do Python para obter instruções sobre como instalar o pip.

3. Instale a biblioteca **NumPy** utilizando o seguinte comando:

 ```shell
   pip install numpy
 ```

O pip instalará o NumPy e suas dependências automaticamente.

4. Escolha o algoritmo que deseja utilizar e acesse o respectivo arquivo.
5. Siga as instruções fornecidas para fornecer os dados de entrada necessários.
6. Execute o código em Python.
7. Verifique os resultados e adapte o código conforme necessário para atender às suas necessidades específicas.
   
# Interpolação

#### [Interpolação de Lagrange](https://en.wikipedia.org/wiki/Lagrange_polynomial)

A interpolação de Lagrange é um método utilizado para estimar o valor de uma função em um ponto não conhecido com base em um conjunto de pontos conhecidos. O método utiliza um polinômio interpolador que passa por todos os pontos conhecidos. O polinômio é construído multiplicando cada ponto conhecido por um polinômio de base Lagrange que é calculado com base nos demais pontos conhecidos.

O algoritmo da Interpolação de Lagrange consiste em:

1. Receber como entrada os pontos conhecidos (x, y) e o ponto para o qual se deseja estimar o valor da função (xi).
2. Inicializar a variável `yi` como zero, que será o valor estimado de f(xi).
3. Para cada ponto conhecido, fazer o seguinte:
   - Inicializar a variável `Li` como 1, que será o polinômio de base Lagrange para o ponto atual.
   - Para cada outro ponto conhecido, fazer o seguinte:
     - Se o ponto atual não for o mesmo ponto que está sendo iterado, calcular o termo `Li` multiplicando-o pelo polinômio de base Lagrange correspondente.
   - Atualizar `yi` somando o produto do valor de `Li` pelo valor de `y` do ponto atual.
4. Retornar o valor estimado `yi`.

A Interpolação de Lagrange é um método simples e direto para interpolação polinomial. No entanto, à medida que o número de pontos conhecidos aumenta, o cálculo do polinômio de Lagrange pode se tornar computacionalmente custoso.

#### [Interpolação de Newton](https://en.wikipedia.org/wiki/Newton_polynomial)

A interpolação de Newton é outro método utilizado para estimar o valor de uma função em um ponto não conhecido com base em um conjunto de pontos conhecidos. O método utiliza um polinômio interpolador que passa por todos os pontos conhecidos. O polinômio é construído utilizando diferenças divididas que são calculadas a partir dos pontos conhecidos.

O algoritmo da Interpolação de Newton consiste em:

1. Receber como entrada os pontos conhecidos (x, y) e o ponto para o qual se deseja estimar o valor da função (xi).
2. Inicializar a variável `yi` como zero, que será o valor estimado de f(xi).
3. Inicializar a lista de coeficientes `coeficientes` com o valor `y` do primeiro ponto conhecido.
4. Para cada ponto conhecido, exceto o primeiro, fazer o seguinte:
   - Inicializar a tabela de diferenças divididas `tabela_diferencas` com o valor `y` do ponto atual.
   - Para cada nível da tabela de diferenças divididas, fazer o seguinte:
     - Calcular as diferenças divididas para cada par de pontos conhecidos adjacentes.
   - Adicionar o valor da primeira linha e coluna da tabela de diferenças divididas à lista de coeficientes.
5. Para cada ponto conhecido, fazer o seguinte:
   - Inicializar a variável `termo` como 1, que será o produtório de (xi - x) para cada ponto conhecido anterior.
   - Atualizar `yi` somando o produto do valor de `termo` pelo valor do coeficiente correspondente.
6. Retornar o valor estimado `yi`.

A Interpolação de Newton é mais eficiente computacionalmente do que a Interpolação de Lagrange, pois calcula as diferenças divididas uma vez e reutiliza-as para estimar os valores em diferentes pontos. Além disso, é possível adicionar pontos extras à interpolação sem recalcular todos os coeficientes.

# Integração Numérica

#### [Método dos Trapézios](https://en.wikipedia.org/wiki/Trapezoidal_rule)

O Método dos Trapézios é um método numérico utilizado para estimar a integral de uma função em um intervalo [a, b]. O método divide o intervalo em subintervalos de tamanho igual e aproxima a área sob a curva em cada subintervalo por um trapézio.

O algoritmo do Método dos Trapézios consiste em:

1. Receber como entrada a função `f` a ser integrada, os limites do intervalo [a, b] e o número de subintervalos `n`.
2. Calcular o tamanho de cada subintervalo `h` através da fórmula `h = (b - a) / n`.
3. Inicializar a variável `soma` como zero.
4. Para cada subintervalo, exceto o primeiro e o último, fazer o seguinte:
   - Calcular o ponto `xi` dentro do subintervalo através da fórmula `xi = a + i * h`.
   - Somar à variável `soma` o valor da função `f(xi)`.
5. Calcular o valor da integral através da fórmula `integral = h * (0.5 * (f(a) + f(b)) + soma)`.
6. Retornar o valor da integral.

O Método dos Trapézios é uma abordagem simples para estimar a integral de uma função, onde a função é aproximada por segmentos retos. Quanto maior o número de subintervalos,mais precisa é a estimativa da integral.

#### [Método 1/3 de Simpson](https://en.wikipedia.org/wiki/Simpson%27s_rule)

O Método 1/3 de Simpson é outro método numérico utilizado para estimar a integral de uma função em um intervalo [a, b]. O método divide o intervalo em subintervalos de tamanho igual e aproxima a área sob a curva em cada subintervalo por uma curva quadrática.

O algoritmo do Método 1/3 de Simpson consiste em:

1. Receber como entrada a função `f` a ser integrada, os limites do intervalo [a, b] e o número de subintervalos `n` (que deve ser um múltiplo de 2).
2. Verificar se o número de subintervalos é par. Caso contrário, lançar um erro.
3. Calcular o tamanho de cada subintervalo `h` através da fórmula `h = (b - a) / n`.
4. Inicializar a variável `soma` como zero.
5. Para cada par de subintervalos, fazer o seguinte:
   - Calcular os pontos `xi` e `xi+1` dentro do par de subintervalos através das fórmulas `xi = a + i * h` e `xi+1 = a + (i + 1) * h`.
   - Calcular a estimativa da integral para o par de subintervalos através da fórmula `integral_par = (h / 6) * (f(xi) + 4 * f((xi + xi+1) / 2) + f(xi+1))`.
   - Somar à variável `soma` o valor da estimativa da integral para o par de subintervalos.
6. Retornar o valor da soma.

O Método 1/3 de Simpson é uma abordagem mais precisa do que o Método dos Trapézios para estimar a integral de uma função. Ele utiliza curvas quadráticas para aproximar a função, o que resulta em uma melhor precisão.

# Eliminação de Gauss

#### [Gauss-Jacobi](https://en.wikipedia.org/wiki/Gauss%E2%80%93Jacobi_method)

O Método de Gauss-Jacobi é um método iterativo utilizado para resolver sistemas lineares. Ele parte da matriz de coeficientes e do vetor de termos independentes do sistema e itera até encontrar uma solução aproximada. O método é baseado na decomposição da matriz de coeficientes em uma matriz diagonal e uma matriz fora da diagonal.

O algoritmo do Gauss-Jacobi consiste em:

1. Receber como entrada a matriz de coeficientes `A`, o vetor de termos independentes `b`, a tolerância `tol` e o número máximo de iterações `max_iter`.
2. Inicializar o vetor de soluções `x` como um vetor de zeros.
3. Para cada iteração, fazer o seguinte:
   - Para cada equação do sistema, fazer o seguinte:
     - Calcular a soma dos produtos dos coeficientes pelos valores das soluções anteriores (exceto o coeficiente correspondente à variável atual).
     - Calcular a nova estimativa da variável utilizando a fórmula `(b[i] - soma_termos) / A[i][i]`.
   - Verificar a condição de convergência comparando a norma do vetor de diferenças entre as soluções atuais e as soluções anteriores com a tolerância.
     - Se a condição de convergência for satisfeita, retornar as soluções estimadas.
   - Atualizar o vetor de soluções com as novas estimativas para a próxima iteração.
4. Se o método não convergir para uma solução, retornar `None`.

#### [Gauss-Seidel](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method)

O Método de Gauss-Seidel também é um método iterativo utilizado para resolver sistemas lineares. Ele é uma melhoria em relação ao Método de Gauss-Jacobi, pois utiliza as soluções atualizadas imediatamente após serem calculadas, ao invés de esperar o final da iteração para atualizá-las. Isso permite que as soluções convirjam mais rapidamente.

O algoritmo do Gauss-Seidel é semelhante ao do Gauss-Jacobi, mas com uma alteração no cálculo das soluções. Em vez de utilizar as soluções anteriores, ele utiliza as soluções atualizadas imediatamente.

O Método de Gauss-Seidel melhora a convergência em relação ao Método de Gauss-Jacobi, pois utiliza as soluções atualizadas imediatamente. Isso reduz o número de iterações necessárias para atingir a solução aproximada.

# Método Numérico de Euler

#### [Método de Euler](https://en.wikipedia.org/wiki/Euler_method)

O Método de Euler é um método numérico utilizado para resolver equações diferenciais ordinárias (EDOs) de primeira ordem. Ele aproxima a solução da EDO por meio de uma série de passos discretos ao longo do intervalo desejado.

O algoritmo do Método de Euler consiste em:

1. Receber como entrada a função derivada `f`, o valor inicial `y0` da solução da EDO, o valor inicial `x0` do intervalo, o valor final `xf` do intervalo e o tamanho do passo `h`.
2. Inicializar as variáveis `x` e `y` com os valores iniciais `x0` e `y0`, respectivamente.
3. Enquanto `x` for menor ou igual a `xf`, fazer o seguinte:
   - Calcular o próximo valor de `y` utilizando a fórmula `y = y + h * f(x, y)`.
   - Incrementar `x` pelo tamanho do passo `h`.
4. Retornar o valor final de `y`.

O Método de Euler é uma abordagem simples para resolver EDOs de primeira ordem, mas pode ter uma precisão limitada, especialmente para EDOs com curvas complexas ou sensíveis a pequenas variações no intervalo.

## Contribuição

Se você gostaria de contribuir para este repositório, sinta-se à vontade para abrir uma issue ou enviar um pull request. Ficarei feliz em revisar e incorporar suas contribuições.

## Licença

Este repositório é licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

