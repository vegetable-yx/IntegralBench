import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_total = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Tolerance for convergence check

while True:
    # Calculate components for the current term
    pow_4n = mp.power(4, n)
    gamma_n_plus_3_2 = mp.gamma(n + mp.mpf('3/2'))
    gamma_n_plus_1_2 = mp.gamma(n + mp.mpf('1/2'))
    factorial_2n = mp.factorial(2 * n)
    gamma_2n_plus_2 = mp.gamma(2 * n + 2)  # Equivalent to (2n+1)!
    
    # Compute current term value
    numerator = pow_4n * gamma_n_plus_3_2 * gamma_n_plus_1_2
    denominator = factorial_2n * gamma_2n_plus_2
    term = numerator / denominator
    
    # Add term to cumulative sum
    sum_total += term
    
    # Check if term is below precision threshold
    if mp.fabs(term) < tolerance:
        break
    n += 1

# Multiply by 2 as per the original formula
result = 2 * sum_total

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))