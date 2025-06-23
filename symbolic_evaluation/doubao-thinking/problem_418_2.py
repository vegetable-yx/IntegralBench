import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide pi squared by 6
pi_sq_over_6 = pi_sq / 6

# Subtract 1 to get the final result
result = pi_sq_over_6 - 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))