import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Bessel function of the first kind of order 0 at 1
J0_1 = mp.besselj(0, 1)

# Compute the term (J0(1) - 1)
term = J0_1 - 1

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))