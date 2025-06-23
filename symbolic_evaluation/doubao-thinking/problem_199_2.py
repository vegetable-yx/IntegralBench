import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Struve H function of order 0 at 1
struve_h0 = mp.struveh(0, 1)

# Calculate Bessel function of the second kind of order 0 at 1
bessel_y0 = mp.bessely(0, 1)

# Compute the difference between Struve H0 and Bessel Y0
difference = struve_h0 - bessel_y0

# Calculate the final result using the analytical expression
result = mp.sqrt(2) * (mp.pi / 2) * difference

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))