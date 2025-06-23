import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute numerator: sqrt(5) - 1
numerator = sqrt5 - 1

# Divide by 4 to get final result
result = numerator / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))