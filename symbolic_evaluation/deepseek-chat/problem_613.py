import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the value of 1/5
result = mp.mpf(1) / mp.mpf(5)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))