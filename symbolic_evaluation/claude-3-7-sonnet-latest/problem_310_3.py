import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Calculate the natural logarithm of 2
ln2_val = mp.log(2)

# Multiply pi and ln(2)
result = pi_val * ln2_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))