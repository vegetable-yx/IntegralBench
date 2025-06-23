import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate ln(5)
ln5 = mp.log(5)

# Calculate pi squared
pi_sq = mp.pi ** 2

# Compute pi squared divided by 4
pi_sq_over_4 = pi_sq / 4

# Subtract pi from pi_sq_over_4
term1_part = pi_sq_over_4 - mp.pi

# Multiply by ln(5) to complete the first term
term1 = ln5 * term1_part

# Compute the dilogarithm of 4/5
dilog = mp.polylog(2, mp.mpf(4)/5)

# Multiply the dilogarithm by 2 for the second term
term2 = 2 * dilog

# Add both terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))