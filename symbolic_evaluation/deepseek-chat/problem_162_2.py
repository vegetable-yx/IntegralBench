import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate hyperbolic cosine of 1
cosh_1 = mp.cosh(1)

# Multiply the components: 2 * sqrt(pi) * cosh(1)
result = 2 * sqrt_pi * cosh_1

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))