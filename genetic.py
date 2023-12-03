# Genetic Algorithm

# gene -> (client,server) ; client-index , server-value ; 
# 4- attributes: {client capacity, MIPS, current server load, maximum server capacity}
#data-type : 

# chromosome -> set of genes ;                           data-type : 

# population -> set of chromosomes                        data-type :

# No of servers, no. of clients
# initialize population
# Find fitness value for all the chromosomes in the population
# Select 2 at random and cross-over to produce a child
# check if the child has better fitness or not -> if yes the add it to population -> else add initial child
# return the chromosome with best fitness value



import random

# Define the number of chromosomes
num_chromosomes = 10  # You can change this value as needed

# Initialize an array to store chromosomes
population = []

# Define the number of genes in each chromosome
num_genes = 5  # You can change this value as needed

# Function to generate a random gene
def generate_gene():
    client_load = random.randint(0, 100)  # integer
    mips = random.uniform(100, 1000)
    current_server_load = random.randint(0, 50)  # integer
    max_server_load = random.randint(50, 100)  # integer
    client_id = random.randint(0, 10)  # integer
    server_id = random.randint(0, 10)  # integer
    return [client_id, server_id, client_load, mips, current_server_load, max_server_load]

# Function to generate a random chromosome
def generate_chromosome(num_genes):
    return [generate_gene() for _ in range(num_genes)]

# Create and append chromosomes to the array
for _ in range(num_chromosomes):
    chromosome = generate_chromosome(num_genes)
    population.append(chromosome)

# Print the array of chromosomes
for i, chromosome in enumerate(population, start=1):
    print(f"Chromosome {i}: {chromosome}")
