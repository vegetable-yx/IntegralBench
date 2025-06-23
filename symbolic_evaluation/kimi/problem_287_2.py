import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant value 1/2
result = mp.mpf(1)/2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))