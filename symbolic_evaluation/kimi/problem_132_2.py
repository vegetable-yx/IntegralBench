import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the modified Bessel function of the first kind I_1(1/2)
bessel_term = mp.besseli(1, 0.5)

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply components: (π * sqrt(2) * bessel_term) / 2
result = (mp.pi * sqrt2 * bessel_term) / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))