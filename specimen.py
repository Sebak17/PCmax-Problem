class Specimen:
	id = None
	tasks = None
	generation = None
	Tmax = None

	def __init__(self, id, tasks, generation):
		self.id = id
		self.tasks = tasks
		self.generation = generation
