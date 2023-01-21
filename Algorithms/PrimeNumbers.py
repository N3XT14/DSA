#Facts:
# 2 is the only even prime. 2 and 3 are the only consective prime numbers.
# Every prime can be written in form(except 2 and 3 and n is natural number): 6b+1 or 6b-1
# Goldbach Conjecture: Every even integer can be expressed as sum of two primes.
# Wilson's Theorem: (p-1)!%p = (p-1)
# Prime Factorization:  logN (base=2)
# sqrt technique is used to reduce the range of lookup because if any of the factors is greater than the sqrt of the number factored then it won't fullfil the product condition. Eg. a=b*c. If either b or c is greater than the sqrt of a then the equation a=b*c does not satisfy.

def isprimeSqrt(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
#(sqrt(N))
# print(isprimeSqrt(2))

limit = (10**9)+7
prime = [True]*limit
def SieveOfEratosthenes():
    p = 2

    while (p*p <= limit):
        if prime[p]:
            for i in range(p*p, limit+1, p):
                prime[i] = False
        p += 1

# SieveOfEratosthenes()
# print(prime[5])

import math
prime = []
def simpleSieve(limit):
	
	mark = [True for i in range(limit + 1)]
	p = 2
	while (p * p <= limit):				
		if (mark[p] == True):						
			for i in range(p * p, limit + 1, p):
				mark[i] = False
		p += 1
		
	for p in range(2, limit):
		if mark[p]:
			prime.append(p)

def segmentedSieve(l,r):
    #Generate list of primes using seive method upto sqrt of the larger number.
    limit = int(math.floor(math.sqrt(r)) + 1)
    simpleSieve(limit)
    
    #Create dummy array for the range of numbers from which prime one's need to be found, marking initially all as True.
    mark = [True for i in range(r - l + 1)]

    #Iterate over list of primes found by Sieve Method and mark all multiples as False.
    for i in range(len(prime)):
        #Find the first multiplier of each prime value w.r.t the lower value
        loLim = int(math.floor(l / prime[i]) * prime[i])
        #eg. 110/2 = 55 * 2 = 110, thus 2 is the lowest factor
        #eg. 110/3 = 36 * 3 = 108, 3 is not the factor of 108 thus add prime to it i.e 108 + 3 = 111 for which 3 is the lowest factor
        if loLim < l:            
            loLim += prime[i]
        #Once found first multiplier mark all multipliers as False.
        for j in range(loLim, r+1, prime[i]):
                mark[j - l] = False
    
    for i in range(l,r+1):
            if mark[i - l]:
                print(i, end = " ")
segmentedSieve(110,130)
