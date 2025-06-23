import mpmath as mp
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Apply negative sign to the logarithm
result = -ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))