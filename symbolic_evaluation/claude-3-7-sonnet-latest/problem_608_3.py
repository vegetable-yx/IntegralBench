import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute ln(2) using mpmath
ln2 = mp.log(2)

# Raise ln(2) to the 4th power
ln2_4 = ln2**4

# Multiply by -193
numerator = -193 * ln2_4

# Divide by 12 to get final result
result = numerator / 12

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))