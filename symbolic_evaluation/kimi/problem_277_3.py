import mpmath as mp

mp.dps = 15  # Set internal precision

result = 0.0
n = 0
tolerance = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate components for each term in the series
    factorial_term = mp.fac(2*n)
    power_term = 2**(2*n + 2)
    gamma_numerator = mp.gamma(n + mp.mpf('1.5'))**2
    gamma_denominator = mp.gamma(2*n + 3)
    
    # Compute current term value
    term = (power_term * gamma_numerator) / (factorial_term * gamma_denominator)
    
    # Add term to cumulative result
    result += term
    
    # Check if term is below precision threshold
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))