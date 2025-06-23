import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (pi) using mpmath constant
pi_value = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Compute the expression: (π * ln(3)) / 4
result = (pi_value * ln3) / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))