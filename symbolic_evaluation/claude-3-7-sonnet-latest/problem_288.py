import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Define fundamental constants
pi = mp.pi
ln2 = mp.log(2)

# Compute intermediate values
pi_cubed = pi ** 3
pi_fifth = pi ** 5
ln2_squared = ln2 ** 2
ln2_cubed = ln2 ** 3

# Calculate term1: (15π³ - π⁵)/120
term1 = (15 * pi_cubed - pi_fifth) / 120

# Calculate term2: π(ln2)²/4
term2 = (pi * ln2_squared) / 4

# Calculate term3: (ln2)³/3
term3 = ln2_cubed / 3

# Combine the terms: term1 - term2 + term3
result = term1 - term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))