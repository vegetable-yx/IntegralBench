import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 10
sqrt_10 = mp.sqrt(10)

# Subtract 3 from the square root of 10
result = sqrt_10 - 3

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))