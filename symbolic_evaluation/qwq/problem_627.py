import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate each term of the expression separately
term1 = mp.pi / 4          # π/4 term
term2 = mp.log(2) / 2     # (ln 2)/2 term
term3 = -1                 # Constant term

# Combine all terms to get final result
result = term1 + term2 + term3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))