from data_loader import Data_loader
from greedy_algorithm import Greedy_algorithm
from genetic_algorithm import Genetic_algorithm

data_loader = Data_loader()
greedy_algorithm = Greedy_algorithm()
genetic_algorithm = Genetic_algorithm()

if __name__ == "__main__":
	proces, nr_of_elements, tasks = data_loader.load("m50n200.txt")

	greedy_Tmax = greedy_algorithm.solve(proces, tasks)

	genetic_algorithm.start(proces, tasks)
