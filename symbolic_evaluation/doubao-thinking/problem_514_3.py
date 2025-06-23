import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi/6
term1 = mp.pi / 6

# Calculate sqrt(3)/8
term2 = mp.sqrt(3) / 8

# Sum the two terms
result = term1 + term2

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))