import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Define the constant sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate the argument for the dilogarithms: c = sqrt(2) / (1 + sqrt(2))
denom = 1 + sqrt2
c = sqrt2 / denom

# Compute the two dilogarithm terms
term1 = 2 * mp.polylog(2, c)       # 2 * Li_2(c)
term2 = -2 * mp.polylog(2, -c)      # -2 * Li_2(-c)

# Compute the logarithmic term: (pi/2) * [ln(1 + sqrt(2))]^2
log_term = mp.log(denom)            # ln(1 + sqrt(2))
term3 = (mp.pi / 2) * (log_term ** 2)

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))