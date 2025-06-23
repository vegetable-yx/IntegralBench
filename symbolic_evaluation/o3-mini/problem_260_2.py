import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Evaluate the expression: (π/2) * [J₀(1) H₀(1) - J₁(1) H₁(1)]

# Compute J₀(1): Bessel function of the first kind, order 0 at x=1
j0_val = mp.besselj(0, 1)

# Compute H₀(1): Struve function (Hankel type), order 0 at x=1
h0_val = mp.struveh(0, 1)

# Compute J₁(1): Bessel function of the first kind, order 1 at x=1
j1_val = mp.besselj(1, 1)

# Compute H₁(1): Struve function (Hankel type), order 1 at x=1
h1_val = mp.struveh(1, 1)

# Compute the product terms
term1 = j0_val * h0_val
term2 = j1_val * h1_val

# Combine terms and multiply by π/2
result = (mp.pi / 2) * (term1 - term2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))