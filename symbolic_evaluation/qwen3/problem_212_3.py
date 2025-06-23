import mpmath as mp

# Set internal precision to 15 decimal places for accurate calculations
mp.dps = 15

# Calculate J0(1) - Bessel function of the first kind of order 0 at x=1
j0_val = mp.besselj(0, 1)

# Calculate J1(1) - Bessel function of the first kind of order 1 at x=1
j1_val = mp.besselj(1, 1)

# Compute the difference: J0(1) - J1(1)
diff = j0_val - j1_val

# Multiply the difference by pi
result = mp.pi * diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))