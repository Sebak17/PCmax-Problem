from greedy_algorithm import Greedy_algorithm
from specimen import Specimen
from config import *
import random

greedy_algorithm = Greedy_algorithm()

class Genetic_algorithm:

	generation = 0

	currentSpecimenId = 0
	currentGeneration = {}

	def start(self, processorsSize, tasks):

		self.generate_first_generation(tasks)

		self.solve_generation_tasks(processorsSize)

		self.print_generation()

		self.select_best_specimens()


	def generate_first_generation(self, tasks):
		specimenTasks = tasks.copy()

		for i in range(0, POPULATION_SIZE, 1):
			el1 = random.randrange(0, len(specimenTasks))
			el2 = random.randrange(0, len(specimenTasks))

			specimenTasks[el1], specimenTasks[el2] = specimenTasks[el2], specimenTasks[el1]

			self.currentGeneration[self.currentSpecimenId] = Specimen(self.currentSpecimenId, specimenTasks.copy())
			self.currentSpecimenId += 1

		self.generation = 1

	def solve_generation_tasks(self, processorsSize):
		for key, specimen in self.currentGeneration.items():
			specimen.Tmax = greedy_algorithm.solve(processorsSize, specimen.tasks)

	def print_generation(self):
		for key, specimen in self.currentGeneration.items():
			print("Specimen " + str(specimen.id) + ":", "Tmax: " + str(specimen.Tmax), specimen.tasks)

	def select_best_specimens(self):
		#print(self.currentGeneration)
		t_max = []
		for key, specimen in self.currentGeneration.items():
			t_max.append(specimen.Tmax)

		for i in range(0,3):
			maxx = max(t_max)
			index = t_max.index(maxx)
			#print(index)
			del self.currentGeneration[index]
			t_max[index] = 0

		self.print_generation()
			