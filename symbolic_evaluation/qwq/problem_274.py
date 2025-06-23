import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate modified Bessel functions of the first kind
I1 = mp.besseli(1, 5)  # Compute I_1(5)
I2 = mp.besseli(2, 5)  # Compute I_2(5)

# Calculate the combination of Bessel functions
combination = 2 * I1 - I2

# Multiply by the constant factor (125π/8)
result = (125 * mp.pi / 8) * combination

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))