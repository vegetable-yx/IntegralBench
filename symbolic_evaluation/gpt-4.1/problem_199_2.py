import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Initialize the sum
result = mp.mpf(0)

# Tolerance for stopping the series when terms become negligible
tol = mp.mpf('1e-20')

# Maximum terms to prevent infinite loops
max_terms = 1000

# Start the series summation
for n in range(max_terms):
    # Calculate sign term: (-1)^n
    sign = mp.power(-1, n)
    
    # Calculate 2^(n/2)
    base_power = mp.power(2, n / mp.mpf(2))
    
    # Gamma((n+3)/4)
    gamma1 = mp.gamma((n + 3) / mp.mpf(4))
    
    # Gamma((n+1)/4)
    gamma2 = mp.gamma((n + 1) / mp.mpf(4))
    
    # Numerator: (-1)^n * 2^(n/2) * Gamma((n+3)/4) * Gamma((n+1)/4)
    numerator = sign * base_power * gamma1 * gamma2
    
    # Denominator components
    # Factorial term: (2n+1)!
    fact_denom = mp.factorial(2 * n + 1)
    
    # Gamma(n/2 + 1)
    gamma_denom = mp.gamma(n / mp.mpf(2) + 1)
    
    # Full denominator: (2n+1)! * Gamma(n/2 + 1)
    denominator = fact_denom * gamma_denom
    
    # Current term value
    term = numerator / denominator
    
    # Add term to the result
    result += term
    
    # Break if term is below tolerance
    if mp.fabs(term) < tol:
        break

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))