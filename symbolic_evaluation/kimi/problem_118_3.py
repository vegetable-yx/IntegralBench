import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Compute (sqrt(2) - 1)
sqrt_minus_one = sqrt_two - 1

# Compute (pi^2 / 2) * (sqrt(2) - 1)
result = (pi_sq / 2) * sqrt_minus_one

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))