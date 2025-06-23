import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the modified Bessel functions of the first kind
I1_6 = mp.besseli(1, 6)
I2_6 = mp.besseli(2, 6)

# Calculate the modified Bessel functions of the second kind
K1_6 = mp.besselk(1, 6)
K2_6 = mp.besselk(2, 6)

# Compute the products: I1(6)*K2(6) and I2(6)*K1(6)
product1 = I1_6 * K2_6
product2 = I2_6 * K1_6

# Calculate the difference: I1(6)K2(6) - I2(6)K1(6)
difference = product1 - product2

# Multiply by the factor 1/3
result = difference / 3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))