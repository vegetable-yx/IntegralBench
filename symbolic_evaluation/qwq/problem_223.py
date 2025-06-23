import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Square the natural logarithm of 2
ln2_sq = ln2 ** 2

# Calculate pi squared
pi_sq = mp.pi ** 2

# Multiply pi squared with squared logarithm of 2
product = pi_sq * ln2_sq

# Divide by 2 to get final result
result = product / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))