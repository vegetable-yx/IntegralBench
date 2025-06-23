import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate fundamental constants
ln2 = mp.log(2)
pi = mp.pi

# Compute Clausen function values
Cl2 = mp.clsin(2, pi/3)  # Clausen function of order 2 at π/3
Cl3 = mp.clsin(3, pi/3)  # Clausen function of order 3 at π/3

# Calculate individual terms of the expression
term1 = (5 * pi / 12) * (ln2 ** 2)  # (5π/12)(ln2)^2 component
term2 = -(3/2) * ln2 * Cl2          # -(3/2)ln2·Cl₂(π/3) component
term3 = (pi ** 3) / 216             # π³/216 component
term4 = 0.5 * Cl3                   # ½Cl₃(π/3) component

# Combine all terms for final result
result = term1 + term2 + term3 + term4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))