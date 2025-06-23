import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Get pi constant
pi_val = mp.pi

# Compute Bessel function of the first kind J_1(1)
bessel_j1_1 = mp.besselj(1, 1)

# Combine components to get final result
result = sqrt2 * pi_val * bessel_j1_1

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))