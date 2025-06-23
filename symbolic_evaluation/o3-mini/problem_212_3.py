import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute J0(1): Bessel function of the first kind of order 0 at 1
j0_val = mp.besselj(0, 1)

# Compute J1(1): Bessel function of the first kind of order 1 at 1
j1_val = mp.besselj(1, 1)

# Compute the difference: J0(1) - J1(1)
diff = j0_val - j1_val

# Multiply by pi to get the final result
result = mp.pi * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))