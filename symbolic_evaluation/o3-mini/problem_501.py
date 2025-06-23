import mpmath as mp

# Set the internal decimal precision to 15
mp.dps = 15

# Calculate the fraction 2/5
numerator = mp.mpf(2)
denominator = mp.mpf(5)
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))