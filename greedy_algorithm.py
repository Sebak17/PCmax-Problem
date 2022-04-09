class GreedyAlgorithm:
	def solve(self, processorsSize, tasks):
		processors = {}

		for i in range(0, processorsSize, 1):
			processors[i] = 0

		for task in tasks:
			procId = min(processors, key=processors.get)
			processors[procId] += task

		return max(processors.values())