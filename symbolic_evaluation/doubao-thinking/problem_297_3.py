import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 11 to get the numerator
numerator = 11 * pi_squared

# Divide by 96 to get the final result
result = numerator / 96

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))