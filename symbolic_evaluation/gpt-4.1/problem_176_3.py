import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the first term: pi^3 / 12
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 12

# Calculate the second term: pi * (ln(2))^2
ln2 = mp.log(2)
ln2_sq = ln2 ** 2
term2 = mp.pi * ln2_sq

# Combine the terms: result = term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))