import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the first term: - (pi^2 / 8) * ln(2)
pi_squared = mp.pi**2
denominator1 = 8
factor1 = pi_squared / denominator1
ln2 = mp.log(2)
term1 = -factor1 * ln2

# Calculate the second term: - (pi / 2) * Catalan's constant (G)
catalan = mp.catalan  # Catalan's constant
denominator2 = 2
factor2 = mp.pi / denominator2
term2 = -factor2 * catalan

# Sum the two terms
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))