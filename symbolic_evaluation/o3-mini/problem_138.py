import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute modified Bessel functions of the first kind
I0 = mp.besseli(0, 6)  # I_0(6)
I2 = mp.besseli(2, 6)  # I_2(6)

# Compute modified Struve functions
L0 = mp.struvel(0, 6)  # L_0(6)
L2 = mp.struvel(2, 6)  # L_2(6)

# Combine the terms: I0 - I2 - L0 + L2
inner_sum = I0 - I2 - L0 + L2

# Multiply by π/6
result = (mp.pi / 6) * inner_sum

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))