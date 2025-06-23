import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)
n = 0

while True:
    # Calculate each component of the term
    exponent = 16 ** n  # 2^(4n) = 16^n
    gamma_term1 = mp.gamma(n + mp.mpf('3/4'))  # Gamma(n + 3/4)
    gamma_term2 = mp.gamma(n + mp.mpf('1/4'))  # Gamma(n + 1/4)
    factorial_denom = mp.factorial(2 * n) ** 2  # (2n)! squared
    
    # Compute the current term
    term = (exponent * gamma_term1 * gamma_term2) / factorial_denom
    sum_result += term
    
    # Check if the term is smaller than 1e-15 to ensure convergence
    if mp.fabs(term) < 1e-15:
        break
    
    n += 1

# Print the result to 10 decimal places
print(mp.nstr(sum_result, n=10))