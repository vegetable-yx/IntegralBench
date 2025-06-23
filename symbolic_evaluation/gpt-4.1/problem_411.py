import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value 1 to the result
result = mp.mpf(1)

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))