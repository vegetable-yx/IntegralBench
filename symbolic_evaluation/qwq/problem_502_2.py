import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the rational number component
term1 = mp.mpf(10747)/10

# Calculate the logarithmic component
term2 = 6 * mp.log(2)

# Combine both terms for final result
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))