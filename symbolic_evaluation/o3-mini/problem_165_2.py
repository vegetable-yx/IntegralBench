import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute Struve H function of order 0 at 2
struve_h0 = mp.struveh(0, 2)

# Compute Bessel function of the second kind (Y) of order 0 at 2
bessel_y0 = mp.bessely(0, 2)

# Calculate the difference: H_0(2) - Y_0(2)
diff = struve_h0 - bessel_y0

# Multiply by π/2
result = (mp.pi / 2) * diff

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))