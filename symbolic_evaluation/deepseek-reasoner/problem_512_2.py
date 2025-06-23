import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute e^2 using mpmath's exponential function
e_squared = mp.exp(2)

# Calculate the numerator (e^2 - 1)
numerator = e_squared - 1

# Divide numerator by 4 to get final result
result = numerator / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))