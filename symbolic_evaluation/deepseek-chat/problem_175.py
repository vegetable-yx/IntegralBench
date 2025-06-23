import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Compute pi^3
pi_cubed = mp.pi ** 3

# Compute the first term: pi^3 / 48
term1 = pi_cubed / 48

# Compute natural log of 2
ln2 = mp.ln(2)

# Square the natural log of 2
ln2_sq = ln2 ** 2

# Compute the second term: (pi * ln^2(2)) / 8
term2 = (mp.pi * ln2_sq) / 8

# Combine the terms: result = term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))