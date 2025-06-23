import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Compute the expression: (pi * ln(3)) / 16
result = (pi_val * ln3) / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))