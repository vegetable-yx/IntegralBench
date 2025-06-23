import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Compute modified Bessel functions of the first kind
i1 = mp.besseli(1, 5)  # I_1(5)
i2 = mp.besseli(2, 5)  # I_2(5)

# Calculate the combination term
combination = 3 * i1 - i2

# Compute the constant coefficient (125/8)*π
coefficient = (mp.mpf(125) / 8) * mp.pi

# Calculate final result
result = coefficient * combination

# Print result with 10 decimal places
print(mp.nstr(result, n=10))