import matplotlib.pyplot as plt
import numpy as np


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

	def generate_chart_random_data(self, procesors, data):
		labels = []
		greedy = []
		genetic = []
		for el in data:
			labels.append(el['tasks_amount'])
			greedy.append(el['greedy'])
			genetic.append(el['genetic'])

		x = np.arange(len(labels))
		width = 0.35

		fig, ax = plt.subplots()
		rects1 = ax.bar(x - width / 2, greedy, width, label='zachłanny', color='blue')
		rects2 = ax.bar(x + width / 2, genetic, width, label='genetyczny', color='green')

		ax.set_ylabel('Tmax')
		ax.set_title('Porównanie algorytmów\n zachłannego i genetycznego\n dla ' + str(procesors) + ' procesorów')
		ax.set_xticks(x, labels)
		ax.legend()

		ax.bar_label(rects1, padding=3)
		ax.bar_label(rects2, padding=3)

		fig.tight_layout()
		plt.savefig('results/random-data.png')
		plt.show()
