import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Compute the natural logarithm of 2
ln2_val = mp.log(2)

# Calculate the numerator: pi multiplied by ln(2)
numerator = pi_val * ln2_val

# Divide the numerator by 8 to get the positive part of the expression
positive_part = numerator / 8

# Apply the negative sign to get the final result
result = -positive_part

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))