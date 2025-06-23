import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute Bessel functions of the first kind
j0 = mp.besselj(0, 1)
j1 = mp.besselj(1, 1)

# Compute Struve functions
h0 = mp.struveh(0, 1)
h1 = mp.struveh(1, 1)

# Calculate the main expression components
term1 = j1 * h0
term2 = j0 * h1

# Combine terms and multiply by pi^2/4
result = (mp.pi**2 / 4) * (term1 - term2)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))