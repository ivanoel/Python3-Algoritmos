#!/usr/bin/python3
'__autor__'=='__Ivanoel__'

def fibonacci(n):
	if n <= 1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)
fibonacci(7)
