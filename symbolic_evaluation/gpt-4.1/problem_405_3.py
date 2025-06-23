import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate exponential terms individually
exp1 = mp.exp(1)
exp2 = mp.exp(2)
exp3 = mp.exp(3)
exp4 = mp.exp(4)

# Compute terms with coefficients
term1 = 3
term2 = 2 * exp1
term3 = 2 * exp2
term4 = 2 * exp3
term5 = -exp4  # Negative sign applied to exp(4)

# Sum all terms for final result
result = term1 + term2 + term3 + term4 + term5

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))