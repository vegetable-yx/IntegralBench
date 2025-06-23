import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π raised to the fourth power
pi_power4 = pi_val**4

# Divide the result by 8 to get final value
result = pi_power4 / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))