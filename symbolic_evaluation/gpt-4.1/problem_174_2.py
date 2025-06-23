import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant a = 0.25
a = mp.mpf('0.25')

# Compute a squared = (0.25)^2 = 0.0625
a_sq = a**2

# Compute the dilogarithm Li_2(a_sq) = Li_2(0.0625)
li2_val = mp.polylog(2, a_sq)

# Multiply by π/4 to get the result: (π/4) * Li_2(0.0625)
result = (mp.pi / 4) * li2_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))