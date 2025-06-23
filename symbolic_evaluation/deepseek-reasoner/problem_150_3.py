import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute square root of 2
sqrt_two = mp.sqrt(2)

# Calculate denominator 2√2
denominator = 2 * sqrt_two

# Compute final result (π²)/(2√2)
result = pi_squared / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))