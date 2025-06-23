import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate golden ratio related constants
sqrt5 = mp.sqrt(5)  # Compute the square root of 5
phi = (1 + sqrt5) / 2  # Golden ratio φ = (1 + √5)/2
neg_phi = (1 - sqrt5) / 2  # Negative counterpart (1 - √5)/2

# Compute the natural logarithm of the golden ratio
log_phi = mp.log(phi)

# Calculate the first term: (π/8) * (ln(φ))²
term1 = (mp.pi / 8) * (log_phi ** 2)

# Compute the dilogarithm terms
# Li₂((1 - √5)/2) = Li₂(neg_phi)
dilog1 = mp.polylog(2, neg_phi)
# Li₂((√5 - 1)/2) = Li₂(-neg_phi) since (√5-1)/2 = -neg_phi
dilog2 = mp.polylog(2, -neg_phi)

# Calculate the second term: (1/4) * (Li₂(neg_phi) - Li₂(-neg_phi))
term2 = (1/4) * (dilog1 - dilog2)

# Sum both terms to get the final result
result = term1 + term2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))