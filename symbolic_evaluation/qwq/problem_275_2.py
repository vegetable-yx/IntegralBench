import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the modified Bessel function of the first kind, order 0 at 3
bessel_term = mp.besseli(0, 3)

# Calculate the constant factor: 3 * sqrt(3)
constant_factor = 3 * mp.sqrt(3)

# Compute the final result
result = constant_factor * bessel_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))