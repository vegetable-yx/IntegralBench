import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate pi^4 using mpmath's constant
pi_power4 = mp.pi ** 4

# Compute the 7/24 coefficient multiplied by pi^4
result = (7 * pi_power4) / 24

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))