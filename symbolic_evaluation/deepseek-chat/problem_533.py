import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the result of the fraction 8/7
numerator = mp.mpf(8)
denominator = mp.mpf(7)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))