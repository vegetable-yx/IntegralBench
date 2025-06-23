import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute J_0(2) - Bessel function of the first kind of order 0 at 2
bessel_term = mp.besselj(0, 2)

# Calculate the difference (1 - J_0(2))
difference = 1 - bessel_term

# Multiply by 1/4 to get the final result
result = 0.25 * difference

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))