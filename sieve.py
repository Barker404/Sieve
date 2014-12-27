import math


def sieve(max):
    # Values for 0 to max
    primes = [True] * (max + 1)
    # For clarity of indexing, the list includes 0 and 1
    # These are both not prime
    # We won't check them, so we set them initially
    primes[0] = False
    primes[1] = False
    
    # A number larger than the square root of the max will not be a factor of 
    # any number less than or equal to the max
    limit = int(math.floor(math.sqrt(max)))
    print limit
    # 2 is first prime number
    # Stop when the last possible factor is passed
    for i in xrange(2, limit):
        isPrime = primes[i]
        if isPrime:
            # Any number below the square would already be checked if not prime
            multiple = i * i
            # Do sieving for this prime
            # "Cross out" any multiple of it
            while multiple <= max:
                primes[multiple] = False
                multiple += i

    # Yield the actual values of the primes found
    for i, e in enumerate(primes):
        if e:
            yield i   

p = []
for i in sieve(10000000):
    p.append[i]