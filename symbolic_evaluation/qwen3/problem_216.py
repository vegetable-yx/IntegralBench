import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression π√2 J_0(2)
sqrt2 = mp.sqrt(2)          # Compute square root of 2
bessel_j0 = mp.besselj(0, 2)  # Compute Bessel function J_0 at 2

# Combine components to get final result
result = mp.pi * sqrt2 * bessel_j0

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))