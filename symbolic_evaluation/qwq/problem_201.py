import mpmath as mp

mp.dps = 15  # Set internal precision

sum_result = mp.mpf(0)  # Initialize sum with mpmath precision
n = 0

while True:
    # Calculate components for the term
    sign = (-1) ** n
    numerator = mp.sqrt(mp.pi) * mp.factorial(n)
    denominator = mp.factorial(2 * n) * mp.gamma(n + mp.mpf('1.5'))
    
    # Compute current term
    term = sign * numerator / denominator
    
    # Add term to the cumulative sum
    sum_result += term
    
    # Check if term magnitude is below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    
    n += 1  # Increment term index

# Print result to 10 decimal places
print(mp.nstr(sum_result, n=10))