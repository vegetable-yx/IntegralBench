import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e squared
e_squared = mp.exp(2)

# Add 1 to e squared
numerator = e_squared + 1

# Divide by 4 to get final result
result = numerator / 4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))