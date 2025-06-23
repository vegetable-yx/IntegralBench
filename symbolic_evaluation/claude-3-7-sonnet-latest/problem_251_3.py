import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi (π) using mpmath constant
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Compute the expression: (π * ln(2)) / 2
result = (pi_val * ln2_val) / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))