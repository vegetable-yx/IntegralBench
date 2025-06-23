import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate e^2 using mpmath's exponential function
e_squared = mp.exp(2)

# Compute the numerator (e^2 - 1)
numerator = e_squared - 1

# Calculate final result by dividing numerator by 4
result = numerator / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))