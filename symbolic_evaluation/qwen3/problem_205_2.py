import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Get pi constant
pi = mp.pi

# Calculate Bessel function of first kind J_1(1)
bessel_j1_1 = mp.besselj(1, 1)

# Multiply components together
result = sqrt2 * pi * bessel_j1_1

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))