import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's high-precision constant
pi_val = mp.pi

# Compute π raised to the fourth power
pi_power4 = pi_val ** 4

# Divide the result by 64 to get the final value
result = pi_power4 / 64

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))