import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Compute first term: pi^3 divided by 48
term1 = pi_cubed / 48

# Compute second term: pi divided by 4
term2 = mp.pi / 4

# Subtract the second term from the first term
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))