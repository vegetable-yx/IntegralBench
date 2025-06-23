import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# First term: pi^2 divided by 48
term1 = pi_sq / 48

# Natural logarithm of 2
ln2 = mp.log(2)

# Square of ln2
ln2_sq = ln2 ** 2

# Second term: (ln2)^2 divided by 4
term2 = ln2_sq / 4

# Sum both terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))