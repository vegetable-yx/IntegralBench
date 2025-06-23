import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π^3 term
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 144

# Calculate logarithmic term (2π/9) * ln(2)
ln2 = mp.log(2)
term2 = (2 * mp.pi / 9) * ln2

# Calculate constant term (37π/216)
term3 = (37 * mp.pi) / 216

# Combine all terms
result = term1 + term2 - term3

# Print result with 10 decimal places
print(mp.nstr(result, n=10))