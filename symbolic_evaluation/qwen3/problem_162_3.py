import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate modified Bessel function of first kind I_0(1)
i0_value = mp.besseli(0, 1)

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply sqrt(2) by pi
sqrt2_pi = sqrt2 * mp.pi

# Combine all components for final result
result = sqrt2_pi * i0_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))