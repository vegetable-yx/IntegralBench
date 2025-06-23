import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Compute Bessel functions of the first kind at x=1
j0 = mp.besselj(0, 1)  # J_0(1)
j1 = mp.besselj(1, 1)  # J_1(1)

# Sum the Bessel function values
sum_bessel = j0 + j1

# Multiply by pi/2 and get final result
result = (mp.pi / 2) * sum_bessel

# Print result with 10 decimal places
print(mp.nstr(result, n=10))