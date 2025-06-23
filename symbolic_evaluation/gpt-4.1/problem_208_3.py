import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define components of the analytical expression
pi = mp.pi
G = mp.catalan  # Catalan's constant

# Compute each term in the expression: π³/48 + π/8 - G/2
term1 = (pi ** 3) / 48  # π³/48
term2 = pi / 8           # π/8
term3 = -G / 2           # -G/2

# Sum all terms
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))