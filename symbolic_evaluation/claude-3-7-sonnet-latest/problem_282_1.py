import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute I_0(4) - modified Bessel function of first kind, order 0 at 4
bessel_value = mp.besseli(0, 4)

# Compute pi * I_0(4)
numerator = mp.pi * bessel_value

# Compute square root of 2
denominator = mp.sqrt(2)

# Final result: (pi * I_0(4)) / sqrt(2)
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))