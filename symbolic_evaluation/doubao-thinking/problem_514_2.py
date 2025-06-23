import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the first term: pi/6
term1 = mp.pi / 6

# Calculate the second term: sqrt(3)/8
# First compute square root of 3
sqrt3 = mp.sqrt(3)
term2 = sqrt3 / 8

# Sum the two terms
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))