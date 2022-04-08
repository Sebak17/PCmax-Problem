from greedy_algorithm import Greedy_algorithm
from specimen import Specimen
from config import *
import random

greedy_algorithm = Greedy_algorithm()

class Genetic_algorithm:

	generation_best_Tmax = []

	generation = 0

	currentSpecimenId = 0
	currentGeneration = []

	def start(self, processorsSize, tasks):

		self.generate_first_generation(tasks)

		self.solve_generation_tasks(processorsSize)

		for i in range(0, GENERATIONS_AMOUNT):
			self.select_best_specimens()

			self.generate_next_generation()

			self.solve_generation_tasks(processorsSize)

			if MUTATION_ENABLE and i % MUTATION_FREQUENCY:
				self.mutate_random_specimen()

			self.solve_generation_tasks(processorsSize)

			self.generation_best_Tmax.append(self.find_best_specimen().Tmax)



		#self.print_generation()


	def generate_first_generation(self, tasks):
		specimenTasks = tasks.copy()

		for i in range(0, POPULATION_SIZE, 1):
			el1 = random.randrange(0, len(specimenTasks))
			el2 = random.randrange(0, len(specimenTasks))

			specimenTasks[el1], specimenTasks[el2] = specimenTasks[el2], specimenTasks[el1]

			self.currentGeneration.append(Specimen(self.currentSpecimenId, specimenTasks.copy()))
			self.currentSpecimenId += 1

		self.generation = 1

	def solve_generation_tasks(self, processorsSize):
		for specimen in self.currentGeneration:
			specimen.Tmax = greedy_algorithm.solve(processorsSize, specimen.tasks)

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
			specimenId = t_max.index(max(t_max))
			del self.currentGeneration[specimenId]
			del t_max[specimenId]



	def find_best_specimen(self):
		bestSpecimen = None

		for specimen in self.currentGeneration:
			if bestSpecimen is None:
				bestSpecimen = specimen
			elif bestSpecimen.Tmax > specimen.Tmax:
				bestSpecimen = specimen

		return bestSpecimen

	def find_worst_specimen(self):
		bestSpecimen = None

		for specimen in self.currentGeneration:
			if bestSpecimen is None:
				bestSpecimen = specimen
			elif bestSpecimen.Tmax < specimen.Tmax:
				bestSpecimen = specimen

		return bestSpecimen

	def generate_next_generation(self):
		nextGeneration = []
		self.generation += 1

		nextGeneration.append(self.find_best_specimen())

		missingSpecimens = POPULATION_SIZE - 1

		while missingSpecimens > 0:
			for firstSpecimen in self.currentGeneration:

				other_specimens = self.currentGeneration.copy()
				del other_specimens[other_specimens.index(firstSpecimen)]

				secondSpecimen = random.choice(other_specimens)

				nextSpecimen = self.cross_specimens(firstSpecimen, secondSpecimen)
				nextGeneration.append(nextSpecimen)

				missingSpecimens -= 1

				if missingSpecimens == 0:
					break


		self.currentGeneration = nextGeneration

	def cross_specimens(self, firstSpecimen, secondSpecimen):
		newTasksList = []

		if random.choice([True, False]):
			baseTasks = firstSpecimen.tasks.copy()
			secondaryTasks = secondSpecimen.tasks.copy()
		else:
			baseTasks = secondSpecimen.tasks.copy()
			secondaryTasks = firstSpecimen.tasks.copy()


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

		nextSpecimen = Specimen(self.currentSpecimenId, newTasksList)
		self.currentSpecimenId += 1

		return nextSpecimen

	def mutate_random_specimen(self):
		bestSpecimenTasks = self.find_best_specimen().tasks.copy()
		worstSpecimen = self.find_worst_specimen()

		task1 = random.randint(0, len(bestSpecimenTasks) - 1)
		task2 = task1
		while task1 == task2:
			task2 = random.randint(0, len(bestSpecimenTasks) - 1)

		bestSpecimenTasks[task1], bestSpecimenTasks[task2] = bestSpecimenTasks[task2], bestSpecimenTasks[task1]

		worstSpecimen.Tmax = None
		worstSpecimen.tasks = bestSpecimenTasks
