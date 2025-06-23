import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate Bessel function of the first kind, order 0 at 1
j0 = mp.besselj(0, 1)

# Calculate Struve function, order 0 at 1
h0 = mp.struveh(0, 1)

# Calculate Bessel function of the first kind, order 1 at 1
j1 = mp.besselj(1, 1)

# Calculate Struve function, order 1 at 1
h1 = mp.struveh(1, 1)

# Compute the product term: J0(1) * H0(1)
term1 = j0 * h0

# Compute the product term: J1(1) * H1(1)
term2 = j1 * h1

# Compute the difference between the two terms
diff = term1 - term2

# Multiply the difference by pi
result = mp.pi * diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))