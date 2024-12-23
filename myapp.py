def find_primes(n):
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
   
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    
    return [num for num in range(2, n + 1) if is_prime[num]]


def main():
    limit = 50
    primes = find_primes(limit)
    print(f"Prime numbers up to {limit}:")

    
    # Additional demonstration of prime number properties
    print(f"\nTotal number of primes found: {len(primes)}")
    print(f"Largest prime found: {primes[-1]}")

if __name__ == "__main__":
    main()
