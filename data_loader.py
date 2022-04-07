class Data_loader:
	def load(self, fileName):
		f = open("data/" + fileName)
		data = f.read()
		data = data.split()
		data2 = []
		for i in data[2:]:
			data2.append(int(i))
		return int(data[0]), int(data[1]), data2
