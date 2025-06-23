import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Bessel functions of the first kind at x=1
j0 = mp.besselj(0, 1)  # J_0(1)
j1 = mp.besselj(1, 1)  # J_1(1)

# Compute the difference between Bessel functions
bessel_diff = j0 - j1

# Multiply by pi to get final result
result = mp.pi * bessel_diff

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))