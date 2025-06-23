import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Struve function H_0(2)
struve_h0 = mp.struveh(0, 2)

# Calculate Bessel function of the second kind Y_0(2)
bessel_y0 = mp.bessely(0, 2)

# Compute the difference between Struve and Bessel functions
difference = struve_h0 - bessel_y0

# Multiply by π/8 to get final result
result = (mp.pi / 8) * difference

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))