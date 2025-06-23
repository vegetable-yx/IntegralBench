import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate J0(1) - Bessel function of the first kind of order 0 at z=1
j0_val = mp.besselj(0, 1)

# Calculate J2(1) - Bessel function of the first kind of order 2 at z=1
j2_val = mp.besselj(2, 1)

# Compute the difference: J0(1) - J2(1)
diff = j0_val - j2_val

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))