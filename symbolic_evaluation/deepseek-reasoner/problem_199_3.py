import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Get π constant from mpmath
pi_val = mp.pi

# Compute Bessel function of the first kind J₁(1)
bessel_j1 = mp.besselj(1, 1)

# Multiply components together
result = sqrt2 * pi_val * bessel_j1

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))