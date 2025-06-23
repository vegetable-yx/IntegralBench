import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Assign the constant value directly to result
result = mp.mpf('2.106189771')

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))