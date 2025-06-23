import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Get the constant from mpmath
pi_constant = mp.pi

# Compute modified Bessel function of first kind I_0 at 1/2
bessel_value = mp.besseli(0, mp.mpf('0.5'))

# Combine all components according to the formula
result = sqrt2 * pi_constant * bessel_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))