import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute e^2
e_squared = mp.exp(2)

# Calculate numerator: e^2 - 1
numerator = e_squared - 1

# Compute final result: (e^2 - 1) / 4
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))