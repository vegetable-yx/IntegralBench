import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate individual square roots
sqrt6 = mp.sqrt(6)
sqrt22 = mp.sqrt(22)
sqrt3 = mp.sqrt(3)
sqrt11 = mp.sqrt(11)

# Compute the argument of the logarithm
log_numerator = 7 + 2 * sqrt22
log_denominator = 3 + 4 * sqrt3
log_argument = log_numerator / log_denominator

# Compute the logarithm term
log_term = mp.log(log_argument)

# Compute the expression inside the parentheses: 1 + log_term
inner_expr = 1 + log_term

# Multiply by 15*sqrt6
term1 = 15 * sqrt6 * inner_expr

# Compute 7*sqrt11
term2 = 7 * sqrt11

# Combine terms: term1 - term2
numerator_inner = term1 - term2

# Multiply by 4
numerator = 4 * numerator_inner

# Divide by 63
result = numerator / 63

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))