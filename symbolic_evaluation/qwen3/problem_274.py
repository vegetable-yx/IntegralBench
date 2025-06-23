import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Compute modified Bessel functions of first kind
i0 = mp.besseli(0, 5)
i1 = mp.besseli(1, 5)
i2 = mp.besseli(2, 5)

# Calculate the weighted sum of Bessel functions
bessel_sum = 13*i0 + 37*i1 + 12*i2

# Compute exponential term
exp_term = mp.exp(-5)

# Calculate the coefficient 25/4 with high precision
coefficient = mp.mpf(25)/4

# Combine all components
result = coefficient * exp_term * bessel_sum * mp.sqrt(mp.pi)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))