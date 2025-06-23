import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute pi raised to the 4th power
pi_val = mp.pi
pi_power4 = mp.power(pi_val, 4)

# Divide by 1440 to get the result
result = pi_power4 / 1440

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))