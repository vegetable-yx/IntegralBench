import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate ln(2)
ln2 = mp.log(2)

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate the expression inside the logarithm: 3 + 2*sqrt(2)
inner_log = 3 + 2 * sqrt2

# Calculate ln(3 + 2*sqrt(2))
log_term = mp.log(inner_log)

# Calculate the coefficient: 3/(2*sqrt(2))
coeff = 3 / (2 * sqrt2)

# Calculate the second term: coeff * log_term
term2 = coeff * log_term

# Calculate the first term: (1/2)*ln(2)
term1 = 0.5 * ln2

# Combine the terms: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))