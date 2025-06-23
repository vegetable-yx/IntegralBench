import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi**2

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate denominator: 2 * sqrt(2)
denominator = 2 * sqrt2

# Compute the result: pi^2 / (2 * sqrt(2))
result = pi_sq / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))