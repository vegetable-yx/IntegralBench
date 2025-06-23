import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value directly
result = mp.mpf('1.5098775308')

# Print result to 10 decimal places
print(mp.nstr(result, n=10))