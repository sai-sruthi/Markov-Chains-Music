import random

class MarkovChainBuilder:
	def __init__(self, list_of_values):
		self._added_values = 0
		self._lookup_reverse_value_ = list_of_values
		self._lookup_value = {}
		for i in range(0, len(list_of_values)):
			self._lookup_value[list_of_values[i]] = i
		#for i in range(0, len(list_of_values)):
		#	for x in range(0, len(list_of_values)):
		#		self._matrix = 0
		self._matrix=[[0 for x in range(0,len(list_of_values))] for i in range(0,len(list_of_values))]

	def add(self, value_from, value_to):
		value = self._lookup_value
		self._matrix[value[value_from]][value[value_to]] += 1
		self._added_values += 1

	def value_next(self, value_from):
		value = self._lookup_value[value_from]
		counts_of_value = self._matrix[value]
		index_of_value = self.choose_at_random(counts_of_value)
		return self._lookup_reverse_value_[index_of_value]

	def choose_at_random(self, choice_counts):
		counted_sum = 0
		count_sum = sum(choice_counts)
		select_count = random.randrange(1, count_sum+1)
		for i in range(0, len(choice_counts)):
			counted_sum += choice_counts[i]
			if (counted_sum >= select_count):
				return i
