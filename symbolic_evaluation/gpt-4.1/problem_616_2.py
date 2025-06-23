import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute (ln2)^2
ln2_squared = ln2**2

# Calculate first term: (1/4) * (ln2)^2
term1 = (1/4) * ln2_squared

# Compute pi squared
pi_squared = mp.pi**2

# Calculate second term: pi^2 / 48
term2 = pi_squared / 48

# Combine terms: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))