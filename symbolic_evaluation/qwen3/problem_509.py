import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the first term: (2π)/3
term1 = (2 * mp.pi) / 3

# Calculate the second term: 4√3
term2 = 4 * mp.sqrt(3)

# Combine both terms for final result
result = term1 + term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))