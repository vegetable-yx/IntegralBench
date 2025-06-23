import mpmath as mp

# Set internal decimal places for calculations
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi ** 2

# Divide by 8
pi_sq_over_8 = pi_sq / 8

# Subtract 1 to get the final result
result = pi_sq_over_8 - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))