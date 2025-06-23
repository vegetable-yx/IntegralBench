import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's built-in constant
pi_val = mp.pi

# Compute π raised to the fourth power
pi_power4 = pi_val**4

# Divide the result by 144 to get the final value
result = pi_power4 / 144

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))