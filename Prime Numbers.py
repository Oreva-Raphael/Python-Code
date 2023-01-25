def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true.
    # A value in prime[i] will finally be
    # false if i is Not a prime, else true.
    prime = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
 
        # If prime[p] is not changed, then it is
        # a prime
        if prime[p]:
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    return [p for p in range(2, n) if prime[p]]

print(sieve_of_eratosthenes(100000))
# This function uses the Sieve of Eratosthenes algorithm to generate the list of prime numbers. 
#It has a time complexity of O(n * log(log(n)))
#so it should be relatively fast for generating a list of primes up to 100000





#APPLY THE TRIAL DIVISION METHOD
def trial_division(n):
    # Create a list to store the prime numbers
    primes = []
    # Iterate through all the numbers from 2 to n
    for i in range(2, n+1):
        # Assume that the number is prime
        is_prime = True
        # Check if the number is divisible by any of the prime numbers that we have found so far
        for prime in primes:
            # If the number is divisible, then it is not prime
            if i % prime == 0:
                is_prime = False
                break
        # If the number is prime, add it to the list of prime numbers
        if is_prime:
            primes.append(i)
    return primes

print(trial_division(100000))

