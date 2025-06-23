import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of the fraction 1/5
result = mp.mpf(1) / mp.mpf(5)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))