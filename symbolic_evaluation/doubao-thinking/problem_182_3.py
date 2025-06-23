import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Calculate the logarithm term: ln(2 + sqrt(5))
log_arg = 2 + mp.sqrt(5)
log_term = mp.log(log_arg)

# Calculate the algebraic fraction: (sqrt(5) - 1) / 2
sqrt5 = mp.sqrt(5)
algebraic_term = (sqrt5 - 1) / 2

# Sum the two terms: log_term + algebraic_term
sum_terms = log_term + algebraic_term

# Multiply by pi to get the final result
result = mp.pi * sum_terms

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))