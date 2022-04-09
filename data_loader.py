class DataLoader:
	def load(self, file_name):
		file = open("data/" + file_name)
		file_content = file.read()
		data = file_content.split()
		tasks = []

		for i in data[2:]:
			tasks.append(int(i))

		return {
			"processors": int(data[0]),
			"tasksSize": int(data[1]),
			"tasks": tasks,
		}
