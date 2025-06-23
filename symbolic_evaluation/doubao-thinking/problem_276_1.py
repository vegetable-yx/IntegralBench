import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (modify a and b values as needed)
a = mp.mpf('1.0')
b = mp.mpf('1.0')

# Initialize sum and variables for series calculation
series_sum = mp.mpf(0)
n = 0
tolerance = mp.mpf('1e-15')
base_factor = (a**2 * b**2) / 4  # Pre-calculate recurring term

# Calculate series terms until convergence
while True:
    # Compute numerator components
    numerator = base_factor**n * (2*n + 1)
    
    # Compute denominator components
    denominator = mp.fac(4*n + 2)
    
    # Calculate current term value
    term = numerator / denominator
    
    # Add term to cumulative sum
    series_sum += term
    
    # Break loop when term falls below precision threshold
    if term < tolerance:
        break
    
    n += 1

# Compute final result with multiplicative constants
result = 2 * mp.sqrt(a) * series_sum

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))