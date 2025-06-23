import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the term inside the parentheses: (7 - 4*sqrt2)
inner_term = 7 - 4 * sqrt2

# Multiply by the fraction 16/105
fraction_term = mp.mpf(16) / 105
scaled_inner = fraction_term * inner_term

# Multiply by pi
result = scaled_inner * mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))