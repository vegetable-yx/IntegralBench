import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide by 32 to get the final result
result = pi_sq / 32

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))