import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi ** 2

# Divide by 8 to get the result
result = pi_sq / 8

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))