import mpmath as mp
mp.dps = 15

# Compute modified Bessel functions of the first kind at 1
I0 = mp.besseli(0, 1)
I1 = mp.besseli(1, 1)

# Calculate the difference between the Bessel functions
bessel_diff = I0 - I1

# Multiply by pi to get the final result
result = mp.pi * bessel_diff

print(mp.nstr(result, n=10))