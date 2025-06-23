import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate e^2 using mpmath's constant e
e_squared = mp.e ** 2

# Compute numerator (e^2 + 1)
numerator = e_squared + 1

# Calculate final result by dividing numerator by 4
result = numerator / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))