import mpmath as mp

mp.dps = 15  # Set internal precision

sum_series = mp.mpf(0)
n = 0
epsilon = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate numerator (n + 1)
    numerator = n + 1
    
    # Calculate denominator components
    factorial_n = mp.factorial(n)
    gamma_term = mp.gamma(n + mp.mpf('5/2'))  # Gamma(n + 5/2)
    denominator = factorial_n * (2 * n + 3) * gamma_term
    
    # Compute current term
    term = numerator / denominator
    sum_series += term
    
    # Check for convergence
    if mp.fabs(term) < epsilon:
        break
    
    n += 1

# Multiply sum by sqrt(pi)/2 to get final result
result = (mp.sqrt(mp.pi) / 2) * sum_series

# Print result with 10 decimal places
print(mp.nstr(result, n=10))