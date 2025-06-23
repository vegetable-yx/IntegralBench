import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi raised to the power of 3/2
pi_power = mp.power(mp.pi, 1.5)

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Compute denominator: 2 * sqrt(2)
denominator = 2 * sqrt_2

# Final result: pi^(3/2) / (2 * sqrt(2))
result = pi_power / denominator

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))