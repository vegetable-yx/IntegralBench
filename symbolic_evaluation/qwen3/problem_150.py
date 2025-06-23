import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Compute the final result: pi^2 divided by sqrt(2)
result = pi_sq / sqrt_two

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))