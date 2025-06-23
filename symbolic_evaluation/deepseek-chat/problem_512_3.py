import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^2 using exponential function
e_squared = mp.exp(2)

# Compute numerator: e^2 - 1
numerator = e_squared - 1

# Divide by 4 to get the final result
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))