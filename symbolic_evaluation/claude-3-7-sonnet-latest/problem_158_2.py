import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value 3.0 to the result
result = mp.mpf('3.0')

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))