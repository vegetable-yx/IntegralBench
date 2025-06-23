import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π raised to the fifth power
pi_power5 = pi_value ** 5

# Divide the result by 128 to get the final value
result = pi_power5 / 128

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))