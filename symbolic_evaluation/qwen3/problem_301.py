import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate (ln2)^2
ln2_squared = ln2**2

# Calculate pi squared
pi_squared = mp.pi**2

# Calculate the term: 4 * ln2
term1 = 4 * ln2

# Calculate the term: 4 * (ln2)^2
term2 = 4 * ln2_squared

# Calculate the term: pi^2 / 12
term3 = pi_squared / 12

# Combine all terms: 4*ln2 - 4*(ln2)^2 - pi^2/12
result = term1 - term2 - term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))