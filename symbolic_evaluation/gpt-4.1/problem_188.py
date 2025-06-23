import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the exact fraction 1/20
numerator = mp.mpf(1)
denominator = mp.mpf(20)
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))