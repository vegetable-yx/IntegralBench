import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate mathematical constant e
e_value = mp.e

# Calculate reciprocal of e
reciprocal_e = 1 / e_value

# Compute the difference (e - 1/e)
e_difference = e_value - reciprocal_e

# Multiply by square root of 2
result = mp.sqrt(2) * e_difference

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))