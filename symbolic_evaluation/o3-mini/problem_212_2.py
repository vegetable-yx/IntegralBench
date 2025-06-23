import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Bessel function J0 at x=1
j0_val = mp.besselj(0, 1)

# Compute Bessel function J2 at x=1
j2_val = mp.besselj(2, 1)

# Compute the difference: J0(1) - J2(1)
diff_val = j0_val - j2_val

# Multiply by π/2
result = (mp.pi / 2) * diff_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))