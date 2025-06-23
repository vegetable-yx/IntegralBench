import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi^4 (π raised to the fourth power)
pi_power_4 = mp.pi ** 4

# Multiply by the coefficient 7/4
result = (7 * pi_power_4) / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))