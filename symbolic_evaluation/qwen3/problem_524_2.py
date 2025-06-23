import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate e squared using mpmath constant
e_squared = mp.e ** 2

# Compute numerator (1 + e^2)
numerator = 1 + e_squared

# Final result by dividing numerator by 4
result = numerator / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))