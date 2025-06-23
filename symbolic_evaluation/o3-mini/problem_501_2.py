import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the fraction 2/5
result = mp.mpf(2) / mp.mpf(5)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))