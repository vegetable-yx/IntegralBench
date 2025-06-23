import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate ln(1 + sqrt(2)) first since it's used in both terms
ln_term = mp.log(1 + mp.sqrt(2))

# Compute the squared term component
squared_term = ln_term**2

# Compute the cubed term component
cubed_term = ln_term**3

# Calculate the first part of the expression: π/8 * (ln(1+√2))²
term1 = (mp.pi / 8) * squared_term

# Calculate the second part of the expression: π/24 * (ln(1+√2))³
term2 = (mp.pi / 24) * cubed_term

# Combine the terms to get final result
result = term1 - term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))