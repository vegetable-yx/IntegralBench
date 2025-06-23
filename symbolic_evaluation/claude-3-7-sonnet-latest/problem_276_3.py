import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the modified Bessel function of the first kind I_0 at 3
bessel_value = mp.besseli(0, 3)

# Multiply by pi and sqrt3 to get the final result
result = mp.pi * sqrt3 * bessel_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))