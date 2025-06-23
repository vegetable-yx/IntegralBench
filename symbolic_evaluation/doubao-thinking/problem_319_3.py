import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the numerator
numerator = mp.mpf(4)

# Calculate the denominator
denominator = mp.mpf(3)

# Compute the final result
result = numerator / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))