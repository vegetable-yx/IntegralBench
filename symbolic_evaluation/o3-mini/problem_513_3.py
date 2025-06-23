import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value 113 to the result
result = mp.mpf(113)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))