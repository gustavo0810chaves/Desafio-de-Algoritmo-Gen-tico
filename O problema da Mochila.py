import random
 
# Função para calcular o valor total e o peso total de uma solução
def fitness(solution, items, max_weight):
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_value += items[i][1]
            total_weight += items[i][0]
    if total_weight > max_weight:
        return 0  # Penalidade para soluções que excedem o peso máximo
    return total_value
 
# Função para criar uma população inicial
def create_population(size, num_items):
    return [[random.randint(0, 1) for _ in range(num_items)] for _ in range(size)]
 
# Função para selecionar pais usando torneio
def tournament_selection(population, fitnesses, k=3):
    selected = random.sample(list(zip(population, fitnesses)), k)
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]
 
# Função para cruzamento (crossover) de dois pais
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]
 
# Função para mutação de um indivíduo
def mutate(individual, mutation_rate=0.01):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
 
# Função principal do algoritmo genético
def genetic_algorithm(items, max_weight, num_chromosomes, generations):
    population = create_population(num_chromosomes, len(items))
    best_solutions = []
 
    for generation in range(generations):
        fitnesses = [fitness(individual, items, max_weight) for individual in population]
        new_population = []
 
        for _ in range(num_chromosomes // 2):
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
 
        population = new_population
        best_solution = max(population, key=lambda x: fitness(x, items, max_weight))
        best_solutions.append((fitness(best_solution, items, max_weight), best_solution))
 
    return best_solutions
 
# Dados de entrada
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50
 
# Executar o algoritmo genético
resultados = genetic_algorithm(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)
 
# Exibir os resultados
for valor, solucao in resultados:
    print(f"Valor: {valor}, Solução: {solucao}")