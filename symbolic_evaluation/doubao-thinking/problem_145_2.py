import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Shi(2) - the hyperbolic sine integral at 2
shi_val = mp.shi(2)

# Calculate cosh(2) - hyperbolic cosine of 2
cosh_val = mp.cosh(2)

# Compute the second term: (cosh(2) - 1) / 2
second_term = (cosh_val - 1) / 2

# Combine the results: Shi(2) minus the second term
result = shi_val - second_term

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))