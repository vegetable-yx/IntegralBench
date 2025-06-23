import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define fundamental constants
pi = mp.pi
catalan = mp.catalan  # Catalan's constant
ln2 = mp.ln(2)        # Natural logarithm of 2

# Compute individual terms of the analytical expression
# Term 1: π²/32
term1 = pi**2 / 32

# Term 2: -π/8
term2 = -pi / 8

# Term 3: -π·ln(2)/16
term3 = - (pi * ln2) / 16

# Term 4: G/4 (positive Catalan term)
term4 = catalan / 4

# Term 5: -π·G/8 (negative Catalan term)
term5 = - (pi * catalan) / 8

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4 + term5

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))