import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Calculate the natural logarithm of 2
ln2_val = mp.log(2)

# Compute π/4
part1 = pi_val / 4

# Compute (1/2) * ln(2)
part2 = 0.5 * ln2_val

# Compute the inner expression: (π/4 - (1/2)ln(2))
inner_expr = part1 - part2

# Compute the square root of π
sqrt_pi = mp.sqrt(pi_val)

# Multiply to get the final result
result = sqrt_pi * inner_expr

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))