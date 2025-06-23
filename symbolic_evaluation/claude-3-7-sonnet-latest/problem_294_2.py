import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Calculate the square root of 3
sqrt_3 = mp.sqrt(3)

# Calculate the denominator: 2 * sqrt(3)
denominator = 2 * sqrt_3

# Compute the final result: pi^2 / (2*sqrt(3))
result = pi_squared / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))