import random


class DataGenerator:

	def generate_tasks(self, processors_size, tasks_size):
		tasks = []

		for _ in range(0, tasks_size):
			tasks.append(random.randint(0, 1000))

		'''
		f = open("data/m" + str(processors_size) + "n" + str(tasks_size) + "_t.txt", "w")
		f.write(str(processors_size) + "\n")
		f.write(str(tasks_size) + "\n")
		for task in tasks:
			f.write(str(task) + "\n")
		'''

		return {
			"processors": processors_size,
			"tasksSize": tasks_size,
			"tasks": tasks,
		}
