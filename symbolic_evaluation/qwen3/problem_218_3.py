import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')  # Tolerance for stopping the summation

while True:
    # Calculate binomial coefficient (2n choose n)
    binom = mp.binomial(2 * n, n)
    
    # Compute denominator components
    pow_16 = mp.power(16, n)
    cubic_term = mp.power(2 * n + 1, 3)
    
    # Calculate current term in the series
    term = binom / (pow_16 * cubic_term)
    
    # Add term to the cumulative sum
    sum_result += term
    
    # Check if term is smaller than tolerance to stop summation
    if mp.fabs(term) < tolerance:
        break
    
    n += 1

# Print result with exactly 10 decimal places
print(mp.nstr(sum_result, n=10))