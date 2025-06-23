import mpmath as mp

mp.dps = 15

# Compute Bessel functions at z=1
j0_1 = mp.besselj(0, 1)
j1_1 = mp.besselj(1, 1)

# Compute Struve functions at z=1
h0_1 = mp.struveh(0, 1)
h1_1 = mp.struveh(1, 1)

# Calculate the combination of Bessel and Struve functions
struve_combination = j1_1 * h0_1 - j0_1 * h1_1

# Multiply by π²/2 factor
pi_factor = mp.pi ** 2 / 2

# Compute final result
result = pi_factor * struve_combination

# Print with 10 decimal precision
print(mp.nstr(result, n=10))