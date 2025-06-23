import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Compute π divided by sqrt(2)
pi_over_sqrt2 = mp.pi / sqrt_two

# Compute the modified Bessel function of the first kind I_0 at 1
i0_value = mp.besseli(0, 1)

# Multiply the components to get the final result
result = pi_over_sqrt2 * i0_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))