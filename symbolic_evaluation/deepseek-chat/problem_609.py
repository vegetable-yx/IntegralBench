import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign negative infinity to result
result = mp.ninf

# Print the result formatted to 10 decimal places
# Note: mp.nstr formats mp.ninf as '-inf'
print(mp.nstr(result, n=10))