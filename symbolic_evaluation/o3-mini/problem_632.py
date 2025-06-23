import mpmath as mp

# Set internal decimal precision to 15 for reliable 10-digit output
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Negate the result to get -ln(2)
result = -ln2

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))