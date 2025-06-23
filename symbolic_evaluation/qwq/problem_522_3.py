import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the numerator: square root of pi
numerator = mp.sqrt(mp.pi)

# Calculate the denominator: square root of 2019
denominator = mp.sqrt(2019)

# Compute the final result by dividing numerator by denominator
result = numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))