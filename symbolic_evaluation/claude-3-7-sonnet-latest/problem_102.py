import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the natural logarithm of 2
ln2_val = mp.log(2)

# Get the constant pi
pi_val = mp.pi

# Multiply pi and ln(2)
result = pi_val * ln2_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))