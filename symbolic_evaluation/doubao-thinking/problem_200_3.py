import mpmath as mp

mp.dps = 15  # Set internal precision

sum_part = mp.mpf(0)
n = 0
while True:
    # Calculate binomial coefficient (2n choose n)
    binom = mp.binomial(2*n, n)
    
    # Calculate numerator component (-1)^n * binomial
    sign = (-1)**n
    numerator = sign * binom
    
    # Calculate denominator components (2n+1)! and 4^n
    factorial_term = mp.fac(2*n + 1)
    four_power = 4**n
    
    # Combine denominator terms
    denominator = factorial_term * four_power
    
    # Calculate current term in the series
    term = numerator / denominator
    
    # Add term to the partial sum
    sum_part += term
    
    # Break condition when term magnitude drops below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    
    n += 1

# Multiply sum by sqrt(2) and pi for final result
result = mp.sqrt(2) * mp.pi * sum_part

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))