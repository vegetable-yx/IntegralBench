import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)
n = 0
epsilon = mp.mpf('1e-15')  # Convergence threshold

while True:
    # Calculate the sign term (-1)^n
    sign = (-1) ** n
    
    # Compute Gamma(n + 3/4) for numerator
    gamma_arg = n + mp.mpf('3/4')
    gamma_term = mp.gamma(gamma_arg)
    
    # Square the gamma term for numerator
    numerator = sign * (gamma_term ** 2)
    
    # Compute denominator components: (2n)! and Gamma(2n + 3/2)
    factorial_term = mp.fac(2 * n)
    gamma_denom_arg = 2 * n + mp.mpf('3/2')
    gamma_denom = mp.gamma(gamma_denom_arg)
    
    # Combine denominator terms
    denominator = factorial_term * gamma_denom
    
    # Calculate current term in the series
    term = numerator / denominator
    
    # Add term to the cumulative sum
    sum_result += term
    
    # Check for convergence (term smaller than epsilon)
    if mp.fabs(term) < epsilon:
        break
    
    n += 1

# Print result with 10 decimal places
print(mp.nstr(sum_result, n=10))