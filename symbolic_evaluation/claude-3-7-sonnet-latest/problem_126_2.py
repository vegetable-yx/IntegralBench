import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Multiply by 2
two_pi_sq = 2 * pi_sq

# Divide by 3 to get the final result
result = two_pi_sq / 3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))