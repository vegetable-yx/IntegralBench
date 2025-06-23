import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by 2
term = 2 * sqrt_2

# Subtract 3 to get final result
result = term - 3

# Print result with 10 decimal places
print(mp.nstr(result, n=10))