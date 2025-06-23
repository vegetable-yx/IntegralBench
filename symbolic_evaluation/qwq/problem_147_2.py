import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi = mp.pi

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute the inner expression (π + 2ln2)
inner_expression = pi + 2 * ln2

# Multiply by π/2 to get final result
result = (pi / 2) * inner_expression

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))