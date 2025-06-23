import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate each term of the expression:
# Result = π³/72 - (π²/12) * ln(2) - (1/2) * ln(2) * Cl₂(π/3) - (1/4) * Cl₃(π/3) + ζ(3)/12

# Term 1: π³/72
term1 = mp.pi**3 / 72

# Term 2: - (π²/12) * ln(2)
term2 = - (mp.pi**2 / 12) * mp.log(2)

# Term 3: - (1/2) * ln(2) * Cl₂(π/3)
# Clausen function of order 2: Cl₂(π/3)
cl2 = mp.clsin(2, mp.pi/3)
term3 = -0.5 * mp.log(2) * cl2

# Term 4: - (1/4) * Cl₃(π/3)
# Clausen function of order 3: Cl₃(π/3)
cl3 = mp.clsin(3, mp.pi/3)
term4 = -0.25 * cl3

# Term 5: ζ(3)/12
zeta3 = mp.zeta(3)
term5 = zeta3 / 12

# Sum all terms
result = term1 + term2 + term3 + term4 + term5

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))