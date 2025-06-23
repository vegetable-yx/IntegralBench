import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(3) and divide by 24
sqrt3 = mp.sqrt(3)
term1 = sqrt3 / 24

# Calculate pi divided by 36
term2 = mp.pi / 36

# Sum the two terms
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))