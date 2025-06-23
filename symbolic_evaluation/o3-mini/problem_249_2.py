import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the square root of 5
sqrt5 = mp.sqrt(5)

# Subtract 2 from the square root of 5
sqrt5_minus_2 = sqrt5 - 2

# Multiply by pi/2
result = (mp.pi / 2) * sqrt5_minus_2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))