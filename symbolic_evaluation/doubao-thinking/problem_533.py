import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the fraction 8/7
numerator = mp.mpf(8)
denominator = mp.mpf(7)
result = numerator / denominator

# Output the result to 10 decimal places
print(mp.nstr(result, n=10))