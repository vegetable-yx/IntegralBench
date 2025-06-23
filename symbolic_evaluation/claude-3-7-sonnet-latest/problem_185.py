import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Calculate square root of 8
sqrt8 = mp.sqrt(8)

# Compute the term in parentheses: (4 - sqrt(8))
paren_term = 4 - sqrt8

# Multiply pi squared by the parentheses term
numerator = pi_sq * paren_term

# Divide by 64 to get the final result
result = numerator / 64

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))