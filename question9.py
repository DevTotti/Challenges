"""
NAME:   OSUNTOLU PAUL ADEDIRAN
EMAIL:  neptunecody@gmail.com
PHONE:  09025111684

Question B9 : Write a program to sum the first 50 Fibonacci sequence
"""
def fib(n):
	a, b = 0, 1
	while a < n:
		#print b,
		a, b = b, a+b
		sum = a + b
	print "The sum of the sequence is: %s" %sum

a = int(input("Enter the value here: "))
fib(a)
