import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi
pi_value = mp.pi

# Multiply by -3 to get the result
result = -3 * pi_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))