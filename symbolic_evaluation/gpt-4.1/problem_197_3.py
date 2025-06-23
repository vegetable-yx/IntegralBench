import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the result: 1 divided by 4
result = mp.mpf(1) / mp.mpf(4)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))