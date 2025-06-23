import mpmath as mp
mp.dps = 15

sum_result = mp.mpf(0)
k = 0
tolerance = mp.mpf('1e-15')

while True:
    # Calculate Gamma(k + 3/2) using mpmath's gamma function
    gamma_term = mp.gamma(k + mp.mpf('3/2'))
    
    # Compute factorial of k using mpmath's factorial
    factorial_k = mp.factorial(k)
    
    # Calculate denominator components: (k!)^3 and (k+1)^2
    factorial_cubed = factorial_k ** 3
    k_plus_1_sq = (k + 1) ** 2
    
    # Combine denominator components
    denominator = factorial_cubed * k_plus_1_sq
    
    # Compute current term in the series
    term = (mp.sqrt(mp.pi) / 2) * gamma_term / denominator
    
    # Add term to cumulative sum
    sum_result += term
    
    # Check convergence using absolute value of term
    if mp.fabs(term) < tolerance:
        break
    
    k += 1

print(mp.nstr(sum_result, n=10))