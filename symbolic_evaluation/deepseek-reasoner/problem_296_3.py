import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply by 8
numerator = pi_squared * 8

# Divide by 16 to get the final result
result = numerator / 16

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))