import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 2 divided by pi using exact constants
numerator = mp.mpf(2)
denominator = mp.pi
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))