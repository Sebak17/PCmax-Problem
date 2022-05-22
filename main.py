from data_loader import DataLoader
from data_generator import DataGenerator
from greedy_algorithm import GreedyAlgorithm
from genetic_algorithm import GeneticAlgorithm
from chart_generator import ChartGenerator
from solver_thread import SolverThread

dataLoader = DataLoader()
dataGenerator = DataGenerator()
greedyAlgorithm = GreedyAlgorithm()
chartGenerator = ChartGenerator()

def check_random_data(processors, tasks_amounts):
	geneticAlgorithm = GeneticAlgorithm()

	chart_data = []
	for tasksAmount in tasks_amounts:
		print("[" + str(tasksAmount) + "] Generating data...")
		app_data = dataGenerator.generate_tasks(processors, tasksAmount)

		print("[" + str(tasksAmount) + "] Solving...")
		greedy_Tmax = greedyAlgorithm.solve(app_data["processors"], app_data["tasks"])

		geneticAlgorithm.reset()
		geneticAlgorithm.start(app_data["processors"], app_data["tasks"])

		chart_data.append({
			"tasks_amount": tasksAmount,
			"greedy": greedy_Tmax,
			"genetic": geneticAlgorithm.find_best_specimen().Tmax,
		})
		print("[" + str(tasksAmount) + "] Done.")

	chartGenerator.generate_chart_random_data(processors, chart_data)


def check_file_data(geneticAlgorithm, filename, fullReport=True):
	if geneticAlgorithm is None:
		geneticAlgorithm = GeneticAlgorithm()

	app_data = dataLoader.load(filename)

	if fullReport:
		greedy_Tmax = greedyAlgorithm.solve(app_data["processors"], app_data["tasks"])
		print("Greedy: ", greedy_Tmax)

	geneticAlgorithm.start(app_data["processors"], app_data["tasks"])
	best_specimen = geneticAlgorithm.find_best_specimen()

	print("Tmax:   ", best_specimen.Tmax, " Generation ", str(best_specimen.generation) + "/" + str(geneticAlgorithm.generation))

	if fullReport:
		chartGenerator.generate_chart_comparing_generations_with_greedy(greedy_Tmax, geneticAlgorithm.generation_best_Tmax)


if __name__ == "__main__":
	# check_file_data(None, "m25.txt")
	# check_random_data(40, [200, 400, 600, 800, 1000])
	# check_file_data_multiple("m25.txt", 5, 5)
	SolverThread("m25.txt", 5, 5).start()

	pass
