import matplotlib.pyplot as plt


class ChartGenerator:

	def generate_chart_comparing_generations_with_greedy(self, greedy_Tmax, generations_data_Tmax):
		greedy_Tmax_list = []
		for i in range(0, len(generations_data_Tmax)):
			greedy_Tmax_list.append(greedy_Tmax)

		plt.figure(figsize=(10, 7))

		x1 = range(0, len(generations_data_Tmax))
		y1 = greedy_Tmax_list
		y2 = generations_data_Tmax

		plt.plot(x1, y1, label="zachłanny")
		plt.plot(x1, y2, label="genetyczny")

		plt.xlabel('Numer generacji')
		plt.ylabel('Tmax')
		plt.title('Porównanie algorytmów\n zachłannego i genetycznego\n w zależności od pokolenia')

		plt.legend()
		plt.savefig('results/greedy-generation-comparison.png')
		plt.show()
