import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π (pi) using mpmath constant
pi_val = mp.pi

# Compute natural logarithm of 2
ln2_val = mp.log(2)

# Calculate π divided by 2
pi_over_2 = pi_val / 2

# Multiply π/2 by ln(2) to get the final result
result = pi_over_2 * ln2_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))