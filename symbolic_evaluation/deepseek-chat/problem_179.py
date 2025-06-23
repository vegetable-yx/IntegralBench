import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the fraction 1/12
numerator = mp.mpf(1)
denominator = mp.mpf(12)
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))