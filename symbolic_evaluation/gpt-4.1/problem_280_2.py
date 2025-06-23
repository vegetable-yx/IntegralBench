import mpmath as mp

mp.dps = 15

sum_terms = mp.mpf(0)
epsilon = mp.mpf('1e-30')
n = 0

while True:
    # Calculate 12^n using mpmath power for precision
    pow_12n = mp.power(12, n)
    
    # Compute factorial of 2n
    factorial_2n = mp.factorial(2 * n)
    
    # Calculate Gamma(n + 3/4) and square it
    gamma_n_34 = mp.gamma(n + mp.mpf('3/4'))
    gamma_sq = gamma_n_34 ** 2
    
    # Calculate Gamma(2n + 3/2)
    gamma_2n_32 = mp.gamma(2 * n + mp.mpf('3/2'))
    
    # Compute current term in the series
    term = (pow_12n / factorial_2n) * (gamma_sq / gamma_2n_32)
    
    # Add term to cumulative sum
    sum_terms += term
    
    # Break loop if term magnitude drops below threshold
    if mp.fabs(term) < epsilon:
        break
    
    n += 1

# Multiply accumulated sum by sqrt(3) for final result
result = mp.sqrt(3) * sum_terms

# Print with 10 decimal precision using mpmath string formatting
print(mp.nstr(result, n=10))