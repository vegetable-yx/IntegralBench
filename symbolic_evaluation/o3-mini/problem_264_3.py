import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define the parameter 'a' (example value, can be modified)
a = 1.0

# Compute Bessel functions of the first kind
J0 = mp.besselj(0, a)  # J₀(a)
J1 = mp.besselj(1, a)  # J₁(a)

# Compute Struve functions (Hankel Struve)
H0 = mp.struveh(0, a)  # 𝐇₀(a)
H1 = mp.struveh(1, a)  # 𝐇₁(a)

# Calculate intermediate products
prod1 = J0 * H0        # J₀(a)𝐇₀(a)
prod2 = J1 * H1        # J₁(a)𝐇₁(a)

# Compute the expression inside the parentheses
inner_expr = 1 + prod1 - prod2

# Multiply by π/(2a)
result = (mp.pi / (2 * a)) * inner_expr

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))