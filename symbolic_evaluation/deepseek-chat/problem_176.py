import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Compute the first term: pi^3 divided by 12
term1 = pi_cubed / 12

# Compute the second term: pi divided by 2
term2 = mp.pi / 2

# Sum the two terms
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))