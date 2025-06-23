import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute Bessel function of the first kind J0 at 2
j0_val = mp.besselj(0, 2)

# Compute Struve function H0 at 2 (using Hankel Struve notation)
h0_val = mp.struveh(0, 2)

# Compute Bessel function of the first kind J1 at 2
j1_val = mp.besselj(1, 2)

# Compute Struve function H1 at 2 (using Hankel Struve notation)
h1_val = mp.struveh(1, 2)

# Calculate the expression inside the brackets: J0(2)*H0(2) - J1(2)*H1(2)
inner_expr = j0_val * h0_val - j1_val * h1_val

# Multiply by π/2
result = (mp.pi / 2) * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))