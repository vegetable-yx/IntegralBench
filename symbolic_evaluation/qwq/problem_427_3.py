import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 11
sqrt_11 = mp.sqrt(11)

# Multiply by 11 to get the numerator
numerator = 11 * sqrt_11

# Divide by 18 to get final result
result = numerator / 18

# Print result with 10 decimal places
print(mp.nstr(result, n=10))