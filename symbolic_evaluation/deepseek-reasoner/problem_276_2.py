import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 3
sqrt_3 = mp.sqrt(3)

# Compute the modified Bessel function of the first kind I_0(3)
bessel_i0 = mp.besseli(0, 3)

# Multiply components to get the final result
result = 2 * sqrt_3 * bessel_i0

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))