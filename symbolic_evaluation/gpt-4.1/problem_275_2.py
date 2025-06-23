import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Define the constant factor outside the integral
constant = 6 * mp.sqrt(3)

# Initialize the sum for the series expansion of cosh
series_sum = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-25')  # Convergence tolerance

while True:
    # Calculate components of the nth term
    numerator = mp.power(6, 2 * n)
    factorial_denom = mp.fac(2 * n)
    gamma1 = mp.gamma(n + mp.mpf('1.5'))  # Gamma(n + 3/2)
    gamma2 = mp.gamma(n + 1)              # Gamma(n + 1)
    gamma3 = mp.gamma(2 * n + mp.mpf('2.5'))  # Gamma(2n + 5/2)
    
    # Compute the term using Beta function relation
    term = (numerator / factorial_denom) * 0.5 * gamma1 * gamma2 / gamma3
    
    # Add term to the series sum
    series_sum += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    n += 1

# Multiply by the constant factor to get final result
result = constant * series_sum

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))