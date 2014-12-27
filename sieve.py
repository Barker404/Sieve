import math

def sieve(max):
    # Values for 0 to max
    isPrime = [True] * (max + 1)
    # For clarity of indexing, the list includes 0 and 1
    # These are both not prime
    # We won't check them, so we set them initially
    isPrime[0] = False
    isPrime[1] = False
    
    # A number larger than the square root of the max will not be a factor of 
    # any number less than or equal to the max
    limit = int(math.floor(math.sqrt(max)))
    # 2 is first prime number
    # Stop when the last possible factor is passed
    for i in xrange(2, limit):
        if isPrime[i]:
            # Any number below the square would already be checked if not prime
            multiple = i * i
            # Do sieving for this prime
            # "Cross out" any multiple of it
            while multiple <= max:
                isPrime[multiple] = False
                multiple += i

    # Yield the actual values of the primes found
    for i, e in enumerate(isPrime):
        if e:
            yield i