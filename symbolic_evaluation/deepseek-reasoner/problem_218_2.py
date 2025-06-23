import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute each component of the expression step by step
ln2 = mp.log(2)  # Natural logarithm of 2

# First term: (π/6) * (ln2)^2
term1 = (mp.pi / 6) * (ln2 ** 2)

# Compute Clausen functions
Cl2_pi3 = mp.clsin(2, mp.pi / 3)  # Cl₂(π/3)
Cl3_2pi3 = mp.clsin(3, 2 * mp.pi / 3)  # Cl₃(2π/3)

# Second term components: sqrt(3)/2 * [Cl₂(π/3)*ln2 - 0.5*Cl₃(2π/3)]
inner_term2 = Cl2_pi3 * ln2 - 0.5 * Cl3_2pi3
term2 = (mp.sqrt(3) / 2) * inner_term2

# Third term: -π³/108
term3 = -(mp.pi ** 3) / 108

# Combine all terms
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))