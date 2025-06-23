import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Compute (pi * ln(2)) / 8
result = (pi_val * ln2_val) / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))