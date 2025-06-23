import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate components of the expression
sqrt5 = mp.sqrt(5)  # Compute square root of 5
golden_ratio = (1 + sqrt5) / 2  # Calculate (1 + sqrt(5))/2
log_term = mp.log(golden_ratio)  # Compute natural logarithm of golden ratio

# Combine components for final result
result = (mp.pi / 2) * log_term  # Multiply π/2 with logarithmic term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))