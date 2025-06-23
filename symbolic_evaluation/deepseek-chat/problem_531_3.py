import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the fraction 5/6
numerator = mp.mpf(5)
denominator = mp.mpf(6)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))