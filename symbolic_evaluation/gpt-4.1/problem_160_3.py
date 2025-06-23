import mpmath as mp

mp.dps = 15  # Initialize sum for series expansion
sum_part = mp.mpf(0)

for k in range(0, 100):
    # Compute parameters for beta function
    a = (k + 1) / 2
    b = (k + 2) / 2
    
    # Calculate beta function component
    beta_val = mp.beta(a, b)
    
    # Compute term components
    numerator = 2**k
    denominator = mp.factorial(2 * k)
    
    # Calculate current term and add to sum
    term = (numerator * beta_val) / denominator
    sum_part += term
    
    # Break if term is negligible for 15-digit precision
    if mp.mag(term) < -25:
        break

# Multiply by sqrt(2) for final result
result = mp.sqrt(2) * sum_part

# Print with 10 decimal precision
print(mp.nstr(result, n=10))