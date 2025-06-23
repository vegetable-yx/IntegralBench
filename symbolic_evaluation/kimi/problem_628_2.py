import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate ln(2) using mpmath's log function
ln2 = mp.log(2)

# Calculate the first term: (1/2) * ln(2)
term1 = mp.mpf(0.5) * ln2

# Calculate the second term: π/4
term2 = mp.pi / 4

# Combine terms to get final result
result = term1 - term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))