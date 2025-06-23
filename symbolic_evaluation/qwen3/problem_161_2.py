import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/2
pi_over_2 = mp.pi / 2

# Compute square root of π/2
sqrt_pi_over_2 = mp.sqrt(pi_over_2)

# Calculate hyperbolic sine of 1
sinh_1 = mp.sinh(1)

# Multiply components to get final result
result = sqrt_pi_over_2 * sinh_1

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))