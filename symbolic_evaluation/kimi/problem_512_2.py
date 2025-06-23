import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^2 using the constant e
e_squared = mp.e ** 2

# Compute numerator: e^2 - 1
numerator = e_squared - 1

# Divide by 4 to obtain final result
result = numerator / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))