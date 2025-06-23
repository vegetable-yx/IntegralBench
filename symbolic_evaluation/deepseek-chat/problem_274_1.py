import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the result of 625 divided by 4
result = mp.mpf(625) / mp.mpf(4)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))