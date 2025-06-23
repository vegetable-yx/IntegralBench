import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute modified Bessel functions of the first kind
I0 = mp.besseli(0, 5)
I1 = mp.besseli(1, 5)
I2 = mp.besseli(2, 5)

# Calculate the combination of Bessel functions
term_4I1 = 4 * I1
combined_bessel = term_4I1 - I0 - I2

# Compute the final result with coefficients
coefficient = (125 * mp.pi) / 16
result = coefficient * combined_bessel

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))