import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate (ln(2))^2
ln2 = mp.log(2)
ln2_squared = ln2 ** 2

# Compute first term: (ln2)^2 / 4
term1 = ln2_squared / 4

# Compute second term: pi^2 / 48
pi_squared = mp.pi ** 2
term2 = pi_squared / 48

# Sum the two terms for final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))