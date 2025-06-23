import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate ln²(2)
ln2 = mp.log(2)
ln2_squared = ln2 ** 2

# Compute first term: (π * ln²2)/6
term1 = (mp.pi * ln2_squared) / 6

# Compute second term: -π³/216
pi_cubed = mp.pi ** 3
term2 = -pi_cubed / 216

# Compute third term: ½ * Li₃(1/2)
li3_half = mp.polylog(3, 0.5)
term3 = 0.5 * li3_half

# Combine all terms
result = term1 + term2 + term3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))