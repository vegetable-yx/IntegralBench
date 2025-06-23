import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate sqrt(2) component
sqrt_2 = mp.sqrt(2)

# Calculate pi squared component
pi_sq = mp.pi ** 2

# Combine components according to the formula (sqrt(2)/4) * pi²
result = (sqrt_2 / 4) * pi_sq

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))