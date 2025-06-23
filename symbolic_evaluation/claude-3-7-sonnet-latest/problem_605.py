import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Precompute frequently used constants
sqrt2 = mp.sqrt(2)  # Square root of 2
pi = mp.pi          # Pi constant
ln2 = mp.log(2)     # Natural logarithm of 2

# Calculate the first term: (3 * pi) / (4 * sqrt(2))
term1 = (3 * pi) / (4 * sqrt2)

# Calculate the second term: pi / 16
term2 = pi / 16

# Calculate the third term: ln(2) / (2 * sqrt(2))
term3 = ln2 / (2 * sqrt2)

# Combine the terms: term1 - term2 - term3
result = term1 - term2 - term3

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))