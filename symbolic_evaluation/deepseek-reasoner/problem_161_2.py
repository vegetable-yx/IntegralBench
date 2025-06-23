import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate modified Bessel functions of the first kind
i0_val = mp.besseli(0, 1)  # I₀(1)
i1_val = mp.besseli(1, 1)  # I₁(1)

# Compute the difference between Bessel functions
bessel_diff = i0_val - i1_val

# Calculate the final result with sqrt(2) and π
result = mp.sqrt(2) * mp.pi * bessel_diff

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))