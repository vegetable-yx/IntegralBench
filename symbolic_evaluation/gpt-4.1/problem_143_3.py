import mpmath as mp
mp.dps = 15

# Compute modified Bessel function of order 0 at 2
I0_2 = mp.besseli(0, 2)
# Compute modified Bessel function of order 1 at 2
I1_2 = mp.besseli(1, 2)

# Calculate the expression inside the brackets
bracket = 1 + I1_2 - I0_2

# Multiply by pi/8 to get the final result
result = (mp.pi / 8) * bracket

print(mp.nstr(result, n=10))