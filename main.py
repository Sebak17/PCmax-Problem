from data_loader import Data_loader
from greedy_algorithm import Greedy_algorithm
from genetic_algorithm import Genetic_algorithm

data_loader = Data_loader()
greedy_algorithm = Greedy_algorithm()
genetic_algorithm = Genetic_algorithm()

if __name__ == "__main__":
	proces, nr_of_elements, tasks = data_loader.load("m10.txt")

	#Tmax = greedy_algorithm.solve(proces, data)

	proces = 3
	#tasks = [2, 4, 1, 2, 3, 3, 2, 2, 2, 2, 1, 6]
	tasks = [1,2,3,4,5,6,7,8,9,10]

	genetic_algorithm.start(proces, tasks)
