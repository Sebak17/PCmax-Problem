from greedy_algorithm import GreedyAlgorithm
from specimen import Specimen
from config import *

import random
import time

greedyAlgorithm = GreedyAlgorithm()


class GeneticAlgorithm:

	generation_best_Tmax = []

	generation = 0

	currentSpecimenId = 0
	currentGeneration = []

	def start(self, processors_size, tasks):

		self.generate_first_generation(tasks)

		self.solve_generation_tasks(processors_size)

		self.add_best_specimen_to_chart_data()

		if MAX_EXECUTION_TIME is not None:
			self.finalTime = time.time() + MAX_EXECUTION_TIME

		for i in range(0, GENERATIONS_AMOUNT - 1):
			if MAX_EXECUTION_TIME is not None and self.finalTime < time.time():
				break

			self.select_best_specimens()

			self.generate_next_generation()

			self.solve_generation_tasks(processors_size)

			if MUTATION_ENABLE and i % MUTATION_FREQUENCY:
				self.mutate_random_specimen()

			self.solve_generation_tasks(processors_size)

			self.add_best_specimen_to_chart_data()

	def reset(self):
		self.generation_best_Tmax = []
		self.generation = 0
		self.currentSpecimenId = 0
		self.currentGeneration = []

	def add_best_specimen_to_chart_data(self):
		self.generation_best_Tmax.append(self.find_best_specimen().Tmax)

	def generate_first_generation(self, tasks):
		specimen_tasks = tasks.copy()
		self.generation = 1

		for i in range(0, POPULATION_SIZE, 1):
			el1 = random.randrange(0, len(specimen_tasks))
			el2 = random.randrange(0, len(specimen_tasks))

			specimen_tasks[el1], specimen_tasks[el2] = specimen_tasks[el2], specimen_tasks[el1]

			self.currentGeneration.append(Specimen(self.currentSpecimenId, specimen_tasks.copy(), self.generation))
			self.currentSpecimenId += 1

	def solve_generation_tasks(self, processors_size):
		for specimen in self.currentGeneration:
			specimen.Tmax = greedyAlgorithm.solve(processors_size, specimen.tasks)

	def print_generation(self):
		print("==================[ GENERATION " + str(self.generation) + " ]==================")
		for specimen in self.currentGeneration:
			print("Specimen " + str(specimen.id) + ":", "Tmax: " + str(specimen.Tmax), specimen.tasks)
		print("====================================================")

	def select_best_specimens(self):
		t_max = []
		for specimen in self.currentGeneration:
			t_max.append(specimen.Tmax)

		for _ in range(0, int(POPULATION_SIZE / 2)):
			specimen_id = t_max.index(max(t_max))
			del self.currentGeneration[specimen_id]
			del t_max[specimen_id]

	def find_best_specimen(self):
		best_specimen = None

		for specimen in self.currentGeneration:
			if best_specimen is None:
				best_specimen = specimen
			elif best_specimen.Tmax > specimen.Tmax:
				best_specimen = specimen

		return best_specimen

	def find_worst_specimen(self):
		worst_specimen = None

		for specimen in self.currentGeneration:
			if worst_specimen is None:
				worst_specimen = specimen
			elif worst_specimen.Tmax < specimen.Tmax:
				worst_specimen = specimen

		return worst_specimen

	def generate_next_generation(self):
		next_generation = []
		self.generation += 1

		next_generation.append(self.find_best_specimen())

		missing_specimens = POPULATION_SIZE - 1

		while missing_specimens > 0:
			for first_specimen in self.currentGeneration:

				other_specimens = self.currentGeneration.copy()
				del other_specimens[other_specimens.index(first_specimen)]

				second_specimen = random.choice(other_specimens)

				next_specimen = self.cross_specimens(first_specimen, second_specimen)
				next_generation.append(next_specimen)

				missing_specimens -= 1

				if missing_specimens == 0:
					break

		self.currentGeneration = next_generation

	def cross_specimens(self, first_specimen, second_specimen):
		newTasksList = []

		if random.choice([True, False]):
			baseTasks = first_specimen.tasks.copy()
			secondaryTasks = second_specimen.tasks.copy()
		else:
			baseTasks = second_specimen.tasks.copy()
			secondaryTasks = first_specimen.tasks.copy()


		startTaskIndex = random.randint(0, (len(baseTasks) // 2) - 1)
		endTaskIndex = random.randint(startTaskIndex + 3, len(baseTasks))
		baseSelectedTasks = baseTasks[startTaskIndex:endTaskIndex]

		for task in baseSelectedTasks:
			del secondaryTasks[secondaryTasks.index(task)]
		random.shuffle(secondaryTasks)

		for i in range(0, len(baseTasks)):
			if i < startTaskIndex or i >= endTaskIndex:
				newTasksList.append(secondaryTasks[0])
				del secondaryTasks[0]
			else:
				newTasksList.append(baseSelectedTasks[0])
				del baseSelectedTasks[0]

		next_specimen = Specimen(self.currentSpecimenId, newTasksList, self.generation)
		self.currentSpecimenId += 1

		return next_specimen

	def mutate_random_specimen(self):
		best_specimen_tasks = self.find_best_specimen().tasks.copy()

		task1 = random.randint(0, len(best_specimen_tasks) - 1)
		task2 = task1
		while task1 == task2:
			task2 = random.randint(0, len(best_specimen_tasks) - 1)

		best_specimen_tasks[task1], best_specimen_tasks[task2] = best_specimen_tasks[task2], best_specimen_tasks[task1]

		worst_specimen = self.find_worst_specimen()
		worst_specimen.Tmax = None
		worst_specimen.tasks = best_specimen_tasks
