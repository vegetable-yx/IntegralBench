import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Calculate pi squared divided by 8
term1 = pi_sq / 8

# Calculate pi divided by 2
term2 = mp.pi / 2

# Compute the result: pi²/8 - pi/2 + 1
result = term1 - term2 + 1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))