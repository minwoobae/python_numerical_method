# Numerical Analysis Library - pynumerical.py
# Date: Sep/29/2015
# Author: Minwoo Bae
import math

def nevilles_method(x0, x, y):

	n = len(x)

	# Create and initiate an n x n multidimentional array: 
	q = [ [ 0 for i in range(n) ] for j in range(n) ]

	# Set y[i] value into q[i][0]:
	for i in range(n):
		q[i][0] = y[i]
	
	for i in range(1, n):
		for j in range(1, i):
			q[i][j] = ((x0 - x[i - j])*(q[i][j - 1]) - (x0 - x[i])*(q[i - 1][j - 1]))/(x[i] - x[i - j])

	print("Result of Neville's Method:\n");
	for i in range(n):
		for j in range(n):
			print("%.4f" %q[i][j])
		print("\n")