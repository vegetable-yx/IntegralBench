import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Print the result with exactly 10 decimal places
print(mp.nstr(ln2, n=10))