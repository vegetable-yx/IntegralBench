import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize sum and term counter
total = mp.mpf(0)
n = 0
# Set tolerance for convergence (stop when term < 1e-20)
tolerance = mp.mpf('1e-20')
max_terms = 1000  # Prevent infinite loops

# Sum the series until convergence
while n < max_terms:
    # Precompute exponent for 2: -(2n+1)/2
    exponent = -(2 * n + 1) / 2
    power_term = mp.power(2, exponent)  # 2^exponent
    
    # Gamma functions in numerator
    gamma1 = mp.gamma(n/2 + 1)         # Γ(n/2 + 1)
    gamma2 = mp.gamma((n + 1)/2)        # Γ((n+1)/2)
    
    # Denominator components
    factorial_n = mp.factorial(n)       # n!
    gamma_denom1 = mp.gamma(n + 2)      # Γ(n+2)
    gamma_denom2 = mp.gamma(n + 1.5)    # Γ(n+3/2)
    
    # Combine denominator: n! * Γ(n+2) * Γ(n+3/2)
    denominator = factorial_n * gamma_denom1 * gamma_denom2
    
    # Compute current term
    term = power_term * gamma1 * gamma2 / denominator
    total += term
    
    # Check for convergence
    if mp.fabs(term) < tolerance:
        break
    n += 1

# Print the final result to 10 decimal places
print(mp.nstr(total, n=10))