import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^4
pi_sq = mp.pi**2  # pi squared
pi_fourth = pi_sq**2  # pi^4

# Multiply by 7 and divide by 16
result = (7 * pi_fourth) / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))