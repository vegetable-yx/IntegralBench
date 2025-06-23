import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Compute the first term: π² / 24
term1 = pi_squared / 24

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Square the natural logarithm of 2
ln2_squared = ln2 ** 2

# Compute the second term: (ln2)^2 / 4
term2 = ln2_squared / 4

# Subtract the second term from the first
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))