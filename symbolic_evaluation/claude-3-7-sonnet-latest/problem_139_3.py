import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate modified Bessel function of first kind, order 0 at 2.0
bessel_i0 = mp.besseli(0, 2.0)

# Calculate modified Struve function, order 0 at 2.0
struve_l0 = mp.struvel(0, 2.0)

# Compute the difference: I_0(2.0) - L_0(2.0)
diff = bessel_i0 - struve_l0

# Multiply by pi to get final result
result = mp.pi * diff

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))