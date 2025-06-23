import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Divide pi squared by 4
pi_sq_over_4 = pi_squared / 4

# Calculate 1/sqrt(2)
one_over_sqrt2 = 1 / mp.sqrt(2)

# Compute the term (1 - 1/sqrt(2))
parenthetical_term = 1 - one_over_sqrt2

# Multiply to get the final result
result = pi_sq_over_4 * parenthetical_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))