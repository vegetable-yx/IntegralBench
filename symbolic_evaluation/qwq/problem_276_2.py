import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute the coefficient (sqrt(3) * pi)/2
coeff = (sqrt3 * mp.pi) / 2

# Calculate modified Bessel function of first kind I_0(3)
bessel_i0 = mp.besseli(0, 3)

# Multiply components to get final result
result = coeff * bessel_i0

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))