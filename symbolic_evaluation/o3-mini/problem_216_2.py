import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute each component of the expression
# pi: mathematical constant π
pi_val = mp.pi

# sqrt(2): square root of 2
sqrt2_val = mp.sqrt(2)

# J_0(1): Bessel function of the first kind, order 0 at 1
besselj_val = mp.besselj(0, 1)

# Multiply components: π * √2 * J_0(1)
result = pi_val * sqrt2_val * besselj_val

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))