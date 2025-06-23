import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the fraction 2/5
numerator = mp.mpf(2)
denominator = mp.mpf(5)
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))