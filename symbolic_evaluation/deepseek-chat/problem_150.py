import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 2 to obtain the result
result = pi_sq / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))