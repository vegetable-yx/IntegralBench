import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate components of the expression
sqrt2 = mp.sqrt(2)          # Compute √2
bessel_term = mp.besseli(1, 1)  # Compute modified Bessel function I_1(1)

# Combine components using the formula 4√2πI_1(1)
result = 4 * sqrt2 * mp.pi * bessel_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))