import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 0 at 6
bessel_i0 = mp.besseli(0, 6)

# Compute the modified Struve function of order 0 at 6
struve_l0 = mp.struvel(0, 6)

# Calculate the difference: I0(6) - L0(6)
diff = bessel_i0 - struve_l0

# Multiply by π/6 to get the final result
result = (mp.pi / 6) * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))