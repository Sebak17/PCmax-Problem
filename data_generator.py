import random


class DataGenerator:

	def generate_tasks(self, processors_size, tasks_size):
		tasks = []

		for _ in range(0, tasks_size):
			tasks.append(random.randint(0, 1000))

		return {
			"processors": processors_size,
			"tasksSize": tasks_size,
			"tasks": tasks,
		}
