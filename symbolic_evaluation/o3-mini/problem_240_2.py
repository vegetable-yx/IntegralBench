import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Calculate 2 times ln(2)
two_ln2 = 2 * ln2

# Subtract 1 from 2*ln(2)
inner_expr = two_ln2 - 1

# Multiply by 1/2 to get final result
result = 0.5 * inner_expr

# Print result with 10 decimal places
print(mp.nstr(result, n=10))