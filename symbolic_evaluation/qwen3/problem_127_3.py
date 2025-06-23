import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute the modified Bessel function of the first kind I_1(1)
bessel_value = mp.besseli(1, 1)

# Compute the square root of 2
sqrt_two = mp.sqrt(2)

# Multiply the components together
result = sqrt_two * bessel_value

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))