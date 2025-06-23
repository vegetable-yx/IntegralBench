import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the fraction 4/3
numerator = mp.mpf(4)
denominator = mp.mpf(3)
result = numerator / denominator

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))