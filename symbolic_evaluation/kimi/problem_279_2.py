import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate hyperbolic cosine of 1
cosh_value = mp.cosh(1)

# Calculate π/2
pi_half = mp.pi / 2

# Multiply π/2 with cosh(1) and apply negative sign
result = -pi_half * cosh_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))