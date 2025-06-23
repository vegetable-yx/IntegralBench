import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute each Bessel function term
I1 = mp.besseli(1, 5)
I2 = mp.besseli(2, 5)
I3 = mp.besseli(3, 5)

# Calculate coefficients multiplied by π
coeff1 = (625 / 32) * mp.pi
coeff2 = (125 / 8) * mp.pi
coeff3 = (125 / 32) * mp.pi

# Compute each term of the expression
term1 = coeff1 * I1
term2 = coeff2 * I2
term3 = coeff3 * I3

# Combine terms to get final result
result = term1 - term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))