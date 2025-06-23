import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi using mpmath's constant
pi_val = mp.pi

# Compute the natural logarithm of 2
ln2_val = mp.log(2)

# Calculate the constant factor pi/8
pi_over_8 = pi_val / 8

# Multiply to get the final result: (pi/8) * ln(2)
result = pi_over_8 * ln2_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))