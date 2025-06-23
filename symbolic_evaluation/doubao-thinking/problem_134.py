import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi to get the final result
result = sqrt2 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))