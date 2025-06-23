import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate pi/6
term1 = mp.pi / 6

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Calculate sqrt(3)/8
term2 = sqrt3 / 8

# Sum the two terms
result = term1 + term2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))