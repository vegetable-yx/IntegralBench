import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π raised to the fourth power
pi_power4 = mp.power(pi_val, 4)

# Multiply by 3 and divide by 16 to get final result
result = (3 * pi_power4) / 16

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))