import mpmath as mp
mp.dps = 15

# Compute the modified Bessel function of the first kind I_0(2)
i0 = mp.besseli(0, 2)

# Subtract 1 from the Bessel function value
numerator = i0 - 1

# Divide by 2 to get the final result
result = numerator / 2

print(mp.nstr(result, n=10))