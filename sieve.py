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
    limit = math.sqrt(max)
    # 2 is first prime number
    currentPrime = 2
    # Stop when the lsat possible factor is passed
    while currentPrime <= limit:
        # Any number below the square would already be checked if not prime
        multiple = currentPrime * currentPrime
        # Do sieving for this prime
        # "Cross out" any multiple of it
        while multiple <= max:
            primes[multiple] = False
            multiple += currentPrime
        # Get the next prime to sieve with
        # The next number not "crossed out"
        currentPrime += 1
        while (primes[currentPrime] == False and 
            currentPrime <= limit):
            currentPrime += 1

    # Yield the actual values of the primes found
    for i, e in enumerate(primes):
        if e:
            yield i   
