import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute each term of the expression separately

# Term 1: (5 * pi^2 * ln(2)) / 4
pi_squared = mp.pi ** 2
ln2 = mp.log(2)
term1 = (5 * pi_squared * ln2) / 4

# Term 2: pi^4 / 48
pi_fourth = mp.pi ** 4
term2 = pi_fourth / 48

# Term 3: (3 * pi^2 * zeta(3)) / 4
zeta_3 = mp.zeta(3)
term3 = (3 * pi_squared * zeta_3) / 4

# Combine the terms: term1 - term2 + term3
result = term1 - term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))