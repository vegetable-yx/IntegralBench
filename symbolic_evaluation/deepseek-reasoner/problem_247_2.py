import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π squared
pi_squared = mp.power(pi_val, 2)

# Calculate numerator: 3 * π²
numerator = mp.mpf(3) * pi_squared

# Calculate denominator: 128
denominator = mp.mpf(128)

# Final result: (3π²)/128
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))