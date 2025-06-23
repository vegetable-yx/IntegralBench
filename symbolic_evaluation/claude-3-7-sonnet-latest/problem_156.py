import mpmath as mp

# Set the internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate π^3
pi_cubed = mp.pi ** 3

# Divide π^3 by 8
pi_cubed_over_8 = pi_cubed / 8

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the natural logarithm of (1 + √2)
ln_term = mp.log(1 + sqrt2)

# Multiply the two parts to get the final result
result = pi_cubed_over_8 * ln_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))