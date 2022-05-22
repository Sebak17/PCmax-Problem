from threading import Thread
from genetic_algorithm import GeneticAlgorithm
from data_loader import DataLoader


class SolverThread:
	filename = ""
	threadsAmount = 0
	threadExec = 0

	threads = []
	results = []

	def __init__(self, filename, threadsAmount, threadExec):
		self.filename = filename
		self.threadsAmount = threadsAmount
		self.threadExec = threadExec

		self.dataLoader = DataLoader()

	def start(self):
		for id in range(0, self.threadsAmount):
			thread = Thread(target=self.start_thread, args=(id,))
			thread.start()

			self.threads.append(thread)

		while any(thread.is_alive() for thread in self.threads):
			pass

		print("# ")
		print("# Lowest value = " + str(min(self.results)))
		print("# ")

	def start_thread(self, threadId):
		geneticAlgorithm = GeneticAlgorithm()

		for _ in range(0, self.threadExec):
			self.solve(threadId, geneticAlgorithm)
			geneticAlgorithm.reset()

	def solve(self, threadId, geneticAlgorithm):
		app_data = self.dataLoader.load(self.filename)

		geneticAlgorithm.start(app_data["processors"], app_data["tasks"])
		best_specimen = geneticAlgorithm.find_best_specimen()

		self.results.append(best_specimen.Tmax)

		print(
			"[Thrad-" + str(threadId) + "]" +
			"  Tmax:   " + str(best_specimen.Tmax) +
			"  Generation " + str(best_specimen.generation) + "/" + str(geneticAlgorithm.generation),
			flush=True
		)
