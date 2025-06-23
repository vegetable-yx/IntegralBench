import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_terms = mp.mpf(0)
n = 1

while True:
    # Calculate sign for the current term
    sign = (-1) ** (n + 1)
    
    # Calculate 3^n * n denominator component
    denom = (3 ** n) * n
    
    # Compute gamma(n/2) and gamma((n+1)/2)
    gamma_n_half = mp.gamma(n / 2)
    gamma_n_plus_half = mp.gamma((n + 1) / 2)
    
    # Compute the current term in the series
    term = sign * gamma_n_half / (denom * gamma_n_plus_half)
    
    # Add term to the cumulative sum
    sum_terms += term
    
    # Check if term magnitude is below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    
    n += 1

# Multiply sum by sqrt(pi) to get final result
result = mp.sqrt(mp.pi) * sum_terms

# Print result with 10 decimal places
print(mp.nstr(result, n=10))