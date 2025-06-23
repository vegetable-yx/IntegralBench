import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π^4 by raising to the fourth power
pi_power4 = mp.power(pi_value, 4)

# Define the denominator from the analytical expression
denominator = 2560

# Calculate the final result by dividing π^4 by 2560
result = pi_power4 / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))