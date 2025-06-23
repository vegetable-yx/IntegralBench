import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Calculate the constant 2π
two_pi = 2 * mp.pi

# Compute the final result: 2π * ln(3)
result = two_pi * ln3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))