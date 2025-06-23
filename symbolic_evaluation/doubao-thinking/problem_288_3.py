import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Compute π (pi) using mpmath constant
pi_val = mp.pi

# Compute the natural logarithm of (1 + √2)
ln_term = mp.log(1 + mp.sqrt(2))

# Compute the square of the natural logarithm term
ln_squared = ln_term ** 2

# Compute π squared divided by 12
pi_sq_over_12 = (pi_val ** 2) / 12

# Compute one-half of the squared logarithm term
half_ln_sq = 0.5 * ln_squared

# Sum the two components to get the final result
result = pi_sq_over_12 + half_ln_sq

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))