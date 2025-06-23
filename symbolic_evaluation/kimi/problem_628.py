import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute the result using exact analytical expression -π/4
result = -pi_value / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))