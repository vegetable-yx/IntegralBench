import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate e squared using mpmath exponential function
e_squared = mp.exp(2)

# Compute the sum of e squared and 1
numerator = e_squared + 1

# Divide the result by 4 to get final value
result = numerator / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))