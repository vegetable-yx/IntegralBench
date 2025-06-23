import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate e squared
e_squared = mp.exp(2)

# Compute numerator: e^2 + 1
numerator = e_squared + 1

# Divide by 4 to get the result
result = numerator / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))