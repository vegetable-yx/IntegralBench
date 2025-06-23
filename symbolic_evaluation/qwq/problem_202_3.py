import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Bessel function of the first kind J0 at z=1
bessel_term = mp.besselj(0, 1)

# Multiply by π to get the final result
result = mp.pi * bessel_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))