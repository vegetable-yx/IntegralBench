import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Calculate pi
pi = mp.pi

# Compute the product of sqrt(3) and pi
sqrt3_pi = sqrt3 * pi

# Divide the product by 2
sqrt3_pi_over_2 = sqrt3_pi / 2

# Calculate the modified Bessel function I_0 at 3
bessel_i0_3 = mp.besseli(0, 3)

# Multiply all components to get the final result
result = sqrt3_pi_over_2 * bessel_i0_3

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))