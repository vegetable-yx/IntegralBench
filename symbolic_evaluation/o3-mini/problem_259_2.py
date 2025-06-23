import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Compute Bessel function of the first kind, order 0 at z=1
j0 = mp.besselj(0, 1)

# Compute Bessel function of the first kind, order 1 at z=1
j1 = mp.besselj(1, 1)

# Compute Struve function (Hankel), order 0 at z=1
h0 = mp.struveh(0, 1)

# Compute Struve function (Hankel), order 1 at z=1
h1 = mp.struveh(1, 1)

# Calculate term1: J1(1) * H0(1)
term1 = j1 * h0

# Calculate term2: J0(1) * H1(1)
term2 = j0 * h1

# Compute the difference: term1 - term2
diff = term1 - term2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))