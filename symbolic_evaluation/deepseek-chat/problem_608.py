import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute ln(2) raised to the 4th power
ln2_power4 = ln2**4

# Multiply by 11/4 to get the final result
result = (mp.mpf(11) / 4) * ln2_power4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))