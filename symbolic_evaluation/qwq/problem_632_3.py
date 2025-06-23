import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Apply negative sign to the result
result = -ln2

# Print the final value with 10 decimal places precision
print(mp.nstr(result, n=10))