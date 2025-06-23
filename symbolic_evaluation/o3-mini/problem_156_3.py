import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define common constants and values
half = mp.mpf(1)/2
ln2 = mp.log(2)
pi_over_4 = mp.pi / 4

# Calculate the first term: (π/4) * (ln 2)^2
ln2_sq = ln2**2
term1 = pi_over_4 * ln2_sq

# Calculate the second term: ln2 * Li₂(1/2)
li2_half = mp.polylog(2, half)
term2 = ln2 * li2_half

# Calculate the third term: -Li₃(1/2)
li3_half = mp.polylog(3, half)
term3 = -li3_half

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))