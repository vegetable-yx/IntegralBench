import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Bessel function of the first kind of order 0 at 2
j0_val = mp.besselj(0, 2)

# Calculate Bessel function of the first kind of order 1 at 2
j1_val = mp.besselj(1, 2)

# Compute the difference: J0(2) - J1(2)
diff = j0_val - j1_val

# Multiply by pi/4 to get the result
result = (mp.pi / 4) * diff

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))