import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate sqrt(π)
sqrt_pi = mp.sqrt(mp.pi)

# Calculate sqrt(2)
sqrt_2 = mp.sqrt(2)

# Compute (sqrt(2) - 1) term
sqrt_diff = sqrt_2 - 1

# Combine components for final result
result = (sqrt_pi * sqrt_diff) / 2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))