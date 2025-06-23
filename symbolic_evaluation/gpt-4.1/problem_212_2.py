import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate Bessel function of the first kind of order 0 at z=1
j0_val = mp.besselj(0, 1)

# Calculate Bessel function of the first kind of order 2 at z=1
j2_val = mp.besselj(2, 1)

# Sum the Bessel function values
bessel_sum = j0_val + j2_val

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * bessel_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))