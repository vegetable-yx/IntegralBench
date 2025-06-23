import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the modified Bessel function of the first kind I_0(4)
bessel_term = mp.besseli(0, 4)

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Multiply all components: π * sqrt(2) * I_0(4)
result = mp.pi * sqrt_two * bessel_term

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))