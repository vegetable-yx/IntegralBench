import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the exact value of the fraction 8/3
result = mp.mpf(8) / mp.mpf(3)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))