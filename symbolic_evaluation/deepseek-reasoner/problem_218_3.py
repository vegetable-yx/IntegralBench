import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute fundamental constants
pi = mp.pi
ln2 = mp.log(2)

# Calculate Clausen functions
cl2 = mp.clsin(2, pi/3)  # Clausen function Cl₂(π/3)
cl3 = mp.clsin(3, pi/3)  # Clausen function Cl₃(π/3)

# Compute individual terms of the expression
term1 = pi**3 / 108
term2 = (pi * ln2**2) / 6
term3 = ln2 * cl2
term4 = 0.5 * cl3

# Combine all terms to get final result
result = term1 + term2 - term3 - term4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))