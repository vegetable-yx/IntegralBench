import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 32 to get the result
result = pi_sq / 32

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))