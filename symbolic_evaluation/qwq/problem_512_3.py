import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate e squared
e_squared = mp.exp(2)

# Compute numerator (e^2 - 1)
numerator = e_squared - 1

# Final result calculation
result = numerator / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))