import mpmath as mp

mp.dps = 15

# Compute modified Bessel functions of the second kind at 2
K0_2 = mp.besselk(0, 2)
K1_2 = mp.besselk(1, 2)

# Compute modified Struve functions at 2
L_minus1_2 = mp.struvel(-1, 2)
L_0_2 = mp.struvel(0, 2)

# Calculate the combination term from special functions
combination = K1_2 * L_minus1_2 + K0_2 * L_0_2
term = 2 * combination

# Final result using the analytical formula
result = (mp.pi / 2) * (1 - term)

print(mp.nstr(result, n=10))