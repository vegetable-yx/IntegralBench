import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute sqrt(2) constant
sqrt2 = mp.sqrt(2)

# Initialize the series sum
series_sum = mp.mpf(0)
k = 0
# Set convergence tolerance (1e-20) and maximum terms (1000) to prevent infinite loops
tol = mp.mpf('1e-20')
max_terms = 1000

while k < max_terms:
    # Compute numerator: Gamma((k+1)/2) * Gamma((k+2)/2)
    gamma1 = mp.gamma((k + 1) / 2)
    gamma2 = mp.gamma((k + 2) / 2)
    numerator = gamma1 * gamma2
    
    # Compute denominator: (k!)^2 * 2^k * Gamma(k+2)
    fact_k = mp.factorial(k)
    fact_k_sq = fact_k ** 2
    two_power_k = 2 ** k
    gamma_k2 = mp.factorial(k + 1)  # Since Gamma(n+1) = n! for integer n
    denominator = fact_k_sq * two_power_k * gamma_k2
    
    # Calculate current term
    term = numerator / denominator
    series_sum += term
    
    # Check for convergence (if term is below tolerance)
    if mp.fabs(term) < tol:
        break
    
    k += 1

# Multiply series by sqrt(2) to get final result
result = sqrt2 * series_sum

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))