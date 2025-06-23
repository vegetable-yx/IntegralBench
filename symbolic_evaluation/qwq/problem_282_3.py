import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Calculate the square root of pi/2
sqrt_pi_over_2 = mp.sqrt(mp.pi / 2)

# Calculate the modified Bessel function of the first kind of order 1/4 at 4
bessel_term = mp.besseli(0.25, 4)

# Multiply the components to get the final result
result = sqrt_pi_over_2 * bessel_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))