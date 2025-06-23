import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π using mpmath's constant
pi = mp.pi

# Compute π squared divided by 8
pi_squared_over_8 = (pi ** 2) / 8

# Compute π divided by 2
pi_over_2 = pi / 2

# Calculate the final result by subtracting the terms
result = pi_squared_over_8 - pi_over_2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))