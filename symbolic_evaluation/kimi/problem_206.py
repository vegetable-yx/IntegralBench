import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate the numerator: π^(3/2)
pi_val = mp.pi
sqrt_pi = mp.sqrt(pi_val)  # Square root of π
numerator = pi_val * sqrt_pi  # π^(3/2) = π * √π

# Calculate the denominator: 2√2
sqrt2 = mp.sqrt(2)
denominator = 2 * sqrt2

# Compute the final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))