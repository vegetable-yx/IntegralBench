import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π (pi) constant
pi_val = mp.pi

# Compute √3 (square root of 3)
sqrt_3 = mp.sqrt(3)

# Calculate numerator: 7 * π
numerator = 7 * pi_val

# Calculate denominator: 3 * √3
denominator = 3 * sqrt_3

# Compute final result: (7π) / (3√3)
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))