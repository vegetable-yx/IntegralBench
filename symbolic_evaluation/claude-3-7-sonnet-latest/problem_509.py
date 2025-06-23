import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 2π/3
term1 = (2 * mp.pi) / 3

# Calculate 4 * square root of 3
term2 = 4 * mp.sqrt(3)

# Sum the two terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))