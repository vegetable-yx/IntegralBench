import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate each term separately
# Term 1: pi cubed divided by 1296
term1 = mp.power(mp.pi, 3) / 1296

# Term 2: pi divided by 24
term2 = mp.pi / 24

# Term 3: negative square root of 3 divided by 108
term3 = -mp.sqrt(3) / 108

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))