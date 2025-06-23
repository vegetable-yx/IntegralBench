import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 11
sqrt_11 = mp.sqrt(11)

# Multiply by 11 to get the numerator
numerator = 11 * sqrt_11

# Denominator is 18
denominator = 18

# Divide numerator by denominator to get the result
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))