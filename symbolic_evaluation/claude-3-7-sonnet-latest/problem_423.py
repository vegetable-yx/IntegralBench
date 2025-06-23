import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value 99 to the result
result = mp.mpf(99)

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))