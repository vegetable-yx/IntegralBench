import mpmath as mp

mp.dps = 15  # Set internal precision for calculations

sum_total = mp.mpf(0)  # Initialize sum for the series
n = 0
tolerance = mp.mpf('1e-15')  # Stopping criterion for term magnitude

while True:
    # Calculate 36^n component
    power_36 = mp.power(36, n)
    
    # Compute factorial term (2n)!
    factorial_2n = mp.fac(2 * n)
    
    # Calculate Gamma(n + 3/2) using mpmath's gamma function
    gamma_n_plus_3half = mp.gamma(n + mp.mpf('3/2'))
    
    # Calculate Gamma(n + 1) which equals n! for integer n
    gamma_n_plus_1 = mp.gamma(n + 1)
    
    # Calculate Gamma(2n + 5/2)
    gamma_2n_plus_5half = mp.gamma(2 * n + mp.mpf('5/2'))
    
    # Compute current term using the formula components
    term = power_36 / factorial_2n
    term *= gamma_n_plus_3half * gamma_n_plus_1
    term /= gamma_2n_plus_5half
    
    sum_total += term  # Add term to cumulative sum
    
    # Break loop if term magnitude drops below precision threshold
    if mp.fabs(term) < tolerance:
        break
    
    n += 1  # Increment series index

# Multiply accumulated sum by 3*sqrt(3) for final result
result = 3 * mp.sqrt(3) * sum_total

# Print result with exactly 10 decimal places using mpmath's nstr
print(mp.nstr(result, n=10))