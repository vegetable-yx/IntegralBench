import mpmath as mp

# Set internal decimal places for sufficient precision
mp.dps = 15

# Compute pi using mpmath constant
pi_val = mp.pi

# Compute natural logarithms
ln2 = mp.log(2)
ln3 = mp.log(3)

# Calculate the first term: (pi/8)*ln(2)
term1 = (pi_val / 8) * ln2

# Calculate the second term: (pi/16)*ln(3)
term2 = (pi_val / 16) * ln3

# Combine terms: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))