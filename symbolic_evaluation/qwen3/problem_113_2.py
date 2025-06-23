import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Initialize the sum and term variables
sum_series = mp.mpf(0)
k = 1
while True:
    # Calculate binomial coefficient (2k choose k)
    binom = mp.binomial(2 * k, k)
    
    # Calculate denominator 8^k * k^2
    denom = (8 ** k) * (k ** 2)
    
    # Compute current term
    term = binom / denom
    
    # Add term to the series sum
    sum_series += term
    
    # Check if term is smaller than 1e-20 to ensure precision up to 1e-10 in final result
    if mp.fabs(term) < 1e-20:
        break
    k += 1

# Multiply by sqrt(2) * pi to get final result
result = mp.sqrt(2) * mp.pi * sum_series

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))