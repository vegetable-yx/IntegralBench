import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute pi/6 term
term1 = mp.pi / 6

# Compute sqrt(3) and then divide by 8
term2 = mp.sqrt(3) / 8

# Sum the two terms to get the final result
result = term1 + term2

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))