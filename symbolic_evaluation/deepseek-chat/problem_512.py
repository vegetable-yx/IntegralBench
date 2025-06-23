import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e raised to the power of 2 using exponential function
e_squared = mp.exp(2)

# Subtract 1 from e^2 to get the numerator
numerator = e_squared - 1

# Divide the numerator by 4 to get the final result
result = numerator / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))