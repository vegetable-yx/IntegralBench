import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the fraction 9/512
result = mp.mpf(9) / mp.mpf(512)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))