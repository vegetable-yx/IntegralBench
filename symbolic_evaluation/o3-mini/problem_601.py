import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define pi constant
pi_val = mp.pi

# Compute natural logarithm of 2
ln2_val = mp.log(2)

# Multiply pi and ln(2)
result = pi_val * ln2_val

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))