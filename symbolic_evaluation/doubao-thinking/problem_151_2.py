import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi squared
pi_sq = mp.power(mp.pi, 2)

# Divide by 2 to get the final result
result = pi_sq / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))