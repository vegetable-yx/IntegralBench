import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate cosh(1)
cosh_1 = mp.cosh(1)

# Calculate π/2
pi_over_2 = mp.pi / 2

# Multiply components and apply negative sign
result = -pi_over_2 * cosh_1

# Print result with 10 decimal places
print(mp.nstr(result, n=10))