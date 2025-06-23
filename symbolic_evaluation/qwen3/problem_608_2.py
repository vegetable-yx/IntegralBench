import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute (ln2)^4 using exponentiation
ln2_pow4 = ln2**4

# Divide the result by 4 to get final value
result = ln2_pow4 / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))