import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the value of pi
pi_value = mp.pi

# Compute the result: -3 * π
result = -3 * pi_value

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))