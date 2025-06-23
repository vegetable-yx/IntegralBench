import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by sqrt(2) to get the final result
result = sqrt_2 * mp.pi

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))