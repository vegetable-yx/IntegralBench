import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the first logarithm term: ln(2 + sqrt(3))
log_term1 = mp.log(2 + sqrt3)

# Compute the second logarithm term: ln(sqrt(3))
log_term2 = mp.log(sqrt3)

# Subtract the two logarithm terms
result = log_term1 - log_term2

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))