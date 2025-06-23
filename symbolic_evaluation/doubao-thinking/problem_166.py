import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi divided by 4
result = pi_value / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))