import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

x = 2  # Upper limit of integration

# Compute Bessel functions K0 and K1 at x
k0 = mp.besselk(0, x)
k1 = mp.besselk(1, x)

# Compute modified Struve functions L0 and L1 at x
l0 = mp.struvel(0, x)
l1 = mp.struvel(1, x)

# Calculate the combination term from the analytical formula
combination = x * (k1 * l0 + k0 * l1)

# Compute the final result using the analytical expression
result = (mp.pi / 2) * (1 - combination)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))