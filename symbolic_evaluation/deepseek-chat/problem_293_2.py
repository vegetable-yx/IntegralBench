import mpmath as mp

# Set internal decimal places of precision to 15
mp.dps = 15

# Calculate the fraction 5/8 exactly
numerator = mp.mpf(5)
denominator = mp.mpf(8)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))