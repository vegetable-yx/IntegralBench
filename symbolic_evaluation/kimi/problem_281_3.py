import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt2 = mp.sqrt(2)  # Compute square root of 2
pi_over_sqrt2 = mp.pi / sqrt2  # Compute π/√2
bessel_i0 = mp.besseli(0, 4)  # Compute modified Bessel function I_0(4)

# Combine components for final result
result = pi_over_sqrt2 * bessel_i0

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))