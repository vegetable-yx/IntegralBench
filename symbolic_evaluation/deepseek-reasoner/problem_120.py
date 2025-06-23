import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi to the 4th power
pi_power4 = mp.power(pi_value, 4)

# Divide by 128 to get final result
result = pi_power4 / 128

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))