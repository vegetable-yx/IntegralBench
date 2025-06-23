import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e squared (e^2)
e_squared = mp.exp(2)  # Alternatively, we could use mp.e**2

# Compute the numerator: e^2 - 1
numerator = e_squared - 1

# Divide the numerator by 4 to get the final result
result = numerator / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))