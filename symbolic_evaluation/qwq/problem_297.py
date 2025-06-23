import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 5
numerator = 5 * pi_squared

# Divide by 84 to get final result
result = numerator / 84

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))