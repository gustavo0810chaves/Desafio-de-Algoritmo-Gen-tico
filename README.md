# Desafio-de-Algoritmo-Gen-tico
# Desafio-de-Algoritmo-Gen-tico
# Algoritmo Genético para Problema da Mochila
 
Este projeto implementa um algoritmo genético para resolver o problema da mochila, onde o objetivo é maximizar o valor total dos itens colocados na mochila sem exceder o peso máximo permitido.
 
## Descrição
 
O código utiliza um algoritmo genético para encontrar a melhor combinação de itens que podem ser colocados na mochila. O algoritmo passa por várias gerações, selecionando, cruzando e mutando soluções para encontrar a melhor solução possível.
 
## Requisitos
 
- Python 3.x
 
## Como Executar
 
1. Clone este repositório:
    ```bash
    git clone https://github.com/gustavo0810chaves/Desafio-de-Algoritmo-Gen-tico
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd seu-repositorio
    ```
3. Execute o script Python:
    ```bash
    python seu_script.py
    ```
 
## Estrutura do Código
 
- `fitness(solution, items, max_weight)`: Calcula o valor total e o peso total de uma solução.
- `create_population(size, num_items)`: Cria uma população inicial de soluções.
- `tournament_selection(population, fitnesses, k=3)`: Seleciona pais usando o método de torneio.
- `crossover(parent1, parent2)`: Realiza o cruzamento entre dois pais.
- `mutate(individual, mutation_rate=0.01)`: Aplica mutação a um indivíduo.
- `genetic_algorithm(items, max_weight, num_chromosomes, generations)`: Função principal que executa o algoritmo genético.
 
## Exemplo de Uso
 
Os dados de entrada são definidos como uma lista de pesos e valores dos itens, o peso máximo da mochila, o número de cromossomos e o número de gerações:
 
```python
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50
 
resultados = genetic_algorithm(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)
 
for valor, solucao in resultados:
    print(f"valor: {valor}, solução: {solucao}")
