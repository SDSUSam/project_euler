import numpy as np
from sympy import isprime

class Answer:

	def __init__(self):
		self.x=1

	def factor_it(self, num):
		"""
		Returns the prime factors of the given number

		Inputs: 
			- num ; is an integer you'd like to factor. 
		Outputs: 
			- array of factors of that number. No	
				particular order
		"""
	
		factors=[]
		i=1
	
		while i<num:
			if num%i==0:
				factors.append(i)
			i+=1
	
		return factors

	def prime_it(self, arr):
		"""
		Takes in the array of factors - recusively calls 
		the factor_it function until there are only primes 
		left in the array. 
		

		Inputs: 
			- Array of integers
		
		Outputs: 
			- Array of same integers and lists. The list 
				will contain prime factors itself. 
 		"""
	
		prime_factors=[]

		for i in range(len(arr)):
			if isprime(arr[i]):
				prime_factors[i]=arr[i]

		return prime_factors
				
