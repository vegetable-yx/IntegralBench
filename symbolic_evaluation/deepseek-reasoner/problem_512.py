import mpmath as mp
mp.dps = 15

# Calculate e squared using exponential function
e_squared = mp.exp(2)

# Compute numerator (e^2 - 1)
numerator = e_squared - 1

# Final result by dividing numerator by 4
result = numerator / 4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))