import math

def isPrime(n):
	if (n == 0 or n == 1):
		print("No")
		return

	m = int(math.ceil(n**(0.5)))

	for i in range(2, m+1):
		if(n % i == 0):
			print("No")
			return

	print("Yes")

n = int(raw_input())
isPrime(n)