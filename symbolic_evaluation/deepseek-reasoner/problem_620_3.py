import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply π with ln2
pi_times_ln2 = mp.pi * ln2

# Divide the product by 8 to get final result
result = pi_times_ln2 / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))