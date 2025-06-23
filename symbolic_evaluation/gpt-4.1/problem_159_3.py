import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate components for the current term
    pow_16 = 16 ** n
    fact_2n = mp.factorial(2 * n)
    gamma_num1 = mp.gamma(n/2 + mp.mpf('1.5'))  # Gamma(n/2 + 3/2)
    gamma_num2 = mp.gamma(n/2 + 1)             # Gamma(n/2 + 1)
    gamma_den = mp.gamma(n + mp.mpf('2.5'))    # Gamma(n + 5/2)
    
    # Compute current term in the series
    term = 8 * pow_16 / fact_2n * gamma_num1 * gamma_num2 / gamma_den
    
    # Add term to cumulative sum
    sum_result += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))