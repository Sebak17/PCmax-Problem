from data_loader import Data_loader
from greedy_algorithm import Greedy_algorithm
from genetic_algorithm import Genetic_algorithm
from chart_generator import Chart_generator

data_loader = Data_loader()
greedy_algorithm = Greedy_algorithm()
genetic_algorithm = Genetic_algorithm()
chart_generator = Chart_generator()

if __name__ == "__main__":
	proces, nr_of_elements, tasks = data_loader.load("m50n200.txt")

	greedy_Tmax = greedy_algorithm.solve(proces, tasks)

	genetic_algorithm.start(proces, tasks)

	bestSpecimen = genetic_algorithm.find_best_specimen()

	chart_generator.generateChartComparingGenerationsWithGreedy(greedy_Tmax, genetic_algorithm.generation_best_Tmax)

	print("Greedy: ", greedy_Tmax)
	print("Genetic: ", bestSpecimen.id, " Tmax:", bestSpecimen.Tmax)