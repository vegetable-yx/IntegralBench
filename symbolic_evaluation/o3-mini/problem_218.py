import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the constant ln(2) for reuse
ln2 = mp.log(2)

# Calculate the first term: (π/6) * (ln(2))^2
term1 = (mp.pi / 6) * (ln2 ** 2)

# Calculate the second term: ln(2) * Li_2(1/4)
# Use polylog for the dilogarithm (order 2)
dilog = mp.polylog(2, mp.mpf(1)/4)
term2 = ln2 * dilog

# Calculate the third term: (1/2) * Li_3(1/4)
# Use polylog for the trilogarithm (order 3)
trilog = mp.polylog(3, mp.mpf(1)/4)
term3 = (mp.mpf(1)/2) * trilog

# Combine the terms: term1 - term2 + term3
result = term1 - term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))