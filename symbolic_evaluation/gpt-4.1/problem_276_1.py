import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components separately
sqrt3 = mp.sqrt(3)        # Compute square root of 3
pi_half = mp.pi / 2        # Compute π/2
bessel_term = mp.besseli(0, 3)  # Compute modified Bessel function I₀(3)

# Combine components according to the formula
result = pi_half * sqrt3 * bessel_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))