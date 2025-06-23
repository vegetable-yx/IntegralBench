import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Precompute the constant factor: sqrt(pi/2)
constant_factor = mp.sqrt(mp.pi / 2)

# Initialize the sum and set tolerance for convergence
series_sum = mp.mpf(0)
tol = mp.mpf('1e-15')  # Tolerance for breaking the loop
n = 0

# Sum the series until terms become negligible
while True:
    # Compute (-1)^n
    sign = mp.mpf(1) if n % 2 == 0 else mp.mpf(-1)
    
    # Compute factorial of (2n)
    fact = mp.factorial(2 * n)
    
    # Compute 4^n
    four_power = mp.power(4, n)
    
    # Compute denominator part: (n + 3/4)
    denom = n + mp.mpf('0.75')
    
    # Calculate the term: sign / (fact * four_power * denom)
    term = sign / (fact * four_power * denom)
    
    # Add term to the series sum
    series_sum += term
    
    # Check for convergence (absolute value of term < tolerance)
    if mp.fabs(term) < tol:
        break
    
    # Increment n for the next term
    n += 1

# Multiply the series sum by the constant factor
result = constant_factor * series_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))