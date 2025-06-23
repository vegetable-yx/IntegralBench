import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi**2

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Calculate denominator: 8 * sqrt(2)
denominator = 8 * sqrt_two

# Final result: pi^2 divided by (8 * sqrt(2))
result = pi_squared / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))