import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Bessel function J0 at 1
j0_val = mp.besselj(0, 1)

# Calculate Bessel function J2 at 1
j2_val = mp.besselj(2, 1)

# Compute numerator: 8 * J0(1) - 4 * J2(1)
numerator = 8 * j0_val - 4 * j2_val

# Divide by 3 to get final result
result = numerator / 3

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))