import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e squared using mpmath's exp function
e_squared = mp.exp(2)

# Compute the numerator (e^2 - 1)
numerator = e_squared - 1

# Divide by 4 to get the final result
result = numerator / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))