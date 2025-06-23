import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 4 to get numerator
numerator = 4 * pi_squared

# Divide by 15 to get final result
result = numerator / 15

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))