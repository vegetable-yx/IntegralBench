import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute e^2 using mpmath's exp function
e_squared = mp.exp(2)

# Calculate numerator (e^2 - 1)
numerator = e_squared - 1

# Final result by dividing numerator by 2
result = numerator / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))