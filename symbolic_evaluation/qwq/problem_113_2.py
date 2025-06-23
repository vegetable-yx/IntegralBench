import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 5
numerator = 5 * pi_squared

# Divide by 84 to get the final result
result = numerator / 84

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))