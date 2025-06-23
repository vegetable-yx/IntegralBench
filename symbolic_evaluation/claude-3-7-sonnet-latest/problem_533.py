import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of the fraction 8/7
numerator = mp.mpf(8)
denominator = mp.mpf(7)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))