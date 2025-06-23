import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π and its powers
pi_val = mp.pi
pi_squared = mp.power(pi_val, 2)
pi_power4 = mp.power(pi_squared, 2)

# Compute numerator and final result
numerator = 27 * pi_power4
result = numerator / 16

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))