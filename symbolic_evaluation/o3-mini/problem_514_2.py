import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi/6
term1 = mp.pi / 6

# Calculate sqrt(3)/8
term2 = mp.sqrt(3) / 8

# Sum the two terms to get the result
result = term1 + term2

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))