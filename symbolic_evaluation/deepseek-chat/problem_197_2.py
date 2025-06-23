import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the fraction 1/4
result = mp.mpf(1) / mp.mpf(4)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))