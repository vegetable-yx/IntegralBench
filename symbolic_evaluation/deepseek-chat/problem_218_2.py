import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate individual terms
# Term 1: (π/6) * (ln 2)^2
ln2 = mp.log(2)
term1 = (mp.pi / 6) * (ln2 ** 2)

# Term 2: π^3 / 216
term2 = (mp.pi ** 3) / 216

# Term 3: (ln 2)/2 * [Cl_2(π/3) - Cl_2(π)]
cl_pi3 = mp.clsin(2, mp.pi / 3)  # Clausen function Cl_2(π/3)
cl_pi = mp.clsin(2, mp.pi)       # Clausen function Cl_2(π)
term3 = (ln2 / 2) * (cl_pi3 - cl_pi)

# Sum all terms
result = term1 + term2 + term3

# Print result to 10 decimal places
print(mp.nstr(result, n=10))