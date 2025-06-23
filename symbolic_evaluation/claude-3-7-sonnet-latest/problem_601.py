import mpmath as mp

# Set decimal places for internal computation
mp.dps = 15

# Calculate each term separately for clarity
# Term 1: -2 * pi
term1 = -2 * mp.pi

# Term 2: (17/4) * arctan(4)
term2 = (17/4) * mp.atan(4)

# Term 3: -2 * ln(2)
term3 = -2 * mp.log(2)

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))