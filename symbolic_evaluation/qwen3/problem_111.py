import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π²
pi_squared = mp.pi ** 2

# Calculate π²/6
term1 = pi_squared / 6

# Calculate (π²/6 - 1)
term2 = term1 - 1

# Calculate sqrt(2π)
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Multiply components for final result
result = sqrt_2pi * term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))