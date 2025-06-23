import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Assign the constant value 4 to the result
result = mp.mpf(4)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))