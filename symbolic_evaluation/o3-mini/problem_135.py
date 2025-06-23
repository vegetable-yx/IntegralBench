import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant π
pi_val = mp.pi

# Multiply π by 3
numerator = 3 * pi_val

# Divide the result by 4
result = numerator / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))