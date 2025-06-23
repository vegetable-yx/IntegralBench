import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Initialize the sum
s = mp.mpf(0)
k = 1
# Tolerance for convergence (sufficient for 10 decimal places)
tol = mp.mpf('1e-20')
max_terms = 10000

# Sum the series until convergence or max terms
while k <= max_terms:
    # Compute numerator components
    gamma1 = mp.gamma((k + 1) / 2)
    gamma2 = mp.gamma((k + 2) / 2)
    two_power_k = mp.power(2, k)
    numerator = two_power_k * gamma1 * gamma2
    
    # Compute denominator components
    k_squared = mp.power(k, 2)
    gamma_k2 = mp.gamma(k + 2)
    denominator = k_squared * gamma_k2
    
    # Calculate current term
    term = numerator / denominator
    s += term
    
    # Check for convergence (absolute value of term below tolerance)
    if mp.fabs(term) < tol:
        break
    k += 1

# Multiply by sqrt(2) for final result
result = mp.sqrt(2) * s

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))