import mpmath as mp
mp.dps = 15

# Calculate the modified Bessel function of the first kind I_1(2)
i1_value = mp.besseli(1, 2)

# Calculate π/4
pi_over_4 = mp.pi / 4

# Multiply components to get final result
result = pi_over_4 * i1_value

print(mp.nstr(result, n=10))