import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Multiply by -3 to get the result
result = -3 * pi_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))