import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Compute the natural logarithm of 2
ln2_val = mp.log(2)

# Calculate the expression: (pi * ln(2)) / 2
result = (pi_val * ln2_val) / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))