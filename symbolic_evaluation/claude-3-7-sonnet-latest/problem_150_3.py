import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 2 to get the result
result = 2 * pi_squared

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))