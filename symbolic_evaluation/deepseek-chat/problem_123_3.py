import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Assign the constant π
pi_value = mp.pi

# Calculate π divided by 2
result = pi_value / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))