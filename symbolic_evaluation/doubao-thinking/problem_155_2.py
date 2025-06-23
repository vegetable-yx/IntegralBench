import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the calculated π value
pi_sq = pi_val ** 2

# Divide squared π by 16 to get final result
result = pi_sq / 16

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))