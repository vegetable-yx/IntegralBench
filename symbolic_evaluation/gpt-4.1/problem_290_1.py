import mpmath as mp

mp.dps = 15  # Set internal precision

sum_series = mp.mpf(0)
m = 0
tolerance = mp.mpf('1e-20')  # Term magnitude tolerance

while True:
    # Calculate numerator (m + 3/2)
    numerator = m + mp.mpf('3/2')
    
    # Calculate denominator components
    factorial_m = mp.factorial(m)
    denominator_factor = (m + 2) * (m + 1)
    denominator = denominator_factor * (factorial_m ** 2)
    
    # Compute current series term
    term = numerator / denominator
    
    # Add term to cumulative sum
    sum_series += term
    
    # Break loop when term magnitude drops below tolerance
    if mp.fabs(term) < tolerance:
        break
    
    m += 1  # Increment series index

# Multiply accumulated sum by sqrt(pi) for final result
result = sum_series * mp.sqrt(mp.pi)

# Output result with 10 decimal precision
print(mp.nstr(result, n=10))