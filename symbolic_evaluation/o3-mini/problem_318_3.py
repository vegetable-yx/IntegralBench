import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.mp.dps = 15

# Compute each term separately for clarity
# Calculate the Struve H function for order 0 at z=1
H0 = mp.struveh(0, 1)

# Calculate the Struve H function for order 1 at z=1
H1 = mp.struveh(1, 1)

# Calculate the Bessel function of the second kind (Weber function) for order 0 at z=1
Y0 = mp.bessely(0, 1)

# Calculate the Bessel function of the second kind for order 1 at z=1
Y1 = mp.bessely(1, 1)

# Combine the terms according to the expression:
# (1/4) * [2*H0 - H1 - 2*Y0 + Y1]
result = (2 * H0 - H1 - 2 * Y0 + Y1) / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))