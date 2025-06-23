import mpmath as mp

# Set internal decimal precision to 15 to ensure accuracy to 10 decimal places
mp.dps = 15

# Define constants and fundamental values
pi = mp.pi
ln2 = mp.log(2)  # Natural logarithm of 2
ln3 = mp.log(3)  # Natural logarithm of 3
G = mp.catalan   # Catalan's constant

# Compute each term of the expression separately

# Term 1: (π/6) * (ln2)^2
term1 = (pi / 6) * (ln2 ** 2)

# Term 2: π^3 / 324
term2 = (pi ** 3) / 324

# Term 3: (π/8) * (ln3)^2
term3 = (pi / 8) * (ln3 ** 2)

# Term 4: -(G * ln2) / 2
term4 = - (G * ln2) / 2

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))