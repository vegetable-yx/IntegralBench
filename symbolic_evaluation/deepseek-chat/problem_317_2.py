import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Compute term1: pi^2 divided by 3
term1 = pi_squared / 3

# Compute natural log of 2
ln2 = mp.log(2)

# Square the logarithm
ln2_squared = ln2 ** 2

# Compute term2: 4 times (ln2)^2
term2 = 4 * ln2_squared

# Combine the terms: term2 minus term1
result = term2 - term1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))