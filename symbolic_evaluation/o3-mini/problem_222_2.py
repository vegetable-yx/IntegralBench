import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is 3 * π
pi_value = mp.pi  # Get the constant π from mpmath
constant_factor = 3  # Numerical factor in the expression

# Compute the result: 3 * π
result = constant_factor * pi_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))