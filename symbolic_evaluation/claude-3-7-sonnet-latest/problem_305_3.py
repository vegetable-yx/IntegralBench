import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate mathematical constant pi
pi_val = mp.pi

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Multiply pi and ln(2)
numerator = pi_val * ln2

# Divide the numerator by 4 to get the final result
result = numerator / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))