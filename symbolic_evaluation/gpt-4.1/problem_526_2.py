import mpmath as mp

# Set internal decimal precision to 15 for accurate results
mp.dps = 15

# Compute natural logarithm of 3
ln3 = mp.log(3)

# Calculate pi/4 multiplied by ln(3)
result = (mp.pi / 4) * ln3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))