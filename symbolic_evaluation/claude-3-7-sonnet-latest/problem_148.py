import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the square of pi
pi_sq = mp.pi ** 2

# Divide the result by 4
result = pi_sq / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))