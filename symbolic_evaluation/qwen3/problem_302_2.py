import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_series = mp.mpf(0)  # Initialize the series sum
n = 0  # Start summation index at 0

while True:
    # Calculate denominator components: 16^n and (2n+1)^3
    power_16 = mp.power(16, n)
    cubic_term = mp.power(2 * n + 1, 3)
    
    # Compute current term value
    denominator = power_16 * cubic_term
    term = mp.mpf(1) / denominator
    
    sum_series += term  # Accumulate terms
    
    # Stop when term magnitude drops below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    
    n += 1  # Move to next term

# Apply the 1/4 factor from the original formula
result = sum_series / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))