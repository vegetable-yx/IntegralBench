import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 3
numerator = 3 * pi_squared

# Divide by 256 to get the final result
result = numerator / 256

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))