import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the value of 1 divided by 4
numerator = mp.mpf(1)
denominator = mp.mpf(4)
result = numerator / denominator

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))