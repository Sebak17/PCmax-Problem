from data_loader import DataLoader
from greedy_algorithm import GreedyAlgorithm
from genetic_algorithm import GeneticAlgorithm
from chart_generator import ChartGenerator

dataLoader = DataLoader()
greedyAlgorithm = GreedyAlgorithm()
geneticAlgorithm = GeneticAlgorithm()
chartGenerator = ChartGenerator()

if __name__ == "__main__":
	fileData = dataLoader.load("m50n200.txt")

	greedy_Tmax = greedyAlgorithm.solve(fileData["processors"], fileData["tasks"])

	geneticAlgorithm.start(fileData["processors"], fileData["tasks"])
	bestSpecimen = geneticAlgorithm.find_best_specimen()

	print("Greedy: ", greedy_Tmax)
	print("Genetic: ", bestSpecimen.id, " Tmax:", bestSpecimen.Tmax, " Generation ", str(bestSpecimen.generation) + "/" + str(geneticAlgorithm.generation))

	chartGenerator.generate_chart_comparing_generations_with_greedy(greedy_Tmax, geneticAlgorithm.generation_best_Tmax)