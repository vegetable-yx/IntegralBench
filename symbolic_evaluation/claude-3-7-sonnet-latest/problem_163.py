import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate term with pi squared: (59 * pi^2) / 24
pi_sq = mp.pi ** 2
term1 = (59 * pi_sq) / 24

# Calculate term with Catalan's constant: (65 * G) / 8
catalan = mp.catalan
term2 = (65 * catalan) / 8

# Combine terms: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))