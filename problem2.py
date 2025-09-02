import numpy as np

class Answer:

	def __init__(self):
		self.x=0

	def fib(self):
		"""
		Creates the sequence of fibonnaci numbers less than 4 million
		"""

		fib_list=[1,2]
		i=2
		while fib_list[len(fib_list)-1]<4000000:
			fib_list.append(fib_list[i-2]+fib_list[i-1])
			i+=1	
		return fib_list

	def even_sum(self,arr):
		"""
		This should calculate the sum of even fibonacci values
		"""
		
		total=0
		
		# Totals the even values in the array

		for i in range (len(arr)):
			if arr[i]%2==0:
				total+=arr[i]
		
		return total
