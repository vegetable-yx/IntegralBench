import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π raised to the fifth power
pi_power = pi_value**5

# Divide the result by 160
result = pi_power / 160

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))