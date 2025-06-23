import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Define necessary constants and logarithms
pi = mp.pi
ln2 = mp.log(2)
ln3 = mp.log(3)
catalan = mp.catalan  # Catalan's constant

# Break down the expression into manageable terms
# Term1: - (pi/6) * (ln2)^2
term1 = - (pi / 6) * (ln2 ** 2)

# Term2: (pi^3) / 72
term2 = (pi ** 3) / 72

# Term3: (pi/12) * (ln3)^2
term3 = (pi / 12) * (ln3 ** 2)

# Term4: (pi/6) * ln2 * ln3
term4 = (pi / 6) * ln2 * ln3

# Term5: (1/2) * catalan * (ln3 - 2*ln2)
term5 = (1/2) * catalan * (ln3 - 2 * ln2)

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4 + term5

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))