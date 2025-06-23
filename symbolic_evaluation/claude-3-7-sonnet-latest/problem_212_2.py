import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate π using mpmath constant
pi_val = mp.pi

# Compute Bessel function of the first kind of order 1 at 1.0
j1_val = mp.besselj(1, 1.0)

# Multiply π by the Bessel function result
result = pi_val * j1_val

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))