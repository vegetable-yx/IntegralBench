import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute pi
pi_val = mp.pi

# Compute ln(2)
ln2_val = mp.log(2)

# Compute Li_2(1/2) - dilogarithm
li2_half = mp.polylog(2, 0.5)

# Compute Li_3(1/2) - trilogarithm
li3_half = mp.polylog(3, 0.5)

# Compute pi^3
pi_cubed = pi_val**3

# Compute (ln(2))^2
ln2_squared = ln2_val**2

# Compute term1: pi^3
term1 = pi_cubed

# Compute term2: 4 * pi * (ln(2))^2
term2 = 4 * pi_val * ln2_squared

# Compute term3: -8 * ln(2) * Li_2(1/2)
term3 = -8 * ln2_val * li2_half

# Compute term4: -3 * Li_3(1/2)
term4 = -3 * li3_half

# Combine terms to form the numerator
numerator = term1 + term2 + term3 + term4

# Denominator is 32
denominator = 32

# Final result: - (numerator) / denominator
result = -numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))