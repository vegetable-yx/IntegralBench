import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 3 to get the numerator
numerator = 3 * pi_squared

# Divide by 16 to get the final result
result = numerator / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))