import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Compute the constant pi
pi_val = mp.pi

# Calculate pi divided by 2
pi_over_2 = pi_val / 2

# Multiply pi/2 by ln(2)
product = pi_over_2 * ln2

# Apply the negative sign to get the final result
result = -product

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))