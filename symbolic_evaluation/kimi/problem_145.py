import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Struve H function of order 0 at 2
struve_h0 = mp.struveh(0, 2)

# Compute Bessel Y function of order 0 at 2
bessel_y0 = mp.bessely(0, 2)

# Calculate the final result using the analytical expression components
result = (mp.pi / 2) * (struve_h0 - bessel_y0)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))