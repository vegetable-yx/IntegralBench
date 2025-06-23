import mpmath as mp
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Raise ln(2) to the 4th power
ln2_power4 = ln2 ** 4

# Divide by 4 to get the final result
result = ln2_power4 / 4

print(mp.nstr(result, n=10))