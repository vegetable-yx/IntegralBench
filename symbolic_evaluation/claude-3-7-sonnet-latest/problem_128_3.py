import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the numerator: 2 * sqrt(2) * (cosh(1) - 1)
sqrt2 = mp.sqrt(2)  # Compute sqrt(2)
cosh1 = mp.cosh(1)  # Compute cosh(1)
numerator = 2 * sqrt2 * (cosh1 - 1)  # Combine terms for numerator

# Calculate the denominator: sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)  # Compute square root of pi

# Compute the final result: numerator / denominator
result = numerator / sqrt_pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))